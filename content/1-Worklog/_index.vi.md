---
title: "Nhật ký công việc"
date: 2026-07-31
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

# Nhật ký Công việc Thực tập (Worklog 12 Tuần)

Trong suốt **12 tuần thực tập** thuộc chương trình **First Cloud AI Journey (FCAJ 2026)** tại **AWS Việt Nam** (từ ngày **15/06/2026** đến ngày **15/08/2026**), tôi đã thực hiện nghiên cứu, thiết kế kiến trúc và triển khai sản xuất ứng dụng **LifeSync AI Calendar** — hệ thống lập lịch khoa học thông minh tích hợp AI.

Dưới đây là tóm tắt lộ trình công việc chi tiết theo từng tuần:

---

### 📅 Danh mục 12 Tuần Thực tập:

- **[Tuần 1 (15/06 – 21/06): On-boarding & Làm quen Dịch vụ AWS](1.1-Week1/)**  
  *On-site tại văn phòng AWS (15/06)*. Nhận bàn giao tài khoản AWS Credits, cài đặt môi trường phát triển và học các dịch vụ đám mây cốt lõi (IAM, EC2, S3, VPC).

- **[Tuần 2 (22/06 – 28/06): Thảo luận Kiến trúc & Thiết kế CSDL MySQL](1.2-Week2/)**  
  *On-site tại văn phòng AWS (24/06)*. Thảo luận kiến trúc dự án với Mentor Tiến Kha, chạy thử nghiệm LocalStack và thiết kế schema CSDL quan hệ trên MySQL.

- **[Tuần 3 (29/06 – 05/07): Tham gia Swinburne Cloud Mastery & Khởi tạo Next.js 16](1.3-Week3/)**  
  *On-site tại văn phòng AWS (04/07)*. Tham dự sự kiện Swinburne Cloud Mastery, khởi tạo cấu trúc dự án LifeSync AI Calendar bằng Next.js 16 và TailwindCSS.

- **[Tuần 4 (06/07 – 12/07): Cấu hình EC2, Elastic IP, Nginx & PM2](1.4-Week4/)**  
  *On-site tại văn phòng AWS (08/07 & 11/07)*. Khởi tạo máy chủ Ubuntu EC2, gán Elastic IP `3.104.121.77`, cấu hình Nginx Reverse Proxy, quản lý tiến trình bằng PM2 và trình bày báo cáo Mid-term.

- **[Tuần 5 (13/07 – 19/07): Sự cố Tài khoản AWS & Triển khai RDS + S3 Presigned URL](1.5-Week5/)**  
  *Sự cố ngày 15/07*: Xử lý sự cố khóa tài khoản AWS chính ➔ Chuyển đổi và khôi phục CSDL & mã nguồn sang tài khoản dự phòng. Cấu hình RDS MySQL và cơ chế upload ảnh avatar S3 qua Presigned URLs.

- **[Tuần 6 (20/07 – 26/07): Tham gia Hackathon AABW & Triển khai AWS WAF + CloudFront](1.6-Week6/)**  
  *On-site tại văn phòng AWS (25/07)*. Tham dự workshop AABW AWS AI Build Week, triển khai CloudFront CDN phân phối toàn cầu và thiết lập tường lửa AWS WAF (Core Rules + bảo vệ SQL Injection).

- **[Tuần 7 (27/07 – 02/08): Sự cố API Bedrock & Tích hợp Dual-AI Engine + Lambda CGV](1.7-Week7/)**  
  *Sự cố ngày 29/07*: Khắc phục lỗi Bedrock quota bằng cách tích hợp **Google Gemini 2.5 Flash** làm Dual-AI Engine dự phòng. Triển khai AWS Lambda + EventBridge cào lịch chiếu CGV hàng tuần và **hoàn thành Workshop (31/07)**.

- **[Tuần 8 (03/08 – 09/08): Tối ưu hóa Thuật toán Địa lý Haversine & Bitmask Scheduler](1.8-Week8/)**  
  Lập trình thuật toán Nam rước Nữ (trọng số 80% Nữ / 20% Nam khi gợi ý rạp CGV) và engine giải Constraint Satisfaction Problem (CSP) với bitmask 68 time slots × 15 phút.

- **[Tuần 9 (10/08 – 16/08): Tự động hóa CI/CD với GitHub Actions & Hoàn tất Thực tập](1.9-Week9/)**  
  Cấu hình pipeline GitHub Actions (`deploy.yml`) tự động build và deploy lên EC2 khi push code. Nghiệm thu hoàn thành chương trình thực tập (15/08/2026).

- **[Tuần 10 (17/08 – 23/08): Tối ưu hóa Giám sát CloudWatch Alarms & Data Protection](1.10-Week10/)**  
  Cấu hình CloudWatch Alarms theo mô hình 3-Right (Right Metric, Right Threshold, Right Action) và thiết lập chính sách che giấu dữ liệu nhạy cảm trong logs.

- **[Tuần 11 (24/08 – 30/08): Đóng gói Tài liệu Workshop & Tổng kết Bài viết Blog](1.11-Week11/)**  
  Biên soạn bộ tài liệu Workshop 9 bước triển khai hạ tầng production-grade AWS và hoàn thiện 4 bài blog kỹ thuật chuyên sâu.

- **[Tuần 12 (31/08 – 06/09): Tổng kết Đánh giá & Hoàn thiện Báo cáo Hugo Portfolio](1.12-Week12/)**  
  Hoàn thiện bảng tự đánh giá bản thân, đóng góp ý kiến cho chương trình FCAJ và xuất bản website báo cáo thực tập trên Hugo.