---
title: "Worklog Tuần 7"
date: 2026-07-29
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:
* Viết AWS Lambda crawler cào phim CGV và cấu hình lịch chạy tự động Amazon EventBridge hàng tuần.
* Tích hợp **Google Gemini 2.5 Flash** làm Dual-AI Engine dự phòng cho Bedrock nhằm đảm bảo hệ thống sẵn sàng cao.
* Rà soát bảo mật tổng thể toàn bộ tài nguyên AWS (AWS WAF, IAM Roles, S3 Bucket Policies, RDS Security Groups) và hoàn thiện sơ đồ kiến trúc hệ thống.

### Các công việc triển khai trong tuần này:
| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 27/07/2026 | - Viết hàm AWS Lambda (`cgv-movie-crawler`) chạy Node.js 20.x bóc tách dữ liệu lịch chiếu phim CGV và cập nhật trực tiếp vào Amazon RDS MySQL.<br>- Tạo Amazon EventBridge Schedule (`cgv-weekly-crawler`) với cú pháp `cron(0 17 ? * SUN *)` tự động kích hoạt lúc 00:00 AM sáng Thứ Hai hàng tuần giờ VN (UTC+7). | 27/07/2026 | 27/07/2026 | Tài liệu AWS Lambda & EventBridge |
| 28/07/2026 | - Thiết lập môi trường phát triển đám mây AWS Cloud9 & AWS CloudShell cho nhóm.<br>- Rà soát bảo mật tổng thể (AWS WAF Core Rules, hạn chót S3 Presigned URL, RDS Security Groups). | 28/07/2026 | 28/07/2026 | Tài liệu AWS Security Best Practices |
| 29/07/2026 | - ⚠️ **SỰ CỐ API BEDROCK & BỔ SUNG GEMINI**: Nâng cấp hệ thống phân tích ngôn ngữ tự nhiên lên mô hình **Dual-AI Engine**, bổ sung **Google Gemini 2.5 Flash** làm engine dự phòng có độ sẵn sàng cao, tự động chuyển đổi khi Bedrock gặp sự cố.<br>- Chuẩn hóa và hoàn thiện sơ đồ kiến trúc hệ thống sản xuất hoàn chỉnh trên AWS. | 29/07/2026 | 29/07/2026 | Tài liệu API Google Gemini & Architecture |

### Sơ đồ Kiến trúc Hệ thống Sản xuất:

![Sơ đồ Kiến trúc Hệ thống AWS LifeSync AI Calendar](/images/architecture.png)

### Kết quả đạt được tuần 7:
* Tự động hóa hoàn toàn quy trình cập nhật dữ liệu phim CGV hàng tuần.
* Làm chủ kiến trúc Dual-AI Engine đa tầng với cơ chế fallback tự động sang Google Gemini 2.5 Flash.
* Chuẩn hóa môi trường phát triển và đảm bảo tính tuân thủ bảo mật tuyệt đối cho hạ tầng cloud.
