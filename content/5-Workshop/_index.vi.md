---
title: "Workshop"
date: 2026-07-31
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Triển khai LifeSync AI Calendar trên AWS

#### Tổng quan

**LifeSync AI Calendar** là ứng dụng lập lịch thông minh tích hợp AI chuẩn production, được xây dựng bằng Next.js 16 và triển khai trên bộ hạ tầng AWS đầy đủ. Trong workshop này, bạn sẽ học cách cài đặt từng dịch vụ AWS từ đầu theo đúng các bước được dùng để xây dựng hệ thống production thực tế tại [https://phuckhanh.id.vn](https://phuckhanh.id.vn).

Workshop này tập trung vào việc cài đặt **các dịch vụ AWS**. Các dịch vụ khác (Google Gemini AI, tên miền Mắt Bão, SSL Certbot) được hướng dẫn ở phần riêng cuối workshop.

#### Kiến trúc

```
[Người dùng Internet]
      │
      ▼
[Amazon CloudFront CDN] ← [AWS WAF Bảo vệ]
      │
      ▼
[AWS EC2 t2.micro — Next.js 16 + Nginx + PM2]
      │
      ├──► [Amazon RDS MySQL]
      ├──► [Amazon S3 — Lưu trữ Avatar]
      └──► [AWS Lambda + EventBridge — Cào phim CGV]
```

#### Nội dung

1. [Tổng quan Workshop](5.1-Workshop-overview)
2. [Chuẩn bị](5.2-Prerequiste/)
3. [Cài đặt Amazon EC2](5.3-EC2/)
4. [Cài đặt Amazon RDS & S3](5.4-RDS-S3/)
5. [Cài đặt Amazon CloudFront](5.5-CloudFront/)
6. [Cài đặt AWS WAF](5.6-WAF/)
7. [Cài đặt AWS Lambda & EventBridge](5.7-Lambda-EventBridge/)
8. [Cài đặt dịch vụ khác](5.8-OtherServices/)
9. [Dọn dẹp tài nguyên](5.9-Cleanup/)