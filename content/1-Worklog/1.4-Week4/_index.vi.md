---
title: "Worklog Tuần 4"
date: 2026-07-12
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:
* Lập trình các thuật toán lập lịch theo Strategy Pattern (`StudyStrategy`, `FitnessStrategy`, `DateStrategy`).
* Khởi tạo máy chủ Amazon EC2 production, gán Elastic IP, cấu hình 2GB Swap memory, Nginx reverse proxy và PM2.
* Báo cáo tiến độ giữa kỳ trực tiếp tại văn phòng AWS với Mentor và cấu hình Security Group bảo mật.

### Các công việc triển khai trong tuần này:
| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 06/07/2026 | - Phát triển kiến trúc Strategy Pattern cho engine lập lịch:<br>&emsp; + `StudyStrategy`: Áp dụng Pomodoro 50m làm / 10m nghỉ, ưu tiên giờ vàng 08:00–11:00.<br>&emsp; + `FitnessStrategy`: Tự động chèn 30m nghỉ ngơi phục hồi sau tập luyện.<br>&emsp; + `DateStrategy`: Ràng buộc cứng 30m di chuyển giữa các địa điểm. | 06/07/2026 | 06/07/2026 | Tài liệu Design Patterns |
| 08/07/2026 | - **Lên công ty (On-site 🏢)**: Khởi tạo EC2 Ubuntu 24.04 LTS `t2.micro` (`LifeSync-Server`).<br>- Gán Elastic IP tĩnh `3.104.121.77`.<br>- Cấu hình 2GB Swap Memory chống quá tải RAM.<br>- Cấu hình Nginx reverse proxy điều hướng port 80 ➔ 3000 và PM2 quản lý tiến trình ứng dụng. | 08/07/2026 | 08/07/2026 | Tài liệu AWS EC2 & Nginx |
| 11/07/2026 | - **Lên công ty (On-site 🏢)**: Thuyết trình bản thử nghiệm giữa kỳ với Mentor.<br>- Siết chặt Security Group của CSDL RDS MySQL, chỉ cho phép duy nhất Security Group của EC2 truy cập qua port 3306. | 11/07/2026 | 11/07/2026 | Quy chuẩn Bảo mật AWS |

### Kết quả đạt được tuần 4:
* Hoàn thành các chiến lược lập lịch khoa học linh hoạt theo ngữ cảnh.
* Đưa máy chủ EC2 production vào vận hành 24/7 với Nginx và PM2.
* Thiết lập bảo mật đa tầng giữa EC2 và CSDL RDS MySQL thành công.
