---
title: "Worklog Tuần 1"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---


### Mục tiêu tuần 1:

* Nhận AWS credits và mở khóa toàn bộ credits được cấp.
* Thực hành và làm quen với một số dịch vụ AWS cốt lõi (EC2, Bedrock Playground, AWS Budgets, Lambda, RDS).
* Học cách deploy trang web, vẽ kiến trúc hệ thống và thiết lập mạng VPC trên AWS.
* Thực hành tải dữ liệu lên cloud và tương tác với database thông qua AWS CLI.
* Phối hợp lập kế hoạch và phân công công việc chi tiết cho tuần tiếp theo với đồng đội Tiến Kha.
* Xử lý sự cố phát sinh trên tài khoản AWS.

### Các công việc cần triển khai trong tuần này:
| Ngày | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 15/06/2026 | - Mở khóa toàn bộ credits của AWS. <br> - Tìm hiểu cách sử dụng và thực hành các dịch vụ AWS:<br>&emsp; + Launch EC2 Instance (Khởi tạo máy chủ ảo EC2)<br>&emsp; + Experience AI/ML with foundation models in Amazon Bedrock Playground (Trải nghiệm AI/ML với các mô hình nền tảng trong Amazon Bedrock Playground)<br>&emsp; + Set up monitoring and alerts for costs - Set up AWS Budgets (Thiết lập theo dõi và cảnh báo chi phí bằng AWS Budgets)<br>&emsp; + Build a serverless web application by Lambda Web App (Xây dựng ứng dụng web serverless với Lambda Web App)<br>&emsp; + Set up managed relational database - RDS Database (Thiết lập cơ sở dữ liệu quan hệ được quản lý - RDS Database) | 15/06/2026 | 15/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 16/06/2026 | - Hẹn lịch họp với teammate Tiến Kha để lên kế hoạch làm việc chi tiết và phân chia công việc cho Tuần 2.<br>- Học cách deploy trang web bằng các dịch vụ của AWS.<br>- Học vẽ sơ đồ kiến trúc AWS trên draw.io qua các video hướng dẫn trên YouTube.<br>- Tìm hiểu cấu hình AWS Virtual Private Cloud (VPC) trên kênh YouTube [AWS Study Group](https://www.youtube.com/@AWSStudyGroup). | 16/06/2026 | 16/06/2026 | Các video hướng dẫn YouTube, [Kênh AWS Study Group](https://www.youtube.com/@AWSStudyGroup) |
| 18/06/2026 | - Tìm hiểu cách đưa dữ liệu (load data) lên AWS Cloud.<br>- Chạy thử nghiệm website tĩnh và kiểm thử các thao tác CRUD cơ bản của database (GET, POST, PUT) hoàn toàn qua giao diện dòng lệnh CLI. | 18/06/2026 | 18/06/2026 | Tài liệu AWS CLI |

### Kết quả đạt được tuần 1:

* Đã mở khóa thành công toàn bộ credits của AWS được cấp cho chương trình học tập.
* Đã tìm hiểu và thực hành thành công các nội dung cốt lõi:
  * **Launch EC2 Instance:** Khởi tạo thành công máy chủ ảo EC2, cấu hình Security Group và kết nối thành công qua SSH.
  * **Experience AI/ML Bedrock:** Trải nghiệm sử dụng các mô hình nền tảng (Foundation Models) như Claude, Llama trên Amazon Bedrock Playground.
  * **AWS Budgets:** Thiết lập thành công các ngưỡng cảnh báo chi phí sử dụng AWS để tránh phát sinh chi phí ngoài ý muốn.
  * **Lambda Web App:** Xây dựng ứng dụng web Serverless cơ bản sử dụng AWS Lambda kết hợp API Gateway.
  * **RDS Database:** Thiết lập cơ sở dữ liệu quan hệ được quản lý hoàn toàn bằng Amazon RDS (MySQL/PostgreSQL).
* **Họp và lập kế hoạch:** Lên lịch làm việc và phân chia vai trò cụ thể với teammate Tiến Kha để chuẩn bị cho Tuần 2.
* **Deploy Website & Vẽ kiến trúc:** Tìm hiểu các phương thức triển khai website trên AWS và thành thạo cách vẽ sơ đồ kiến trúc hệ thống AWS bằng công cụ draw.io.
* **Cấu hình VPC:** Tiếp thu kiến thức về thiết lập và cấu hình mạng VPC (Virtual Private Cloud) trên AWS thông qua các bài học của AWS Study Group.
* **Tải dữ liệu & Kiểm thử CLI:** Tải thành công dữ liệu lên cloud, thực hiện kiểm thử website tĩnh cùng các truy vấn API database (GET, POST, PUT) bằng CLI.

### Sự cố gặp phải:
* **Mô tả:** Trong quá trình tự tìm hiểu và thực hành trên tài khoản AWS, tôi đã vô tình thực hiện thao tác tạo mới một tổ chức (AWS Organization). Hành động này đã kích hoạt việc chuyển đổi tài khoản từ gói miễn phí (Free Tier) sang tài khoản thanh toán thông thường (Paid Plan).
* **Cách xử lý:** Tôi đã tạo ngay một phiếu hỗ trợ (Support Case) gửi đến trung tâm hỗ trợ của AWS (AWS Support Center) để giải thích sự cố vô ý này và đang chờ AWS phản hồi, trợ giúp đưa tài khoản trở lại trạng thái cũ hoặc miễn trừ các chi phí phát sinh nếu có.
