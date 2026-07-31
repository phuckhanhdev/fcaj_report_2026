---
title: "GenAI-powered App-DB Modernization Workshop"
date: 2026-06-27
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Báo cáo tóm tắt: “GenAI-powered App-DB Modernization Workshop”

### Mục tiêu sự kiện

- Chia sẻ các thực tiễn tốt nhất trong thiết kế ứng dụng hiện đại và hiện đại hóa hạ tầng đám mây
- Giới thiệu phương pháp Domain-Driven Design (DDD) và kiến trúc điều hướng theo sự kiện (Event-driven architecture)
- Phân tích và lựa chọn các dịch vụ tính toán phù hợp (EC2 vs Fargate vs Lambda)
- Giới thiệu công cụ AI Amazon Q Developer hỗ trợ toàn bộ vòng đời phát triển phần mềm

### Thông tin sự kiện

- **Thời gian:** 27/06/2026
- **Địa điểm:** Tầng 36, Văn phòng AWS Việt Nam, TP. Hồ Chí Minh
- **Vai trò:** Người tham dự (Attendee)

### Diễn giả

- **Jignesh Shah** – Giám đốc mảng Cơ sở dữ liệu Mã nguồn mở, AWS
- **Erica Liu** – Chuyên gia cao cấp GTM, AppMod AWS
- **Fabrianne Effendi** – Chuyên gia Kiến trúc Giải pháp Serverless, AWS

---

### Điểm nổi bật chính

#### 1. Chuyển đổi sang Microservices & Kiến trúc Event-Driven
- Chuyển đổi hệ thống Monolith thành các dịch vụ độc lập giao tiếp qua tin nhắn bất đồng bộ.
- 3 trụ cột cốt lõi: Quản lý hàng đợi (Queue), Chiến lược Cache và Xử lý tin nhắn (Pub/Sub, Point-to-point, Streaming).

#### 2. Thiết kế theo Domain (Domain-Driven Design - DDD)
- Áp dụng DDD xác định sự kiện nghiệp vụ (Domain events), vùng giới hạn (Bounded contexts) và ngôn ngữ chung giữa đội ngũ kinh doanh và kỹ thuật.

#### 3. Tiến trình Tính toán & Amazon Q Developer
- Lựa chọn giải pháp tính toán: từ EC2 ➔ ECS ➔ Fargate ➔ Lambda Serverless.
- Tự động hóa hiện đại hóa code và CSDL với sự trợ giúp của Amazon Q Developer.

---

### Bài học rút ra

- **Tư duy Business-First**: Luôn bắt đầu hiện đại hóa ứng dụng từ bài toán nghiệp vụ thay vì chạy theo công nghệ.
- **Tận dụng Serverless**: Giảm thiểu chi phí vận hành hạ tầng và tối ưu khả năng tự động mở rộng.

> Tổng kết: Workshop mang lại nhiều phương pháp luận thực chiến trong việc hiện đại hóa ứng dụng, cơ sở dữ liệu và quy trình phát triển trên AWS.
