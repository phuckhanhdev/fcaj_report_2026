---
title: "Worklog Tuần 7"
date: 2026-07-31
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:
* Viết AWS Lambda crawler cào phim CGV và cấu hình lịch chạy tự động Amazon EventBridge hàng tuần.
* Xử lý sự cố giới hạn API AWS Bedrock và tích hợp **Google Gemini 2.5 Flash** làm AI Engine dự phòng song song.
* Hoàn thành toàn bộ báo cáo Workshop 9 bước triển khai trên AWS đúng mốc 31/07/2026.

### Các công việc triển khai trong tuần này:
| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 27/07/2026 | - Viết hàm AWS Lambda (`cgv-movie-crawler`) chạy Node.js 20.x bóc tách dữ liệu lịch chiếu phim CGV và cập nhật trực tiếp vào Amazon RDS MySQL.<br>- Tạo Amazon EventBridge Schedule (`cgv-weekly-crawler`) với cú pháp `cron(0 17 ? * SUN *)` tự động kích hoạt lúc 00:00 AM sáng Thứ Hai hàng tuần giờ VN (UTC+7). | 27/07/2026 | 27/07/2026 | Tài liệu AWS Lambda & EventBridge |
| 29/07/2026 | - ⚠️ **SỰ CỐ API BEDROCK & BỔ SUNG GEMINI**: AWS Bedrock gặp sự cố quá giới hạn API/quota.<br>- Nâng cấp hệ thống phân tích ngôn ngữ tự nhiên lên mô hình **Dual-AI Engine**, bổ sung **Google Gemini 2.5 Flash** làm engine dự phòng có độ sẵn sàng cao, tự động chuyển đổi khi Bedrock gặp sự cố. | 29/07/2026 | 29/07/2026 | Tài liệu API Google Gemini |
| 31/07/2026 | - 🎉 **HOÀN THÀNH WORKSHOP AWS**: Biên soạn và hoàn tất cuốn báo cáo kỹ thuật Workshop triển khai sản phẩm 9 bước trên AWS (`docs/aws_full_production_deployment_report.md`) đúng tiến độ ngày 31/07/2026. | 31/07/2026 | 31/07/2026 | Tài liệu Báo cáo Kỹ thuật Workshop |

### Kết quả đạt được tuần 7:
* Tự động hóa hoàn toàn quy trình cập nhật dữ liệu phim CGV hàng tuần.
* Làm chủ kiến trúc Dual-AI Engine đa tầng với cơ chế fallback tự động sang Google Gemini 2.5 Flash.
* Hoàn thành cuốn báo cáo Workshop triển khai production chuẩn AWS đúng mốc 31/07/2026.
