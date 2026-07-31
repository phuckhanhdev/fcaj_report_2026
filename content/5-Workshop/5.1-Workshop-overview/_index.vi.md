---
title: "Tổng quan Workshop"
date: 2026-07-31
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

## LifeSync AI Calendar — Tổng quan Workshop

### Bạn sẽ xây dựng gì?

Sau khi hoàn thành workshop, bạn sẽ có một **hệ thống production đầy đủ trên AWS** phản ánh kiến trúc đang vận hành tại [https://phuckhanh.id.vn](https://phuckhanh.id.vn), bao gồm:

- Instance **Amazon EC2** chạy Next.js 16 với Nginx reverse proxy và PM2 process manager
- CSDL **Amazon RDS MySQL** lưu trữ tài khoản người dùng, sự kiện lịch và lịch sử chat AI
- Bucket **Amazon S3** lưu trữ ảnh đại diện người dùng qua Presigned URL
- Phân phối **Amazon CloudFront** CDN tăng tốc toàn cầu và che giấu IP EC2
- Tường lửa **AWS WAF** với Core Rules và bảo vệ SQL Injection
- Hàm **AWS Lambda** + **Amazon EventBridge** Scheduler để cào dữ liệu rạp CGV hàng tuần

### Công nghệ chính

| Công nghệ | Mục đích |
|---|---|
| **Next.js 16** | Framework React full-stack (App Router + Server Actions) |
| **PM2** | Quản lý tiến trình Node.js production (tự khởi động lại, ghi log) |
| **Nginx** | Reverse proxy hiệu suất cao điều hướng port 80/443 → 3000 |
| **Ubuntu 24.04 LTS** | Hệ điều hành Linux ổn định cho EC2 |
| **MySQL 8.0** | CSDL quan hệ production trên Amazon RDS |
| **Google Gemini 2.5 Flash** | Mô hình AI phân tích ý định lập lịch từ ngôn ngữ tự nhiên |
| **GitHub Actions** | Pipeline CI/CD tự động deploy mỗi khi `git push` |

### Phạm vi Workshop

Workshop chia thành **Dịch vụ AWS** (Mục 3–7) và **Dịch vụ khác** (Mục 8):

**Dịch vụ AWS được hướng dẫn chi tiết:**
- Amazon EC2 — Khởi tạo server, Security Group, Elastic IP, swap memory
- Amazon RDS — Cài đặt MySQL, Security Group, migration schema
- Amazon S3 — Tạo bucket, CORS policy, cơ chế Presigned URL
- Amazon CloudFront — Tạo distribution, cài đặt origin, cache behavior
- AWS WAF — Tạo Web ACL, chọn managed rules, gắn CloudFront
- AWS Lambda — Tạo hàm, biến môi trường, gói triển khai
- Amazon EventBridge — Lịch cron kích hoạt Lambda

**Dịch vụ khác (Mục 8 — hướng dẫn cài đặt ngắn gọn):**
- Tên miền Mắt Bão & cấu hình DNS A Record
- SSL/TLS Let's Encrypt với Certbot
- Quản lý API key Google Gemini

### Thời gian ước tính

| Mục | Thời gian ước tính |
|---|---|
| Chuẩn bị | 15 phút |
| Cài đặt EC2 | 20 phút |
| Cài đặt RDS & S3 | 20 phút |
| Cài đặt CloudFront | 15 phút |
| Cài đặt WAF | 10 phút |
| Lambda + EventBridge | 20 phút |
| Dịch vụ khác | 15 phút |
| **Tổng cộng** | **~2 giờ** |
