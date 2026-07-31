---
title: "Cài đặt Amazon CloudFront"
date: 2026-07-31
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

## Cài đặt Amazon CloudFront

Amazon CloudFront là mạng phân phối nội dung (CDN) toàn cầu đứng trước máy chủ EC2. Nó cung cấp:
- **Tải trang nhanh hơn** nhờ cache nội dung tại các edge location trên toàn thế giới
- **Che giấu IP** — ẩn Elastic IP EC2 khỏi Internet công khai
- **Bắt buộc HTTPS** qua chứng chỉ SSL được AWS quản lý
- **Tích hợp AWS WAF** — WAF gắn trực tiếp vào CloudFront (trình bày ở Mục 5.6)

---

### Bước 1: Mở CloudFront Console

1. Vào **AWS Console** → Tìm **CloudFront** → Click **Create distribution**

![Tạo CloudFront Distribution](images/5-Workshop/picture/cloudfront/1_setup.png)

---

### Bước 2: Cấu hình Origin

2. **Distribution type**: Chọn **Web** (ứng dụng web chuẩn)

3. **Origin type**: Chọn **Other** *(cho tên miền tùy chỉnh / máy chủ EC2)*

4. **Origin domain**: Nhập tên miền hoặc Elastic IP:
   - Nếu có tên miền: `phuckhanh.id.vn`
   - Chưa có tên miền: `3.104.121.77` (Elastic IP EC2 của bạn)

5. **Protocol**: HTTP only (EC2 xử lý HTTP, CloudFront xử lý HTTPS)

![Cấu hình tên CloudFront](images/5-Workshop/picture/cloudfront/2_name.png)

---

### Bước 3: Cấu hình Cache Behavior mặc định

6. **Viewer protocol policy**: `Redirect HTTP to HTTPS`
   - Mọi yêu cầu HTTP tự động chuyển hướng sang HTTPS

7. **Allowed HTTP methods**: `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`
   - Cần thiết cho Next.js Server Actions, API Routes và gửi form

8. **Cache policy**: Chọn `CachingDisabled` cho nội dung Next.js động
   - Hoặc `CachingOptimized` chỉ cho tài nguyên tĩnh

![Cài đặt Origin CloudFront](images/5-Workshop/picture/cloudfront/3_origin%20setup.png)

---

### Bước 4: Cấu hình Settings

9. **Alternate domain names (CNAME)**: Nhập tên miền tùy chỉnh:
   - `phuckhanh.id.vn`
   - `www.phuckhanh.id.vn`

   > Bỏ qua nếu chưa có tên miền — bạn có thể dùng trực tiếp tên miền CloudFront (vd: `dbpvljmyvgnai.cloudfront.net`)

10. **Custom SSL certificate**: Yêu cầu hoặc import chứng chỉ AWS Certificate Manager (ACM)
    - Click **Request certificate** → Nhập tên miền → Hoàn thành DNS validation
    - Hoặc bỏ qua nếu chỉ dùng tên miền CloudFront

11. **Default root object**: Nhập `index.html` (tùy chọn cho Next.js)

![Cài đặt cuối CloudFront](images/5-Workshop/picture/cloudfront/4_cloudFront%20settings.png)

12. Click **Create distribution** → Chờ 5–10 phút để deploy hoàn tất

---

### Bước 5: Lưu tên miền CloudFront

13. Sau khi tạo xong, sao chép **Distribution domain name** (vd: `dbpvljmyvgnai.cloudfront.net`)

    Đây là URL công khai mới. Bạn có thể:
    - Truy cập trực tiếp: `https://dbpvljmyvgnai.cloudfront.net`
    - Hoặc trỏ DNS tên miền tùy chỉnh về đây (trình bày ở Mục 5.8 — Dịch vụ khác)

---

### Lưu ý quan trọng: Xóa cache CloudFront

Khi deploy code mới, CloudFront có thể vẫn phục vụ nội dung cũ đã cache. Để buộc làm mới cache:

```bash
aws cloudfront create-invalidation \
  --distribution-id YOUR_DISTRIBUTION_ID \
  --paths "/*"
```

Hoặc làm trên AWS Console: **CloudFront** → Chọn distribution → **Invalidations** → **Create invalidation** → Nhập `/*`

---

### ✅ Hoàn thành cài đặt CloudFront

Ứng dụng của bạn hiện có:
- Điểm phân phối **CDN toàn cầu** tại `dbpvljmyvgnai.cloudfront.net`
- **HTTPS tự động** với chuyển hướng HTTP → HTTPS
- **Che giấu IP** — IP EC2 không bị lộ công khai
- Sẵn sàng gắn **AWS WAF** ở bước tiếp theo

**Tiếp theo**: [Cài đặt AWS WAF →](../5.6-WAF/)
