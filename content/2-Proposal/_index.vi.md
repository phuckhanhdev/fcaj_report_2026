---
title: "Bản đề xuất"
date: 2026-07-31
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# LifeSync AI Calendar
## Hệ thống Lập lịch Thông minh Khoa học tích hợp AI trên Hạ tầng Đám mây AWS

---

### 1. Tóm tắt điều hành

**LifeSync AI Calendar** là một ứng dụng lập lịch thông minh toàn diện được xây dựng bằng **Next.js 16** và triển khai trên hạ tầng **Amazon Web Services (AWS)**. Nền tảng sử dụng **Google Gemini 2.5 Flash AI** để phân tích ý định lập lịch từ ngôn ngữ tự nhiên, **Thuật toán Haversine** tùy chỉnh để gợi ý rạp chiếu phim CGV gần nhất theo vị trí địa lý, cùng **Engine Lập lịch Khoa học** dựa trên thuật toán giải CSP (Constraint Satisfaction Problem) với tối ưu hóa Bitmask.

Hệ thống được triển khai trên nền tảng AWS production-grade gồm Amazon EC2 (t2.micro Free Tier), Amazon RDS MySQL, Amazon S3, Amazon CloudFront CDN, AWS WAF, AWS Lambda và Amazon EventBridge Scheduler — truy cập tại tên miền chính thức **[https://phuckhanh.id.vn](https://phuckhanh.id.vn)**.

<!-- Khung Nhúng Video Demo Hệ thống -->
<div align="center" style="margin: 25px 0;">
  <h4>📹 Video Demo Hệ thống LifeSync AI Calendar</h4>
  <iframe width="100%" height="450" style="max-width: 800px; border-radius: 8px; border: 1px solid #ddd;" src="LINK_VIDEO_DEMO_CỦA_BẠN" frameborder="0" allowfullscreen></iframe>
  <p><i>(Dán link nhúng video YouTube / Loom / MP4 của bạn vào thuộc tính src ở trên)</i></p>
</div>

---

### 2. Tuyên bố vấn đề

#### Vấn đề hiện tại
Các ứng dụng lịch truyền thống thiếu khả năng tự động hóa thông minh — người dùng phải tạo thủ công từng sự kiện mà không nhận được đề xuất lập lịch theo ngữ cảnh. Không có phương pháp khoa học nào để gợi ý khung giờ tối ưu dựa trên lịch hiện có của người dùng, khoa học năng suất (Pomodoro, giờ vàng), hay vị trí nhóm khi đi chơi.

#### Giải pháp
LifeSync AI Calendar giải quyết vấn đề trên bằng cách:
- Phân tích yêu cầu ngôn ngữ tự nhiên qua **Google Gemini AI** để trích xuất ý định lập lịch (học tập, thể dục, hẹn hò, v.v.)
- Áp dụng **Engine Lập lịch Khoa học** với 68 khung giờ (mỗi 15 phút) từ 06:00–23:00 dùng thuật toán CSP-Bitmask
- Gợi ý **Top 3 Rạp CGV gần nhất** bằng công thức Haversine với thuật toán đặc biệt **"Nam rước Nữ"** (trọng số 80% vị trí bạn Nữ, 20% bạn Nam cho cặp đôi)
- Tự động tạo sự kiện và chèn vào lịch cá nhân chỉ bằng 1 cú click

---

### 3. Kiến trúc đám mây AWS

#### Sơ đồ Kiến trúc Hệ thống (AWS Cloud Architecture)

![Sơ đồ Kiến trúc AWS LifeSync AI Calendar](/images/architecture.png)

#### Dịch vụ AWS sử dụng

| Dịch vụ | Vai trò |
|---|---|
| **Amazon EC2 (t2.micro)** | Máy chủ ứng dụng chạy Next.js 16 + PM2 + Nginx |
| **Amazon RDS MySQL** | CSDL đám mây cho người dùng, sự kiện và lịch sử chat |
| **Amazon S3** | Lưu trữ ảnh đại diện qua cơ chế Presigned URL |
| **Amazon CloudFront** | CDN toàn cầu để tăng tốc độ và che giấu IP EC2 |
| **AWS WAF** | Tường lửa ứng dụng web (Core Rules + bảo vệ SQL Injection) |
| **AWS Lambda** | Hàm serverless cào rạp CGV hàng tuần |
| **Amazon EventBridge** | Lịch Cron kích hoạt Lambda vào 00:00 mỗi Thứ Hai |
| **GitHub Actions CI/CD** | Pipeline tự động build & deploy khi `git push origin main` |

---

### 4. Triển khai kỹ thuật

#### Kiến trúc Engine Lập lịch AI
- **Strategy Pattern**: `StudyStrategy` (Pomodoro 50m/10m + Giờ vàng 08:00–11:00), `FitnessStrategy` (Buffer phục hồi 30m sau luyện tập), `DateStrategy` (Buffer di chuyển 30m — Ràng buộc cứng)
- **CSP Bitmask Solver**: 68 slot × 15 phút từ 06:00–23:00, chạy 100% JavaScript thuần
- **Phân tích ý định NLP**: Google Gemini 2.5 Flash với định dạng Tool Calling

#### Thuật toán Gợi ý Rạp CGV Khoa học
- **Công thức Haversine**: Tính khoảng cách km chính xác giữa 2 tọa độ GPS
- **Trọng số "Nam rước Nữ"**: Cặp đôi (1Nam+1Nữ): `avgLat = lat_nu × 0.8 + lat_nam × 0.2` — ưu tiên rạp gần nhà bạn Nữ hơn (trọng số 80%)
- **Trọng tâm nhóm (Group Centroid)**: Từ 3+ người hoặc cùng giới — lấy trung bình cộng chuẩn

#### Các tính năng nổi bật
- Hệ thống màu Avatar theo Cung Hoàng Đạo (12 cung × hash cố định theo User_ID)
- Lịch sử chat AI tự động dọn sạch sau 3 ngày
- Mời bạn bè theo thời gian thực & lập lịch nhóm với bỏ phiếu
- Tích hợp Google Maps chỉ đường trực tiếp tới rạp CGV

---

### 5. Lộ trình & Mốc triển khai

| Giai đoạn | Thời gian | Hoạt động |
|---|---|---|
| **Giai đoạn 1** | Tháng 1 | Thiết kế kiến trúc, cài đặt AWS (EC2, RDS, S3), dựng khung Next.js |
| **Giai đoạn 2** | Tháng 2 | Tính năng cốt lõi (xác thực, lịch, engine lập lịch), tích hợp AI |
| **Giai đoạn 3** | Tháng 3 | Triển khai CloudFront + WAF, tính năng CGV, kiểm thử production |
| **Sau ra mắt** | Liên tục | Tự động hóa CI/CD, giám sát, phát triển tính năng mới |

---

### 6. Ước tính ngân sách & Chi phí thực tế

#### Kịch bản 1: Có AWS Credits & Free Tier (Thực tế thời gian thực tập)
| Dịch vụ AWS | Chi phí Free Tier / Credit |
|---|---|
| **Amazon EC2 t2.micro** (Free Tier 750h/tháng + 20GB EBS) | $0,00/tháng |
| **Amazon RDS db.t3.micro** (Free Tier 750h/tháng + 20GB SSD) | $0,00/tháng |
| **Amazon S3 Standard** (< 5GB Free Tier + Presigned URLs) | $0,00/tháng |
| **Amazon CloudFront** (1TB Free Tier Data Transfer) | ~$0,01/tháng |
| **AWS WAF** ($5 Web ACL + $2 Managed Rule Sets) | ~$7,00/tháng *(Chi trả từ AWS Credits)* |
| **AWS Lambda & EventBridge** (< 1M request Free Tier) | $0,00/tháng |
| **Tổng chi trả thực tế túi cá nhân**: | **$0,00 / tháng** |

#### Kịch bản 2: Chi phí thực tế Thương mại (KHÔNG có AWS Credits & KHÔNG có Free Tier)
| Dịch vụ AWS | Cấu hình On-Demand | Chi phí ($/tháng) | Quy đổi (VNĐ/tháng) |
|---|---|---|---|
| **Amazon EC2** | `t3.micro` (730 giờ) + 20GB EBS gp3 SSD | **$10,07** | ~251.750 VNĐ |
| **Amazon RDS** | MySQL `db.t3.micro` Single-AZ + 20GB gp3 | **$14,71** | ~367.750 VNĐ |
| **AWS WAF** | 1 Web ACL ($5) + 2 Rule Sets ($2) + Traffic | **$7,60** | ~190.000 VNĐ |
| **Amazon CloudFront** | CDN Data Transfer Out (10GB) + HTTPS requests | **$0,95** | ~23.750 VNĐ |
| **Amazon S3** | Standard Storage (5GB) + PUT/GET Presigned URLs | **$0,19** | ~4.750 VNĐ |
| **AWS Lambda & EventBridge** | `cgv-movie-crawler` cron job hàng tuần | **$0,20** | ~5.000 VNĐ |
| **API AI Engine** | Google Gemini 2.5 Flash / Amazon Bedrock | **$1,00** | ~25.000 VNĐ |
| **Tên miền & SSL** | Tên miền `phuckhanh.id.vn` + Let's Encrypt SSL | **$0,40** | ~10.000 VNĐ |
| **TỔNG CHI PHÍ THỰC TẾ HÀNG THÁNG** | **Duy trì hệ thống Production 24/7** | **~$35,12 / tháng** | **~878.000 VNĐ / tháng** |

---

### 7. Đánh giá rủi ro

| Rủi ro | Mức ảnh hưởng | Xác suất | Giải pháp |
|---|---|---|---|
| EC2 instance gián đoạn | Cao | Thấp | PM2 tự khởi động lại + Elastic IP cố định |
| Giới hạn tần suất API AI | Trung bình | Trung bình | Fallback AWS Bedrock Claude |
| Mất kết nối CSDL | Cao | Thấp | Connection pooling + retry logic |
| Vượt ngân sách | Trung bình | Thấp | AWS Budget Alerts + giám sát Free Tier |

---

### 8. Kết quả kỳ vọng

#### Thành tựu kỹ thuật
- Hạ tầng AWS cloud production-grade phục vụ người dùng thực 24/7
- Đề xuất lập lịch AI dưới 1 giây qua Google Gemini 2.5 Flash
- Tối ưu hóa địa lý toán học cho buổi đi xem phim nhóm
- Bảo mật cấp doanh nghiệp: SSL/TLS 1.3 + AWS WAF đa tầng

#### Giá trị dài hạn
- Bản thiết kế kiến trúc AWS có thể tái sử dụng cho các dự án tương lai
- Thể hiện năng lực triển khai full-stack trên nền tảng đám mây AWS
- Ứng dụng thực tế của AI/NLP vào bài toán lập lịch trong cuộc sống