---
title: "Nhật ký công việc"
date: 2026-07-31
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

# Nhật ký Công việc Thực tập (Worklog 8 Tuần)

Trong suốt **8 tuần thực tập** thuộc chương trình **First Cloud AI Journey (FCAJ 2026)** tại **AWS Việt Nam** (từ ngày **15/06/2026** đến ngày **31/07/2026**), tôi đã thực hiện nghiên cứu, thiết kế kiến trúc và triển khai sản xuất ứng dụng **LifeSync AI Calendar** — hệ thống lập lịch khoa học thông minh tích hợp AI.

Dưới đây là tóm tắt lộ trình công việc chi tiết theo từng tuần:

---

### 📅 Danh mục 8 Tuần Thực tập:

- **[Tuần 1 (15/06 – 21/06): On-boarding & Làm quen Dịch vụ AWS](1.1-Week1/)**  
  *On-site tại văn phòng AWS (15/06)*. Nhận bàn giao tài khoản AWS Credits, cài đặt môi trường phát triển và học các dịch vụ đám mây cốt lõi (IAM, EC2, S3, VPC, Lambda, RDS).

- **[Tuần 2 (22/06 – 28/06): Thảo luận Ý tưởng & Thiết kế CSDL MySQL](1.2-Week2/)**  
  *On-site tại văn phòng AWS (24/06)*. Thảo luận ý tưởng dự án Lịch AI với Tiến Kha, chạy thử nghiệm LocalStack và thiết kế schema CSDL quan hệ trên MySQL.

- **[Tuần 3 (29/06 – 05/07): Tham gia Swinburne Cloud Mastery & Thuật toán Địa lý Haversine](1.3-Week3/)**  
  *On-site tại văn phòng AWS (04/07)*. Tham dự sự kiện Swinburne Cloud Mastery, phát triển thuật toán Haversine với trọng số "Nam rước Nữ" (80% Nữ / 20% Nam) và tích hợp NextAuth.js Google OAuth 2.0.

- **[Tuần 4 (06/07 – 12/07): Cấu hình EC2, Elastic IP, Nginx & Strategy Pattern Scheduler](1.4-Week4/)**  
  *On-site tại văn phòng AWS (08/07 & 11/07)*. Khởi tạo máy chủ EC2 Ubuntu, gán Elastic IP `3.104.121.77`, cấu hình Nginx Reverse Proxy, PM2, phát triển các chiến lược lập lịch (`StudyStrategy`, `FitnessStrategy`, `DateStrategy`) và báo cáo Mid-term.

- **[Tuần 5 (13/07 – 19/07): Sự cố Tài khoản AWS & Triển khai RDS + S3 Presigned URLs](1.5-Week5/)**  
  *Sự cố ngày 15/07*: Khắc phục sự cố tài khoản AWS chính ➔ Chuyển đổi và khôi phục CSDL & mã nguồn sang tài khoản dự phòng. Cấu hình RDS MySQL và cơ chế upload ảnh avatar S3 qua Presigned URLs.

- **[Tuần 6 (20/07 – 26/07): Tham gia Hackathon AABW & Triển khai AWS WAF + CloudFront](1.6-Week6/)**  
  *On-site tại văn phòng AWS (25/07)*. Tham dự workshop AABW AWS AI Build Week, triển khai CloudFront CDN phân phối toàn cầu và thiết lập tường lửa AWS WAF (Core Rules + bảo vệ SQL Injection).

- **[Tuần 7 (27/07 – 29/07): Tích hợp Dual-AI Engine (Bedrock + Gemini), Lambda CGV & Kiểm thử Bảo mật](1.7-Week7/)**  
  Tích hợp **Google Gemini 2.5 Flash** làm Dual-AI Engine dự phòng cho Bedrock, triển khai AWS Lambda + EventBridge cào lịch chiếu CGV tự động, cấu hình AWS Cloud9/CloudShell và rà soát bảo mật tổng thể (WAF, RDS S3 policies).

- **[Tuần 8 (30/07 – 31/07): Tối ưu Hiệu năng Nginx, Xuất bản 4 Bài Blog Kỹ thuật & Hoàn tất Nộp Báo cáo](1.8-Week8/)**  
  Tối ưu hóa nén Gzip/Cache Nginx & Load testing (`ab`), hoàn thiện 4 bài blog kỹ thuật (Bedrock vs SageMaker, DevOps Agent, CloudWatch Alarms, Data Protection), tự đánh giá, góp ý FCAJ và **chính thức hoàn thành nộp báo cáo thực tập (31/07/2026)**.