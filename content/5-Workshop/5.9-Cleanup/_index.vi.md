---
title: "Dọn dẹp tài nguyên"
date: 2026-07-31
weight: 9
chapter: false
pre: " <b> 5.9. </b> "
---

## Dọn dẹp tài nguyên AWS

Sau khi hoàn thành workshop, bạn có thể muốn dọn dẹp tài nguyên để tránh phát sinh chi phí ngoài ý muốn. Làm theo hướng dẫn này để xóa an toàn tất cả tài nguyên AWS đã tạo trong workshop.

> **⚠️ Cảnh báo**: Xóa các tài nguyên này là **vĩnh viễn và không thể hoàn tác**. Chỉ tiến hành nếu bạn đã xong với hệ thống LifeSync AI Calendar và không cần dữ liệu nữa.

---

## Thứ tự dọn dẹp

**Quan trọng**: Xóa tài nguyên theo đúng thứ tự này để tránh lỗi phụ thuộc.

### 1. Amazon EventBridge Scheduler

1. Vào **EventBridge** → **Scheduler** → **Schedules**
2. Chọn `cgv-weekly-crawler` → Click **Delete** → Xác nhận

### 2. AWS Lambda Function

1. Vào **Lambda** → **Functions**
2. Chọn `cgv-movie-crawler` → Click **Actions** → **Delete** → Xác nhận

### 3. AWS WAF — Web ACL

1. Vào **WAF & Shield** → **Protection packs (web ACLs)**
2. Chuyển region sang **Global (CloudFront)**
3. Chọn `LifeSync-WAF` → Click **Delete** → Xác nhận

### 4. Amazon CloudFront Distribution

1. Vào **CloudFront** → **Distributions**
2. Chọn distribution → Click **Disable** trước → Chờ trạng thái thay đổi
3. Sau khi đã disable, chọn lại → Click **Delete** → Xác nhận

### 5. Amazon S3 Bucket

1. Vào **S3** → Click vào `lifesync-avatar-bucket`
2. Chọn tất cả object → **Delete** (làm trống bucket trước)
3. Quay lại → Chọn bucket → Click **Delete** → Nhập tên bucket → Xác nhận

### 6. Amazon RDS Instance

1. Vào **RDS** → **Databases**
2. Chọn `lifesync-calendar` → Click **Actions** → **Delete**
3. Bỏ chọn **Create final snapshot** (nếu không cần backup)
4. Nhập `delete me` → Click **Delete**

### 7. Amazon EC2 Instance & Elastic IP

1. **Elastic IP trước**: Vào **EC2** → **Elastic IPs**
   - Chọn Elastic IP → Click **Actions** → **Disassociate** → rồi **Release**
   
   > Elastic IP tính phí $0,005/giờ nếu được cấp phát nhưng KHÔNG gắn vào instance đang chạy. Hãy Release ngay.

2. **Terminate EC2**: Vào **EC2** → **Instances**
   - Chọn `LifeSync-Server` → Click **Instance state** → **Terminate instance** → Xác nhận

### 8. Security Groups

1. Vào **EC2** → **Security Groups**
2. Xóa `lifesync-rds-sg` và các security group của workshop
   - Lưu ý: Không thể xóa nếu đang được sử dụng bởi tài nguyên khác

### 9. IAM User (Tùy chọn)

1. Vào **IAM** → **Users**
2. Chọn IAM user đã tạo cho S3 Presigned URL
3. Click **Delete** → Xác nhận

---

## Chi phí sau dọn dẹp

Sau khi dọn dẹp xong, hóa đơn AWS hàng tháng của bạn sẽ về **$0,00** (giả sử không có tài nguyên AWS nào khác đang chạy trong tài khoản vượt Free Tier).

| Dịch vụ | Chi phí hàng tháng sau dọn dẹp |
|---|---|
| EC2 | $0,00 (đã terminate) |
| RDS | $0,00 (đã xóa) |
| S3 | $0,00 (đã xóa) |
| CloudFront | $0,00 (đã xóa) |
| WAF | $0,00 (đã xóa) |
| Lambda | $0,00 (đã xóa) |
| EventBridge | $0,00 (đã xóa) |

---

## Lưu lại trước khi xóa

Trước khi xóa, hãy lưu:
- File `.env.local` với tất cả giá trị cấu hình
- Backup CSDL: `mysqldump -h <RDS_HOST> -u admin -p lifesync_db > backup.sql`
- GitHub repository (code được bảo tồn dù dọn dẹp AWS)

---

### ✅ Hoàn thành Workshop

Chúc mừng! Bạn đã thành công:
1. ✅ Cài đặt máy chủ **Amazon EC2** production với Next.js 16, Nginx và PM2
2. ✅ Cấu hình **Amazon RDS MySQL** với security group và schema đúng
3. ✅ Tạo bucket **Amazon S3** với CORS và Presigned URL để upload avatar
4. ✅ Triển khai **Amazon CloudFront** CDN cho hiệu suất toàn cầu và che giấu IP
5. ✅ Bảo mật ứng dụng bằng **AWS WAF** (Core Rules + bảo vệ SQL Injection)
6. ✅ Tự động hóa cào phim CGV hàng tuần với **AWS Lambda + EventBridge**
7. ✅ Tích hợp dịch vụ ngoài AWS: tên miền, SSL, Google Gemini AI và NextAuth

**Đây là kiến trúc AWS production-grade hoàn chỉnh cho ứng dụng web AI full-stack!**
