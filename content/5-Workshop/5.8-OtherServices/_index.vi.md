---
title: "Cài đặt dịch vụ khác"
date: 2026-07-31
weight: 8
chapter: false
pre: " <b> 5.8. </b> "
---

## Cài đặt dịch vụ khác

Phần này hướng dẫn cài đặt các dịch vụ ngoài AWS cần thiết để LifeSync AI Calendar hoạt động trên production. Các dịch vụ này phối hợp với hạ tầng AWS đã cài đặt ở các phần trước.

---

## 1. Tên miền tùy chỉnh với Mắt Bão

Mắt Bão (`matbao.net`) là nhà đăng ký tên miền dùng cho `phuckhanh.id.vn`. Cần cấu hình DNS để điều hướng lưu lượng về CloudFront distribution.

### Các bước cài đặt

1. Đăng nhập [id.matbao.net](https://id.matbao.net) → Chọn quản lý tên miền `phuckhanh.id.vn`

2. Vào **Quản lý DNS** → Thêm 2 **CNAME Record** trỏ về CloudFront:

   | Host | Loại | Giá trị | TTL |
   |---|---|---|---|
   | `@` (root) | CNAME | `dbpvljmyvgnai.cloudfront.net` | 3600 |
   | `www` | CNAME | `dbpvljmyvgnai.cloudfront.net` | 3600 |

   > **Lưu ý**: Một số nhà cung cấp không hỗ trợ CNAME trên root (`@`). Trong trường hợp này, dùng **A Record**:
   > - `@` → Loại `A` → Giá trị: Elastic IP EC2 (`3.104.121.77`)
   > - `www` → Loại `A` → Giá trị: Elastic IP EC2 (`3.104.121.77`)

3. Chờ 5–30 phút để DNS lan truyền

4. Kiểm tra DNS:
   ```bash
   nslookup phuckhanh.id.vn
   # Nên trả về CloudFront hoặc IP EC2
   ```

---

## 2. SSL/TLS với Let's Encrypt (Certbot)

Certbot cung cấp **chứng chỉ SSL/TLS miễn phí** từ Let's Encrypt cho tên miền. Cho phép HTTPS trên Nginx EC2.

### Các bước cài đặt

1. SSH vào EC2 và cài Certbot:
   ```bash
   sudo apt install -y certbot python3-certbot-nginx
   ```

2. Yêu cầu và tự động cài chứng chỉ:
   ```bash
   sudo certbot --nginx -d phuckhanh.id.vn -d www.phuckhanh.id.vn
   ```

3. Làm theo hướng dẫn tương tác:
   - Nhập email để nhận thông báo gia hạn
   - Chấp nhận Điều khoản dịch vụ
   - Chọn tùy chọn **2** (Redirect — bắt buộc HTTPS cho mọi yêu cầu HTTP)

4. Certbot tự động:
   - Lấy chứng chỉ từ Let's Encrypt
   - Sửa cấu hình Nginx để bật HTTPS trên cổng 443
   - Thiết lập tự gia hạn (chạy 2 lần/ngày qua systemd timer)

5. Kiểm thử gia hạn chứng chỉ:
   ```bash
   sudo certbot renew --dry-run
   # Nên hoàn thành không có lỗi
   ```

> **Lưu ý**: Nếu dùng CloudFront làm CDN (khuyến nghị), không cần Certbot trên EC2 — CloudFront xử lý HTTPS. Certbot chỉ cần khi người dùng truy cập EC2 trực tiếp không qua CloudFront.

---

## 3. Google Gemini AI API

LifeSync AI Calendar dùng **Google Gemini 2.5 Flash** để phân tích ý định lập lịch từ ngôn ngữ tự nhiên (chuyển đổi "ăn trưa ngày mai lúc 12h" thành dữ liệu sự kiện lịch có cấu trúc).

### Các bước cài đặt

1. Vào [Google AI Studio](https://aistudio.google.com/) → Đăng nhập Google

2. Click **Get API key** → **Create API key** → Sao chép key

3. Thêm vào `.env.local` trên EC2:
   ```bash
   GOOGLE_AI_API_KEY=AIzaSy...key-của-bạn
   ```

4. Khởi động lại ứng dụng:
   ```bash
   pm2 restart lifesync
   ```

### Các tính năng API được dùng

| Tính năng | Mô tả |
|---|---|
| **Intent Parsing** | Chuyển ngôn ngữ tự nhiên → JSON sự kiện có cấu trúc (tiêu đề, ngày, giờ, thời lượng) |
| **Slot Filling** | Hỏi thêm khi thiếu thông tin |
| **Multi-turn Chat** | Giữ ngữ cảnh hội thoại 3 ngày |
| **Chọn Strategy** | AI xác định chiến lược lập lịch khoa học áp dụng |

### Chi phí
- Gói miễn phí: 15 request/phút, 1 triệu token/phút
- Production có người dùng thực: nâng cấp gói trả phí ~$0,075 mỗi 1 triệu token

---

## 4. Xác thực NextAuth.js

LifeSync AI Calendar dùng **NextAuth.js** (nay là Auth.js) để xác thực người dùng bằng Google OAuth 2.0.

### Các bước cài đặt

1. Vào [Google Cloud Console](https://console.cloud.google.com/) → **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth 2.0 Client IDs**

2. Cấu hình:
   - **Application type**: Web application
   - **Authorized redirect URIs**: `https://phuckhanh.id.vn/api/auth/callback/google`

3. Sao chép **Client ID** và **Client Secret**

4. Thêm vào `.env.local`:
   ```bash
   GOOGLE_CLIENT_ID=xxxxxx.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=GOCSPX-...
   NEXTAUTH_SECRET=<chuỗi-ngẫu-nhiên-32-ký-tự>
   NEXTAUTH_URL=https://phuckhanh.id.vn
   ```

---

### ✅ Hoàn thành cài đặt tất cả dịch vụ

Bộ stack production LifeSync AI Calendar đầy đủ của bạn đang chạy:

| Lớp | Dịch vụ | Trạng thái |
|---|---|---|
| **DNS** | Tên miền Mắt Bão | ✅ Đã cấu hình |
| **CDN** | Amazon CloudFront | ✅ Hoạt động |
| **Bảo mật** | AWS WAF | ✅ Hoạt động |
| **SSL/TLS** | Let's Encrypt / CloudFront | ✅ Hoạt động |
| **App Server** | Amazon EC2 + Nginx + PM2 | ✅ Đang chạy |
| **CSDL** | Amazon RDS MySQL | ✅ Đang chạy |
| **Lưu trữ file** | Amazon S3 | ✅ Hoạt động |
| **AI Engine** | Google Gemini 2.5 Flash | ✅ Đã kết nối |
| **Xác thực** | NextAuth.js + Google OAuth | ✅ Hoạt động |
| **Crawler** | Lambda + EventBridge | ✅ Đã lên lịch |
| **CI/CD** | GitHub Actions | ✅ Hoạt động |

**Tiếp theo**: [Dọn dẹp tài nguyên →](../5.9-Cleanup/)
