---
title: "Worklog Tuần 3"
date: 2026-07-05
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:
* Phân tích và xây dựng thuật toán tính khoảng cách Haversine và logic trọng số **"Nam rước Nữ"** để đề xuất rạp xem phim CGV gần nhất.
* Triển khai xác thực người dùng bằng NextAuth.js kết hợp Google OAuth 2.0.
* Tham dự hội thảo **"Swinburne Cloud Mastery"** trực tiếp tại văn phòng AWS và review kiến trúc dự án với Mentor.

### Các công việc triển khai trong tuần này:
| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 30/06/2026 | - Lập trình công thức toán học Haversine bằng JavaScript để tính khoảng cách km chính xác giữa tọa độ GPS người dùng và các rạp CGV.<br>- Phát triển thuật toán trọng số "Nam rước Nữ": `avgLat = lat_nu * 0.8 + lat_nam * 0.2`, ưu tiên vị trí rạp gần nhà bạn Nữ hơn (trọng số 80%). | 30/06/2026 | 30/06/2026 | Tài liệu Toán học Haversine & Geolocation |
| 02/07/2026 | - Triển khai NextAuth.js Google OAuth 2.0 provider vào ứng dụng Next.js 16.<br>- Viết script migration khởi tạo bảng `USER` trong CSDL MySQL để lưu trữ thông tin và tọa độ vị trí. | 02/07/2026 | 02/07/2026 | [NextAuth.js Documentation](https://next-auth.js.org/) |
| 04/07/2026 | - **Lên công ty (On-site 🏢)**: Tham dự hội thảo "Swinburne Cloud Mastery" tại văn phòng AWS.<br>- Họp trực tiếp với Mentor để review bản vẽ kiến trúc đám mây LifeSync AI Calendar và nhận góp ý tối ưu. | 04/07/2026 | 04/07/2026 | Tài liệu Hội thảo AWS Office |

### Kết quả đạt được tuần 3:
* Hoàn thành engine đề xuất vị trí rạp CGV thông minh cho cặp đôi dựa trên tọa độ địa lý.
* Thiết lập thành công luồng đăng nhập bằng tài khoản Google.
* Tiếp thu kiến thức từ hội thảo AWS và hoàn thiện bản vẽ kiến trúc hệ thống.
