---
title: "Cài đặt AWS WAF"
date: 2026-07-31
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

## Cài đặt AWS WAF (Web Application Firewall)

AWS WAF (Tường lửa Ứng dụng Web) bảo vệ LifeSync AI Calendar khỏi các cuộc tấn công web phổ biến. Nó được gắn trực tiếp vào **CloudFront distribution** đã tạo ở bước trước, lọc lưu lượng độc hại trước khi tới máy chủ EC2.

**LifeSync WAF bảo vệ chống:**
- **SQL Injection (SQLi)** — ngăn kẻ tấn công thao túng CSDL Amazon RDS MySQL
- **OWASP Top 10** — các lỗ hổng bảo mật ứng dụng web phổ biến nhất
- **Cross-Site Scripting (XSS)** — ngăn chèn script độc hại
- **Layer 7 DDoS** — giới hạn tốc độ để chặn bot tấn công dồn dập

---

### Bước 1: Mở AWS WAF Console

1. Vào **AWS Console** → Tìm **WAF & Shield** → Click **Protection packs (web ACLs)**

2. Click **Create protection pack (web ACL)**

> **Quan trọng**: Đảm bảo region được chuyển sang **Global (CloudFront)** ở góc trên bên phải — WAF phải ở phạm vi Global để gắn vào CloudFront distribution.

![Cài đặt ban đầu WAF](/images/5-Workshop/picture/waf/1_setup.png)

---

### Bước 2: Mô tả Web ACL

3. **Tell us about your app**:
   - **App category**: `Web Application`
   - **App focus**: `Both API and web`

4. **Đặt tên và mô tả**:
   - **Name**: `LifeSync-WAF`
   - **Description**: `Web ACL bảo vệ cho LifeSync AI Calendar`

---

### Bước 3: Chọn tài nguyên cần bảo vệ

5. **Select resources to protect**:
   - Click **Add CloudFront or Amplify resources**
   - Chọn CloudFront distribution (`dbpvljmyvgnai.cloudfront.net`)
   - Click **Add**

![Cài đặt WAF](/images/5-Workshop/picture/waf/2_setting.png)

---

### Bước 4: Chọn quy tắc bảo vệ

6. **Choose initial protections**:
   - Chọn **`Build your own pack (You build it)`** — chi phí ~$7/tháng (tiết kiệm nhất)

7. Thêm **2 AWS Managed Rules** sau (click **Add rules**):

   | Tên quy tắc | Rule Set | Bảo vệ chống |
   |---|---|---|
   | **AWSManagedRulesCommonRuleSet** | AWS Core rule set | OWASP Top 10, XSS, khai thác phổ biến |
   | **AWSManagedRulesSQLiRuleSet** | SQL database | Tấn công SQL Injection vào RDS MySQL |

8. Với mỗi quy tắc, đặt **Action** là `Block`

![Cấu hình quy tắc tùy chỉnh WAF](/images/5-Workshop/picture/waf/3_custom%20rule.png)

---

### Bước 5: Cấu hình hành động mặc định

9. **Default action**: `Allow` — Cho phép mọi lưu lượng không khớp quy tắc nào
   - Các quy tắc trên sẽ chặn yêu cầu độc hại
   - Người dùng hợp lệ sẽ truy cập bình thường

---

### Bước 6: Xem lại và tạo

10. Xem lại tóm tắt:
    - **Name**: `LifeSync-WAF`
    - **Associated resources**: CloudFront distribution của bạn
    - **Rules**: 2 managed rules (Core + SQLi)
    - **Chi phí hàng tháng ước tính**: ~$7 (Web ACL $5 + 2 quy tắc × $1)

11. Click **Create protection pack (web ACL)**

---

### Phân tích chi phí

| Mục | Chi phí |
|---|---|
| Web ACL | $5,00/tháng |
| AWSManagedRulesCommonRuleSet (1 quy tắc) | $1,00/tháng |
| AWSManagedRulesSQLiRuleSet (1 quy tắc) | $1,00/tháng |
| Xử lý request (< 1 triệu/tháng) | ~$0,01/tháng |
| **Tổng cộng** | **~$7,01/tháng** |

> Toàn bộ chi phí WAF được chi trả bằng **AWS Credits** — không tốn thêm chi phí thực.

---

### ✅ Hoàn thành cài đặt WAF

Ứng dụng của bạn hiện được bảo vệ bởi:
- **AWS WAF** với Web ACL `LifeSync-WAF` gắn vào CloudFront
- Bảo vệ **OWASP Top 10** qua AWS Core Rule Set
- Bảo vệ **SQL Injection** cho Amazon RDS MySQL
- Luồng lưu lượng: Internet → CloudFront → WAF → EC2 → RDS

**Tiếp theo**: [Cài đặt AWS Lambda & EventBridge →](../5.7-Lambda-EventBridge/)
