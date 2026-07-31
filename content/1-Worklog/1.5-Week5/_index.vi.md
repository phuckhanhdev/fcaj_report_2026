---
title: "Worklog Tuần 5"
date: 2026-07-19
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:
* Khởi tạo Amazon S3 bucket phục vụ lưu trữ ảnh đại diện (avatar) của người dùng.
* Khắc phục sự cố tài khoản AWS chính bị lỗi/khóa và hoàn tất di chuyển hạ tầng sang tài khoản AWS dự phòng.
* Triển khai cơ chế upload ảnh trực tiếp lên S3 qua Presigned URL không thông qua server EC2.

### Các công việc triển khai trong tuần này:
| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 13/07/2026 | - Khởi tạo Amazon S3 bucket (`lifesync-avatar-bucket`) tại region `ap-southeast-2`.<br>- Cấu hình CORS policy cho phép các phương thức `PUT`, `GET` từ tên miền `https://phuckhanh.id.vn`. | 13/07/2026 | 13/07/2026 | Tài liệu Hướng dẫn AWS S3 |
| 15/07/2026 | - ⚠️ **SỰ CỐ TÀI KHOẢN AWS & CHUYỂN DỊCH**: Tài khoản AWS chính gặp sự cố bị khóa do liên quan đến AWS Organization.<br>- Nhanh chóng kích hoạt tài khoản AWS dự phòng thứ 2.<br>- Khôi phục CSDL RDS MySQL, cấu hình máy chủ EC2 và tạo lại S3 bucket trên tài khoản mới để đảm bảo dự án không bị gián đoạn. | 15/07/2026 | 15/07/2026 | Quy trình Sao lưu & Khôi phục AWS |
| 18/07/2026 | - Xây dựng API Route `/api/upload/presign` trong Next.js để cấp Presigned URL có thời hạn 60 giây.<br>- Tích hợp giao diện Frontend cho phép người dùng upload ảnh đại diện trực tiếp lên S3 không tốn băng thông EC2. | 18/07/2026 | 18/07/2026 | Tài liệu AWS SDK v3 S3 Presigned URL |

### Kết quả đạt được tuần 5:
* Xử lý thành công sự cố tài khoản AWS, đảm bảo hệ thống khôi phục nhanh chóng và không mất mát dữ liệu.
* Xây dựng xong hạ tầng lưu trữ S3 chuẩn hóa.
* Tối ưu hóa hiệu năng upload tệp avatar 0đ qua cơ chế Presigned URL.
