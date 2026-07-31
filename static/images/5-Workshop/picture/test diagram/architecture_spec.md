# AWS ARCHITECTURE SPECIFICATION

## 1. System Overview & Tech Stack Scan

### 1.1 System Overview
**LifeSync AI Calendar** (tên dự án mã nguồn: `ai_calendar_fcaj`) là ứng dụng quản lý lịch trình cá nhân và nhóm thông minh tích hợp Trí tuệ nhân tạo (AI). Hệ thống cho phép người dùng lập kế hoạch công việc, phân tích mệnh/năng lượng cá nhân, bình chọn thời gian họp nhóm, đính kèm tệp tin và tự động gửi email nhắc nhở lịch trình hàng ngày. 

### 1.2 Tech Stack Scan (Kết quả phân tích từ Source Code)
- **Frontend Framework**: Next.js 16.2 (App Router) + React 19.
- **Backend Framework**: Next.js Serverless API Routes (`/api/auth/*`, `/api/event/*`, `/api/ai/chat/*`, `/api/upload/*`).
- **Database Engine**: Amazon RDS MySQL 8.0 (Driver: `mysql2/promise` kết nối bất đồng bộ lazy-loaded pool).
- **Authentication & Authorization**: Custom JWT (`jsonwebtoken`) lưu trong HTTP-Only Secure Cookies, tích hợp Google OAuth 2.0 (Google Identity Services).
- **Storage System**: Amazon S3 (AWS SDK v3 `@aws-sdk/client-s3` & `@aws-sdk/s3-request-presigner`) sinh Presigned Upload URL trực tiếp.
- **Secret & Configuration Vault**: AWS Secrets Manager (`@aws-sdk/client-secrets-manager`) kết hợp nạp biến môi trường động (`.env.production`).
- **AI / LLM Integration**: Dual AI Engine - **AWS Bedrock (Claude 3 Haiku)** làm bộ não chính + **Google Gemini API (`gemini-2.5-flash`)** làm bộ não dự phòng tự động (Fallback).
- **Email Notification System**: Dual Email Engine - **Amazon SES (SMTP)** làm kênh chính + **Google SMTP (Gmail App Password)** làm kênh dự phòng.
- **Asynchronous Task & Cron Engine**: AWS Lambda (Node.js 20.x runtime) + Amazon EventBridge Scheduler (chạy tự động lúc 07:00 AM UTC+7).

---

## 2. Required AWS Services Breakdown

### Layer 1: Edge, CDN & Security
- **Amazon Route 53**: Quản lý tên miền (DNS), điều hướng truy cập toàn cầu và kiểm tra mức độ hoạt động (Health Checks).
- **Amazon CloudFront**: Mạng lưới phân phối nội dung (CDN) giúp tối ưu tốc độ tải các file tĩnh (`/_next/static/*`) và phân phối ảnh avatar/file từ S3 tới người dùng với độ trễ thấp.
- **AWS WAF (Web Application Firewall)**: Chống tấn công lớp ứng dụng (Layer 7), bao gồm chống SQL Injection, XSS, Botnet và giới hạn số lượng request (Rate Limiting).

### Layer 2: Ingress & Compute
- **AWS Amplify Hosting**: Môi trường lưu trữ và thực thi các trang SSR (Server-Side Rendering) và Next.js API Routes.
- **AWS Lambda**: Máy chủ Serverless chạy độc lập xử lý công việc ngầm (Worker) quét database RDS và gửi mail báo lịch hàng ngày.

### Layer 3: Database & Caching
- **Amazon RDS MySQL 8.0**: Hệ quản trị cơ sở dữ liệu quan hệ chính (Multi-AZ Deployment để tăng tính sẵn sàng cao), lưu trữ các bảng `USER`, `EVENT`, `FRIENDSHIP`, `MEETING_REQUEST`, `SYSTEM_SETTING`.

### Layer 4: Storage & Files
- **Amazon S3 (Simple Storage Service)**: Bucket chứa tệp tin `lifesync-calendar-storage` dùng để lưu ảnh đại diện (Avatars) và tài liệu đính kèm sự kiện. Cấu hình quyền riêng tư 100% kết hợp Origin Access Control (OAC) và Presigned URLs.

### Layer 5: Queue, Async & Cron
- **Amazon EventBridge Scheduler**: Bộ đếm thời gian dạng Cronjob kích hoạt tự động theo biểu thức `cron(0 7 * * ? *)` (7h00 sáng giờ Việt Nam) để gọi hàm Lambda.

### Layer 6: Security, Auth & Monitoring
- **AWS Secrets Manager**: Lưu trữ và mã hóa các thông tin nhạy cảm (`DB_PASSWORD`, `JWT_SECRET`, `GEMINI_API_KEY`) với khóa **AWS KMS**.
- **AWS IAM (Identity and Access Management)**: Cấp quyền truy cập tối thiểu (Principle of Least Privilege) cho Amplify, Lambda, S3 và SES.
- **Amazon CloudWatch**: Thu thập log ứng dụng (`/aws/amplify/*`, `/aws/lambda/*`) và thiết lập cảnh báo khi có lỗi 5xx hoặc tải CPU cao.

### Layer 7: External/Third-party Integrations & Failovers
- **AWS Bedrock (Claude 3 Haiku)**: Mô hình AI chính trên hạ tầng AWS dùng để bóc tách ngữ nghĩa lịch trình tiếng Việt.
- **Google Gemini API (`gemini-2.5-flash`)**: Mô hình AI dự phòng khi AWS Bedrock chạm hạn mức (Rate limit) hoặc gặp sự cố.
- **Amazon SES (Simple Email Service)**: Kênh gửi email chính để phát mã xác thực OTP và thông báo lịch.
- **Google SMTP (Gmail)**: Kênh gửi email dự phòng khi Amazon SES nằm trong Sandbox mode.

---

## 3. Data Flow Steps (Luồng xử lý 14 bước)

1. **User Request**: Người dùng nhập địa chỉ trang web hoặc thực hiện thao tác trên trình duyệt (`https://lifesync.com`).
2. **DNS Resolution**: Request được điều hướng qua **Amazon Route 53** để phân giải địa chỉ IP của CDN.
3. **Firewall Inspection**: Traffic đi qua **AWS WAF** để kiểm tra và loại bỏ các request độc hại (SQLi, XSS, DDoS).
4. **Edge Caching**: **Amazon CloudFront** kiểm tra cache; nếu là file tĩnh thì trả về ngay, nếu là API/SSR thì đẩy tiếp vào Compute.
5. **App Rendering / API**: Request được xử lý bởi **AWS Amplify Hosting (Next.js Serverless API)**.
6. **Fetch Secrets**: Ứng dụng nạp an toàn các chuỗi kết nối và khóa bảo mật từ **AWS Secrets Manager** (hoặc `.env.production`).
7. **Database Query**: Next.js API gửi truy vấn SQL tới **Amazon RDS MySQL** (thông qua cổng 3306 nội bộ).
8. **Presigned URL Request**: Khi người dùng tải ảnh/file, API tạo **Presigned Upload URL** từ **Amazon S3** và trả về cho client.
9. **Direct Upload to S3**: Client sử dụng Presigned URL để tải trực tiếp file từ trình duyệt lên **Amazon S3 Bucket**.
10. **Primary AI Processing**: Lệnh trò chuyện/bóc tách lịch trình được gửi tới **AWS Bedrock (Claude 3 Haiku)**.
11. **Secondary AI Fallback**: Nếu AWS Bedrock phản hồi lỗi, hệ thống tự động chuyển hướng request tới **Google Gemini API**.
12. **Primary Email Sending**: Mã OTP xác thực được gửi thông qua **Amazon SES**.
13. **Secondary Email Fallback**: Nếu SES bị giới hạn Sandbox, hệ thống tự động fallback qua **Google SMTP (Gmail)**.
14. **Daily Cron Notification**: Đúng 07:00 AM, **Amazon EventBridge Scheduler** kích hoạt **AWS Lambda Worker** ➔ Lambda quét **RDS** ➔ Gửi mail tổng hợp lịch trình ngày mới cho người dùng.

---

## 4. Node Mapping for Python 'diagrams' Library

### 4.1 Nodes Table
| Tên hiển thị (Label) | AWS / External Service | Diagrams Module Path (Python) |
| :--- | :--- | :--- |
| User Browser | Client User | `diagrams.onprem.client.User` |
| Route 53 | Amazon Route 53 | `diagrams.aws.network.Route53` |
| AWS WAF | AWS WAF | `diagrams.aws.security.WAF` |
| CloudFront CDN | Amazon CloudFront | `diagrams.aws.network.CloudFront` |
| Amplify Hosting | AWS Amplify | `diagrams.aws.mobile.Amplify` |
| Secrets Manager | AWS Secrets Manager | `diagrams.aws.security.SecretsManager` |
| RDS MySQL | Amazon RDS | `diagrams.aws.database.RDS` |
| S3 Storage | Amazon S3 | `diagrams.aws.storage.S3` |
| AWS Bedrock | AWS Bedrock | `diagrams.aws.ml.Bedrock` |
| Gemini API | Google Gemini API | `diagrams.saas.chat.Slack` *(hoặc Custom/SaaS)* |
| Amazon SES | Amazon SES | `diagrams.aws.engagement.SimpleEmailServiceSes` |
| Google SMTP | Google Gmail SMTP | `diagrams.saas.chat.Slack` *(hoặc Custom/SaaS)* |
| EventBridge Scheduler | Amazon EventBridge | `diagrams.aws.integration.Eventbridge` |
| Lambda Daily Worker | AWS Lambda | `diagrams.aws.compute.Lambda` |
| CloudWatch Logs | Amazon CloudWatch | `diagrams.aws.management.Cloudwatch` |

### 4.2 Connections Table
| Node nguồn (Source) | Node đích (Target) | Label mũi tên (Luồng dữ liệu) | Kiểu nối |
| :--- | :--- | :--- | :--- |
| User Browser | Route 53 | 1. DNS Lookup | Solid |
| User Browser | AWS WAF | 2. HTTPS Request | Solid |
| AWS WAF | CloudFront CDN | 3. Clean Traffic | Solid |
| CloudFront CDN | Amplify Hosting | 4. Forward SSR & API | Solid |
| Amplify Hosting | Secrets Manager | 5. Fetch KMS Encrypted Secrets | Solid |
| Amplify Hosting | RDS MySQL | 6. SQL Queries (CRUD) | Solid |
| Amplify Hosting | S3 Storage | 7. Generate Presigned URL | Solid |
| User Browser | S3 Storage | 8. Direct File Upload (PUT) | Solid |
| Amplify Hosting | AWS Bedrock | 9a. Primary AI NLP Request | Solid |
| Amplify Hosting | Gemini API | 9b. Secondary AI Fallback | Dashed |
| Amplify Hosting | Amazon SES | 10a. Primary Email OTP | Solid |
| Amplify Hosting | Google SMTP | 10b. Secondary Email Fallback | Dashed |
| Google SMTP | User Browser | 11. Deliver Email to Inbox | Solid |
| EventBridge Scheduler | Lambda Daily Worker | 12. Daily Trigger (07:00 AM) | Solid |
| Lambda Daily Worker | RDS MySQL | 13. Query Today's Events | Solid |
| Lambda Daily Worker | Google SMTP | 14. Dispatch Daily Schedule Email | Solid |
| Amplify Hosting | CloudWatch Logs | System Server Logs | Dotted |
| Lambda Daily Worker | CloudWatch Logs | Worker Execution Logs | Dotted |
