---
title: "Cài đặt Amazon EC2"
date: 2026-07-31
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

## Cài đặt Amazon EC2

Amazon EC2 (Elastic Compute Cloud) là máy chủ ứng dụng chạy **Next.js 16**, **Nginx** reverse proxy và **PM2** process manager cho LifeSync AI Calendar.

---

### Bước 1: Khởi tạo EC2 Instance

1. Đăng nhập **AWS Console** → Tìm kiếm **EC2** → Click **Launch instance**

2. Cấu hình instance:
   - **Name**: `LifeSync-Server`
   - **AMI**: `Ubuntu Server 24.04 LTS (HVM), SSD Volume Type (64-bit x86)` *(Free Tier Eligible)*
   - **Instance type**: `t2.micro` (1 vCPU, 1GB RAM — 750 giờ/tháng Free Tier)
   - **Key pair**: Chọn `lifesync-key` (đã tạo ở phần Chuẩn bị)

![Khởi tạo EC2 Instance Bước 1](images/5-Workshop/picture/ec2/1_setup.png)

---

### Bước 2: Cấu hình Security Group (Tường lửa)

3. Trong **Network settings** → Click **Edit** → Cấu hình **Inbound rules**:

   | Loại | Cổng | Nguồn | Mô tả |
   |---|---|---|---|
   | SSH | 22 | 0.0.0.0/0 | Truy cập terminal từ xa |
   | HTTP | 80 | 0.0.0.0/0 | Lưu lượng web (chuyển hướng sang HTTPS) |
   | HTTPS | 443 | 0.0.0.0/0 | Lưu lượng web an toàn |

![Cài đặt Security Group EC2](images/5-Workshop/picture/ec2/2_setup.png)

4. Giữ nguyên **Storage** mặc định 8GB gp3 (Free Tier) → Click **Launch instance**

---

### Bước 3: Gán Elastic IP (IP tĩnh)

5. Sau khi instance khởi động, vào **EC2 Console** → **Elastic IPs** → **Allocate Elastic IP address** → Click **Allocate**

6. Chọn Elastic IP mới → Click **Actions** → **Associate Elastic IP address**:
   - **Instance**: Chọn `LifeSync-Server`
   - Click **Associate**

![Cài đặt Elastic IP EC2](images/5-Workshop/picture/ec2/3_setup.png)

> **Lưu ý**: Elastic IP đảm bảo IP máy chủ không thay đổi dù EC2 khởi động lại. Rất quan trọng cho cấu hình DNS A Record.

---

### Bước 4: Kết nối và cài đặt phụ thuộc

7. Kết nối với EC2 instance qua SSH:
   ```bash
   chmod 400 lifesync-key.pem
   ssh -i "lifesync-key.pem" ubuntu@<elastic-ip-của-bạn>
   ```

8. Cài đặt Node.js 20, Nginx, Git và PM2:
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
   sudo apt update && sudo apt install -y nodejs nginx git
   sudo npm install -g pm2
   ```

9. Kiểm tra cài đặt:
   ```bash
   node --version   # Hiển thị v20.x.x
   nginx -v         # Hiển thị phiên bản nginx
   pm2 --version    # Hiển thị phiên bản pm2
   ```

![Cài đặt Terminal EC2](images/5-Workshop/picture/ec2/4_terminal_setup.png)

---

### Bước 5: Cấu hình Swap Memory (RAM ảo 2GB)

EC2 t2.micro chỉ có 1GB RAM. Thêm swap memory ngăn Node.js bị crash khi chạy `npm run build`:

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

Kiểm tra swap đã hoạt động:
```bash
free -h
# Hiển thị ~2GB ở dòng Swap
```

---

### Bước 6: Cấu hình Nginx Reverse Proxy

10. Chỉnh sửa cấu hình mặc định Nginx:
    ```bash
    sudo nano /etc/nginx/sites-available/default
    ```

11. Thay toàn bộ nội dung bằng:
    ```nginx
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name phuckhanh.id.vn www.phuckhanh.id.vn;

        location / {
            proxy_pass http://localhost:3000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }
    ```

12. Kiểm tra và khởi động lại Nginx:
    ```bash
    sudo nginx -t && sudo systemctl restart nginx
    sudo systemctl enable nginx
    ```

---

### Bước 7: Triển khai ứng dụng

13. Clone repository:
    ```bash
    cd /home/ubuntu
    git clone https://github.com/<your-username>/ai_calendar_fcaj.git
    cd ai_calendar_fcaj
    ```

14. Tạo file `.env.local` với tất cả biến môi trường:
    ```bash
    nano .env.local
    # Dán tất cả biến môi trường từ phần Chuẩn bị
    ```

15. Cài dependencies, build và khởi động với PM2:
    ```bash
    npm install --legacy-peer-deps
    npm run build
    pm2 start npm --name "lifesync" -- start
    pm2 save
    sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u ubuntu --hp /home/ubuntu
    ```

16. Kiểm tra ứng dụng đang chạy:
    ```bash
    pm2 status
    # Hiển thị "lifesync" với trạng thái "online"
    curl http://localhost:3000
    # Trả về phản hồi HTML
    ```

---

### Bước 8: Cài đặt GitHub Actions CI/CD

17. Trong GitHub repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**:
    - `EC2_HOST`: Địa chỉ Elastic IP của bạn
    - `EC2_SSH_KEY`: Nội dung file `lifesync-key.pem`

18. Tạo `.github/workflows/deploy.yml` trong repository:
    ```yaml
    name: Auto Deploy Next.js to AWS EC2

    on:
      push:
        branches: [ "main" ]

    jobs:
      deploy:
        name: Deploy App to AWS EC2
        runs-on: ubuntu-latest
        steps:
          - name: Checkout Repository
            uses: actions/checkout@v3

          - name: SSH Remote Commands to Deploy
            uses: appleboy/ssh-action@v1.0.0
            with:
              host: ${{ secrets.EC2_HOST }}
              username: ubuntu
              key: ${{ secrets.EC2_SSH_KEY }}
              port: 22
              script: |
                cd /home/ubuntu/ai_calendar_fcaj || exit 1
                git pull origin main
                npm install --legacy-peer-deps
                npm run build
                pm2 restart lifesync || pm2 start npm --name "lifesync" -- start
                pm2 save
    ```

Từ đây, mỗi lần `git push origin main` sẽ **tự động deploy** code mới nhất lên EC2.

---

### ✅ Hoàn thành cài đặt EC2

Máy chủ EC2 của bạn hiện:
- Chạy **Next.js 16** trên cổng 3000 quản lý bởi **PM2**
- Reverse proxy qua **Nginx** trên cổng 80
- Bảo vệ bằng **Elastic IP** tĩnh
- Tự động deploy qua **GitHub Actions CI/CD**

**Tiếp theo**: [Cài đặt Amazon RDS & S3 →](../5.4-RDS-S3/)
