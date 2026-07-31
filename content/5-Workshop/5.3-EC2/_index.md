---
title: "Setup Amazon EC2"
date: 2026-07-31
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

## Setup Amazon EC2

Amazon EC2 (Elastic Compute Cloud) is the application server that runs the **Next.js 16** web application, **Nginx** reverse proxy, and **PM2** process manager for LifeSync AI Calendar.

---

### Step 1: Launch EC2 Instance

1. Sign in to **AWS Console** → Search for **EC2** → Click **Launch instance**

2. Configure the instance:
   - **Name**: `LifeSync-Server`
   - **AMI**: `Ubuntu Server 24.04 LTS (HVM), SSD Volume Type (64-bit x86)` *(Free Tier Eligible)*
   - **Instance type**: `t2.micro` (1 vCPU, 1GB RAM — 750 hours/month Free Tier)
   - **Key pair**: Select `lifesync-key` (created in Prerequisites)

![EC2 Instance Setup Step 1](images/5-Workshop/picture/ec2/1_setup.png)

---

### Step 2: Configure Security Group (Firewall)

3. In **Network settings** → Click **Edit** → Configure **Inbound rules**:

   | Type | Port | Source | Description |
   |---|---|---|---|
   | SSH | 22 | 0.0.0.0/0 | Remote terminal access |
   | HTTP | 80 | 0.0.0.0/0 | Web traffic (redirects to HTTPS) |
   | HTTPS | 443 | 0.0.0.0/0 | Secure web traffic |

![EC2 Security Group Setup](images/5-Workshop/picture/ec2/2_setup.png)

4. Keep **Storage** at the default 8GB gp3 (Free Tier) → Click **Launch instance**

---

### Step 3: Assign Elastic IP (Static IP)

5. After the instance starts, go to **EC2 Console** → **Elastic IPs** → **Allocate Elastic IP address** → Click **Allocate**

6. Select the new Elastic IP → Click **Actions** → **Associate Elastic IP address**:
   - **Instance**: Select `LifeSync-Server`
   - Click **Associate**

![EC2 Elastic IP Setup](images/5-Workshop/picture/ec2/3_setup.png)

> **Note**: Elastic IP ensures your server IP never changes even after EC2 reboots. This is critical for DNS A Record configuration.

---

### Step 4: Connect and Install Dependencies

7. Connect to the EC2 instance via SSH:
   ```bash
   chmod 400 lifesync-key.pem
   ssh -i "lifesync-key.pem" ubuntu@<your-elastic-ip>
   ```

8. Install Node.js 20, Nginx, Git, and PM2:
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
   sudo apt update && sudo apt install -y nodejs nginx git
   sudo npm install -g pm2
   ```

9. Verify installation:
   ```bash
   node --version   # Should show v20.x.x
   nginx -v         # Should show nginx version
   pm2 --version    # Should show pm2 version
   ```

![EC2 Terminal Setup](images/5-Workshop/picture/ec2/4_terminal_setup.png)

---

### Step 5: Configure Swap Memory (2GB Virtual RAM)

EC2 t2.micro only has 1GB RAM. Adding swap memory prevents Node.js from crashing during `npm run build`:

```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

Verify swap is active:
```bash
free -h
# Should show ~2GB under Swap
```

---

### Step 6: Configure Nginx Reverse Proxy

10. Edit the default Nginx configuration:
    ```bash
    sudo nano /etc/nginx/sites-available/default
    ```

11. Replace the entire content with:
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

12. Test and restart Nginx:
    ```bash
    sudo nginx -t && sudo systemctl restart nginx
    sudo systemctl enable nginx
    ```

---

### Step 7: Deploy the Application

13. Clone the repository:
    ```bash
    cd /home/ubuntu
    git clone https://github.com/<your-username>/ai_calendar_fcaj.git
    cd ai_calendar_fcaj
    ```

14. Create the `.env.local` file with all environment variables:
    ```bash
    nano .env.local
    # Paste all environment variables from Prerequisites section
    ```

15. Install dependencies, build, and start with PM2:
    ```bash
    npm install --legacy-peer-deps
    npm run build
    pm2 start npm --name "lifesync" -- start
    pm2 save
    sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u ubuntu --hp /home/ubuntu
    ```

16. Verify the application is running:
    ```bash
    pm2 status
    # Should show "lifesync" with status "online"
    curl http://localhost:3000
    # Should return HTML response
    ```

---

### Step 8: Setup GitHub Actions CI/CD

17. In your GitHub repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**:
    - `EC2_HOST`: Your Elastic IP address
    - `EC2_SSH_KEY`: Contents of your `lifesync-key.pem` file

18. Create `.github/workflows/deploy.yml` in your repository:
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

From now on, every `git push origin main` will **automatically deploy** the latest code to your EC2 instance.

---

### ✅ EC2 Setup Complete

Your EC2 server is now:
- Running **Next.js 16** on port 3000 managed by **PM2**
- Reverse proxied by **Nginx** on port 80
- Protected with a static **Elastic IP**
- Auto-deploying via **GitHub Actions CI/CD**

**Next**: [Setup Amazon RDS & S3 →](../5.4-RDS-S3/)
