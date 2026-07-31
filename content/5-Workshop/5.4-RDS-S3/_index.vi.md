---
title: "Cài đặt Amazon RDS & S3"
date: 2026-07-31
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

## Cài đặt Amazon RDS & Amazon S3

Trong phần này, bạn sẽ cài đặt **Amazon RDS MySQL** làm CSDL ứng dụng và **Amazon S3** để lưu trữ ảnh đại diện người dùng.

---

## Phần A: Amazon RDS MySQL

Amazon RDS (Relational Database Service) cung cấp CSDL MySQL 8.0 được quản lý sẵn cho LifeSync AI Calendar. Nó lưu trữ tất cả tài khoản người dùng, sự kiện lịch, lịch sử chat AI và dữ liệu lịch chiếu phim CGV.

### Bước 1: Tạo RDS MySQL Instance

1. Vào **AWS Console** → Tìm **RDS** → Click **Create database**

2. Cấu hình:
   - **Choose a database creation method**: Standard create
   - **Engine type**: MySQL
   - **Engine Version**: MySQL 8.0.x
   - **Templates**: Free tier
   - **DB instance identifier**: `lifesync-calendar`
   - **Master username**: `admin`
   - **Master password**: Tạo mật khẩu mạnh và lưu an toàn

3. **DB Instance Class**: `db.t2.micro` (Free Tier)

4. **Storage**: 20 GiB gp2 (Free Tier), tắt auto-scaling

### Bước 2: Cấu hình kết nối

5. **VPC**: Default VPC
6. **Public access**: **Yes** (cần thiết để EC2 kết nối qua hostname endpoint)
7. **VPC Security group**: Create new
   - Tên security group: `lifesync-rds-sg`

8. **Additional configuration** → **Initial database name**: `lifesync_db`

9. Click **Create database** → Chờ 5–10 phút để instance sẵn sàng

### Bước 3: Cấu hình Security Group RDS

10. Vào security group `lifesync-rds-sg` → **Inbound rules** → **Edit inbound rules**

11. Thêm rule:
    - **Type**: MySQL/Aurora
    - **Port**: 3306
    - **Source**: Custom → Chọn Security Group của EC2 instance (`LifeSync-Server`)

    > Điều này chỉ cho phép EC2 của bạn kết nối với CSDL — chặn mọi truy cập Internet công khai vào MySQL.

### Bước 4: Lấy Endpoint RDS

12. Quay lại RDS instance → Sao chép **Endpoint** (vd: `lifesync-calendar.xxxxxxxx.ap-southeast-2.rds.amazonaws.com`)

13. Cập nhật `.env.local` trên EC2:
    ```bash
    RDS_HOST=lifesync-calendar.xxxxxxxx.ap-southeast-2.rds.amazonaws.com
    RDS_USER=admin
    RDS_PASSWORD=<mật-khẩu-của-bạn>
    RDS_DATABASE=lifesync_db
    ```

### Bước 5: Chạy migration schema CSDL

14. SSH vào EC2 và chạy script migration:
    ```bash
    cd /home/ubuntu/ai_calendar_fcaj
    node src/database/migrate.js
    ```

    Tạo các bảng cốt lõi sau:
    - `USER`: `User_ID`, `Email`, `Name`, `Gender`, `Latitude`, `Longitude`, `Avatar_Url`, `Zodiac_Sign`
    - `EVENT`: `Event_ID`, `User_ID`, `Title`, `Start_Time`, `End_Time`, `Category`, `Color`
    - `AI_CHAT_HISTORY`: `Chat_ID`, `User_ID`, `Role`, `Content`, `Created_At`
    - `CGV_MOVIE`: `Movie_ID`, `Title`, `Duration_Minutes`, `Genre`, `Showtimes_Json`
    - `FRIEND_INVITE`: `Invite_ID`, `From_User_ID`, `To_User_ID`, `Status`

---

## Phần B: Amazon S3

Amazon S3 lưu trữ file ảnh đại diện người dùng. Ứng dụng dùng **Presigned URL** để cho phép trình duyệt upload trực tiếp lên S3 mà không qua máy chủ EC2.

### Bước 1: Tạo S3 Bucket

1. Vào **AWS Console** → Tìm **S3** → Click **Create bucket**

2. Cấu hình:
   - **Bucket name**: `lifesync-avatar-bucket`
   - **AWS Region**: `ap-southeast-2`
   - **Block all public access**: **Bỏ chọn** "Block all public access" → Xác nhận

3. Click **Create bucket**

### Bước 2: Cấu hình CORS Policy

4. Vào bucket → Tab **Permissions** → **Cross-origin resource sharing (CORS)**

5. Click **Edit** và dán:
   ```json
   [
     {
       "AllowedHeaders": ["*"],
       "AllowedMethods": ["PUT", "GET"],
       "AllowedOrigins": ["https://phuckhanh.id.vn", "http://localhost:3000"],
       "ExposeHeaders": ["ETag"]
     }
   ]
   ```

6. Click **Save changes**

### Bước 3: Cấu hình Bucket Policy (Public Read cho Avatar)

7. Vẫn trong tab **Permissions** → **Bucket policy** → **Edit**:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::lifesync-avatar-bucket/*"
       }
     ]
   }
   ```

8. Click **Save changes**

### Bước 4: Cách Presigned URL Upload hoạt động

Luồng upload ảnh đại diện:
1. Trình duyệt gọi `/api/upload/presign` (API Route Next.js trên EC2)
2. EC2 tạo **Presigned URL** có hiệu lực 60 giây bằng thông tin IAM user
3. Trình duyệt upload file **trực tiếp lên S3** qua Presigned URL (dữ liệu không qua EC2)
4. URL công khai S3 được lưu vào `USER.Avatar_Url` trong RDS MySQL

---

### ✅ Hoàn thành cài đặt RDS & S3

- **Amazon RDS MySQL** đang chạy tại endpoint `lifesync-calendar.xxxxxxxx.ap-southeast-2.rds.amazonaws.com`
- Bucket **Amazon S3** `lifesync-avatar-bucket` sẵn sàng với CORS và quyền đọc công khai cho avatar
- Migration schema đã tạo đủ các bảng CSDL cần thiết

**Tiếp theo**: [Cài đặt Amazon CloudFront →](../5.5-CloudFront/)
