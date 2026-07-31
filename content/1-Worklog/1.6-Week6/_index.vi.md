---
title: "Worklog Tuần 6"
date: 2026-07-26
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:
* Triển khai Amazon CloudFront CDN để tăng tốc độ tải trang toàn cầu và ẩn IP tĩnh máy chủ EC2.
* Cấu hình tường lửa ứng dụng web AWS WAF (Web ACL `LifeSync-WAF`) bảo vệ ứng dụng trước các tấn công OWASP Top 10 và SQL Injection.
* Tham dự sự kiện **"FCAJ: Agentic AI Build Week"** trực tiếp tại văn phòng AWS và thuyết trình dự án.

### Các công việc triển khai trong tuần này:
| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 21/07/2026 | - Khởi tạo Amazon CloudFront CDN distribution (`dbpvljmyvgnai.cloudfront.net`) trỏ về tên miền `phuckhanh.id.vn`.<br>- Cấu hình chính sách tự động chuyển hướng HTTP sang HTTPS.<br>- Bật đầy đủ các phương thức HTTP `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`. | 21/07/2026 | 21/07/2026 | Tài liệu Hướng dẫn AWS CloudFront |
| 23/07/2026 | - Tạo Web ACL `LifeSync-WAF` gắn trực tiếp vào CloudFront distribution.<br>- Tích hợp bộ quy tắc AWS Managed Rules: `AWSManagedRulesCommonRuleSet` (OWASP) và `AWSManagedRulesSQLiRuleSet` (bảo vệ CSDL RDS). | 23/07/2026 | 23/07/2026 | Tài liệu Hướng dẫn AWS WAF |
| 25/07/2026 | - **Lên công ty (On-site 🏢)**: Tham dự sự kiện "FCAJ: Agentic AI Build Week" tại văn phòng AWS.<br>- Thuyết trình demo kiến trúc giải pháp LifeSync AI Calendar và trao đổi với các Solution Architect cùng các đội thi hackathon. | 25/07/2026 | 25/07/2026 | Tài liệu Sự kiện FCAJ |

### Kết quả đạt được tuần 6:
* Phân phối ứng dụng qua mạng CDN toàn cầu thành công và che giấu IP EC2 an toàn.
* Tích hợp tường lửa WAF bảo vệ ứng dụng ở tầng ứng dụng (Layer 7).
* Thuyết trình demo giải pháp ấn tượng tại sự kiện Build Week ở văn phòng AWS.
