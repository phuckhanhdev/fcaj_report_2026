---
title: "Cài đặt Lambda & EventBridge"
date: 2026-07-31
weight: 7
chapter: false
pre: " <b> 5.7. </b> "
---

## Cài đặt AWS Lambda & Amazon EventBridge

**AWS Lambda** và **Amazon EventBridge** phối hợp với nhau để tự động hóa crawler dữ liệu phim CGV hàng tuần cho LifeSync AI Calendar.

- **AWS Lambda** chạy code crawler (Node.js 20.x) để cào dữ liệu rạp CGV và cập nhật bảng `CGV_MOVIE` trong Amazon RDS MySQL
- **Amazon EventBridge Scheduler** kích hoạt Lambda mỗi **Thứ Hai lúc 00:00 sáng (giờ Việt Nam / UTC+7)**

---

## Phần A: AWS Lambda — Hàm cào phim CGV

### Bước 1: Tạo Lambda Function

1. Vào **AWS Console** → Tìm **Lambda** → Click **Create function**

2. Cấu hình:
   - **Author from scratch**
   - **Function name**: `cgv-movie-crawler`
   - **Runtime**: Node.js 20.x
   - **Architecture**: x86_64
   - **Execution role**: Tạo role mới với quyền cơ bản của Lambda

3. Click **Create function**

![Cài đặt Lambda Function](images/5-Workshop/picture/lambda/cgv_movie_crawler/1_setup.png)

---

### Bước 2: Cấu hình biến môi trường

4. Trong Lambda function → Tab **Configuration** → **Environment variables** → **Edit**

5. Thêm các biến sau:

   | Key | Value |
   |---|---|
   | `RDS_HOST` | Hostname endpoint RDS của bạn |
   | `RDS_USER` | `admin` |
   | `RDS_PASSWORD` | Mật khẩu RDS của bạn |
   | `RDS_DATABASE` | `lifesync_db` |

6. Click **Save**

![Cài đặt biến môi trường Lambda](images/5-Workshop/picture/lambda/cgv_movie_crawler/2_envSetup.png)

---

### Bước 3: Deploy code Lambda

7. Hàm crawler tải dữ liệu phim và suất chiếu CGV từ API CGV rồi upsert vào bảng `CGV_MOVIE`.

8. **Tùy chọn A — Code editor trực tiếp** (cho hàm đơn giản):
   - Click tab **Code** → Dán code crawler vào `index.mjs`

9. **Tùy chọn B — Upload gói ZIP** (khuyến nghị khi có `node_modules`):
   ```bash
   # Trên máy tính local:
   mkdir cgv-crawler && cd cgv-crawler
   npm init -y
   npm install mysql2 axios
   cp /path/to/your/crawler/index.mjs .
   zip -r cgv-crawler.zip .
   ```
   - Trong Lambda → Tab **Code** → **Upload from** → `.zip file` → Upload `cgv-crawler.zip`

10. Đặt **Handler** thành `index.handler`

---

### Bước 4: Cấu hình Timeout & Memory Lambda

11. Trong tab **Configuration** → **General configuration** → **Edit**:
    - **Memory**: `256 MB` (đủ cho crawler)
    - **Timeout**: `5 phút` (gọi API CGV có thể chậm)
    - Click **Save**

---

### Bước 5: Kiểm thử Lambda Function

12. Click **Test** → **Create new test event**:
    - **Event name**: `ManualCrawlTest`
    - **Event JSON**: `{}`
    - Click **Save** → Click **Test**

13. Kiểm tra kết quả thực thi — output thành công hiển thị số phim được cập nhật vào RDS

---

## Phần B: Amazon EventBridge — Lịch Cron hàng tuần

### Bước 1: Tạo EventBridge Schedule

1. Vào **AWS Console** → Tìm **EventBridge** → Click **Scheduler** → **Schedules** → **Create schedule**

![EventBridge Scheduler](images/5-Workshop/picture/eventBridge/1_scheduler.png)

---

### Bước 2: Cấu hình tên & Cron

2. **Schedule name**: `cgv-weekly-crawler`

3. **Schedule pattern**: Chọn **Recurring schedule** → **Cron-based schedule**

4. **Cron expression**: `cron(0 17 ? * SUN *)`
   - Chạy lúc **17:00 UTC Chủ nhật** = **00:00 sáng Thứ Hai giờ Việt Nam (UTC+7)**

5. **Flexible time window**: `Off` (chạy đúng giờ)

![Tên & Cấu hình EventBridge](images/5-Workshop/picture/eventBridge/2_name%26config.png)

---

### Bước 3: Chọn Target (Lambda Function)

6. **Target**: Chọn **AWS Lambda** → **Invoke**

7. **Lambda function**: Chọn `cgv-movie-crawler`

8. **Payload**: `{}` (rỗng — crawler không cần đầu vào)

![EventBridge đã chọn Target](images/5-Workshop/picture/eventBridge/3_target_selected.png)

---

### Bước 4: Cấu hình quyền

9. **Execution role**: Chọn **Create new role for this schedule** — EventBridge tự tạo IAM role với quyền invoke Lambda

10. Click **Next** → Xem lại → Click **Create schedule**

![Xem lại EventBridge](images/5-Workshop/picture/eventBridge/4_review.png)

---

### Tham chiếu biểu thức Cron

| Biểu thức | Ý nghĩa |
|---|---|
| `cron(0 17 ? * SUN *)` | Chủ nhật 17:00 UTC (Thứ Hai 00:00 VN) |
| `cron(0 0 ? * MON *)` | Thứ Hai 00:00 UTC |
| `cron(0 */6 * * ? *)` | Mỗi 6 giờ |

---

### ✅ Hoàn thành cài đặt Lambda & EventBridge

Pipeline tự động hóa hiện đang hoạt động:
- **Mỗi Chủ nhật lúc 17:00 UTC** (Thứ Hai 00:00 sáng giờ Việt Nam), EventBridge kích hoạt Lambda `cgv-movie-crawler`
- Lambda tải lịch chiếu CGV mới nhất và cập nhật bảng `CGV_MOVIE` trong Amazon RDS MySQL
- Người dùng luôn thấy lịch chiếu phim cập nhật khi lên kế hoạch đi xem phim

**Tiếp theo**: [Cài đặt dịch vụ khác →](../5.8-OtherServices/)
