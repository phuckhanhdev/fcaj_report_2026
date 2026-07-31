---
title: "Chuẩn bị"
date: 2026-07-31
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

## Chuẩn bị

Trước khi bắt đầu workshop, hãy đảm bảo bạn đã có đủ các yêu cầu sau:

### 1. Tài khoản AWS

- **Tài khoản AWS** đang hoạt động với đủ quyền (AdministratorAccess hoặc tối thiểu: quyền đầy đủ EC2, RDS, S3, CloudFront, WAF, Lambda, EventBridge, IAM)
- Khuyến nghị có **AWS Credits** — workshop sử dụng các dịch vụ có thể vượt Free Tier (ví dụ: AWS WAF ~$7/tháng)
- Region khuyến nghị: **ap-southeast-2 (Sydney)** — gần Việt Nam nhất, độ trễ thấp

### 2. Mã nguồn

- Fork hoặc clone repository LifeSync AI Calendar:
  ```bash
  git clone https://github.com/<your-username>/ai_calendar_fcaj.git
  ```
- Cần có **tài khoản GitHub** và **GitHub repository** để cấu hình GitHub Actions CI/CD

### 3. Công cụ cần có trên máy

| Công cụ | Phiên bản | Mục đích |
|---|---|---|
| **Node.js** | 20.x LTS | Runtime cho Next.js |
| **npm** | 10.x | Quản lý package |
| **Git** | Mới nhất | Quản lý phiên bản code |
| **SSH client** | Tích hợp sẵn (Mac/Linux) hoặc PuTTY (Windows) | Kết nối EC2 |
| **AWS CLI** | v2 (tùy chọn) | Quản lý AWS qua dòng lệnh |

### 4. Biến môi trường

Chuẩn bị các biến môi trường sau để cấu hình trong `.env.local` và GitHub Secrets:

| Biến | Mô tả |
|---|---|
| `DATABASE_URL` | Chuỗi kết nối MySQL từ endpoint RDS |
| `NEXTAUTH_SECRET` | Chuỗi ngẫu nhiên để mã hóa session NextAuth |
| `NEXTAUTH_URL` | URL production của bạn (vd: `https://phuckhanh.id.vn`) |
| `GOOGLE_AI_API_KEY` | API key Google Gemini từ Google AI Studio |
| `AWS_ACCESS_KEY_ID` | Access key IAM user cho S3 Presigned URL |
| `AWS_SECRET_ACCESS_KEY` | Secret key IAM user cho S3 Presigned URL |
| `AWS_REGION` | Region AWS (vd: `ap-southeast-2`) |
| `S3_BUCKET_NAME` | Tên S3 bucket lưu avatar |
| `RDS_HOST` | Hostname endpoint RDS MySQL |
| `RDS_USER` | Tên người dùng CSDL RDS |
| `RDS_PASSWORD` | Mật khẩu CSDL RDS |
| `RDS_DATABASE` | Tên database RDS |

### 5. IAM User cho ứng dụng

Tạo IAM user với **Programmatic Access** và gắn inline policy sau để sử dụng S3 Presigned URL:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::lifesync-avatar-bucket/*"
    }
  ]
}
```

### 6. Key Pair cho EC2

1. Vào **EC2 Console** → **Key Pairs** → **Create key pair**
2. Tên: `lifesync-key`
3. Định dạng: `.pem` (Mac/Linux) hoặc `.ppk` (Windows PuTTY)
4. Tải về và lưu trữ an toàn — **không thể tải lại sau khi đóng**
5. Đặt quyền đúng: `chmod 400 lifesync-key.pem`