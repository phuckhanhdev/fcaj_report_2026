---
title: "Blog 3"
date: 2026-07-15
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# TỐI ƯU CLOUDWATCH ALARMS: BIẾN TIẾNG ỒN THÀNH NHỮNG CẢNH BÁO CÓ GIÁ TRỊ

Có bao giờ bạn cảm thấy mệt mỏi vì hệ thống giám sát liên tục phát ra hàng loạt cảnh báo chung chung, thiếu ngữ cảnh làm gián đoạn công việc mà chẳng giúp ích gì cho việc sửa lỗi?

Trong bài viết này, mình sẽ cùng bạn biến những CloudWatch Alarms ầm ĩ đó thành các cảnh báo thực sự có giá trị, mang lại thông tin chuẩn xác và chỉ dẫn hành động cụ thể mỗi khi sự cố xảy ra!

---

### Vấn đề với cách tạo CloudWatch Alarm truyền thống

Hầu hết chúng ta thường có thói quen tạo Alarm thủ công cho từng server hay service riêng lẻ và dựa vào chỉ số trung bình (AVG). Tuy nhiên, cách làm này bộc lộ rất nhiều hạn chế trong thực tế:
- Khi hệ thống Auto Scaling tạo thêm các instance mới, những máy chủ này hoàn toàn bị bỏ sót và không hề được giám sát.
- Các chỉ số trung bình thường che giấu sự cố rất khéo: CPU trung bình của toàn cluster có thể báo xanh ở mức 19%, nhưng thực tế lại đang có 1 node chết đứng vì quá tải 100% CPU.

Kết quả là chúng ta sẽ phải nhận hàng đống thông báo vô nghĩa (*alert noise*), nhưng khi có sự cố thật sự thì kỹ sư lại mất từ 15 đến 30 phút chỉ để mò mẫm tìm xem Dashboard hay Runbook nằm ở đâu.

---

### Giải pháp khắc phục: Mô hình "3 Right" từ AWS

Để khắc phục triệt để những hạn chế trên và biến các cảnh báo rác thành thông tin có giá trị, AWS mang đến câu trả lời thông qua một chuẩn mực giúp chuẩn hóa toàn bộ hệ thống cảnh báo, gọi là **mô hình "3 Right"**:

#### 1. Right Data: Ghi nhận đúng dữ liệu & Tự động thích ứng
- Để cảnh báo luôn bao phủ chính xác hạ tầng, chúng ta chuyển sang dùng truy vấn SQL động từ **Metrics Insights** (có chứa cấu trúc `GROUP BY`) thay vì chọn tĩnh từng tài nguyên. Nhờ đó, bất kỳ resource mới nào sinh ra cũng sẽ tự động được đưa vào tầm giám sát.
- Đồng thời, việc gán thẻ **Telemetry Tags** (như `Environment=Production`, `Service=Payment`) giúp phân loại cảnh báo chuẩn xác theo từng dịch vụ nghiệp vụ.
- Kết hợp linh hoạt giữa **Static Threshold** (ngưỡng tĩnh dành cho các giới hạn cứng như đĩa đầy > 90% hay tràn hàng đợi) với **Anomaly Detection** (dùng Machine Learning tự học xu hướng traffic hàng ngày để phát hiện điểm bất thường mà không cần cố định một con số).

#### 2. Right Context: Cung cấp đầy đủ ngữ cảnh ngay trong cảnh báo
- Một cảnh báo chất lượng phải cung cấp ngay lập tức bức tranh toàn cảnh mà kỹ sư cần. Tên cảnh báo cần được chuẩn hóa theo cấu trúc `[Môi trường] - [Dịch vụ] - [Lỗi]`, kết hợp gắn trực tiếp liên kết tới Runbook xử lý sự cố và CloudWatch Dashboard tương ứng ngay trong phần mô tả.
- Đặc biệt, khi cảnh báo kích hoạt, tính năng **Contributor Attributes** sẽ tự động đính kèm chính xác ID của tài nguyên đang vi phạm vào nội dung thông báo. Điều này giúp đội ngũ vận hành khoanh vùng và xác định ngay lập tức máy chủ gặp sự cố mà không mất thời gian dò tìm thủ công.

#### 3. Right Actions: Tự động hóa chuỗi phản ứng
- Thay vì chỉ gửi email thông báo đơn thuần, chúng ta tích hợp **Amazon EventBridge** hoặc **SNS** để bắn tin nhắn giàu ngữ cảnh (*Rich Notification*) trực tiếp vào Slack, tự động tạo ticket trên Jira hoặc gọi PagerDuty cho ca trực.
- Xa hơn nữa là **tự động hóa khôi phục (Auto-remediation)**: gắn kịch bản kích hoạt AWS Lambda hoặc AWS Systems Manager (SSM) Runbook để hệ thống tự động khởi động lại dịch vụ hoặc xóa cache lỗi ngay khi Alarm chuyển sang trạng thái cảnh báo mà không cần con người phải can thiệp thủ công.

---

### Ưu điểm sau khi áp dụng giải pháp

- **Tối ưu hóa chỉ số MTTR (Mean Time to Resolution)** một cách rõ rệt: giảm thời gian truy vết sự cố từ hàng chục phút xuống chỉ còn vài giây nhờ thông tin máy chủ bị lỗi, link Dashboard và Runbook đã có sẵn trong thông báo.
- **Chấm dứt hoàn toàn tình trạng ‘spam’ cảnh báo**: lọc bỏ các tín hiệu rác, giúp đội ngũ SRE và DevOps tập trung năng lượng vào các vấn đề thực sự quan trọng.
- **Tự động hóa luồng vận hành**: giải phóng áp lực cho nhân sự trực ca mỗi khi hệ thống mở rộng quy mô.

---

### Kết luận

Thay vì tiếp tục chịu đựng những "tiếng ồn" báo lỗi mờ mịt, việc chuyển sang các cảnh báo có giá trị sẽ biến hệ thống giám sát thành trợ lý đắc lực của bạn. Với khả năng tự động khoanh vùng tài nguyên vi phạm, tự động kích hoạt kịch bản khôi phục và gửi thông báo giàu ngữ cảnh, đội ngũ kỹ thuật có thể hoàn toàn tự tin duy trì độ ổn định của hệ thống mà không còn lo bị quấy rầy bởi các cảnh báo rác.

---

### Hình ảnh kiến trúc & Tham khảo

![Optimizing CloudWatch Alarms](/images/3-BlogsPosted/picture/blog3.png)

#### Tài liệu tham khảo:
- [AWS Management & Governance Blog – Turn your Amazon CloudWatch alarms into actionable signals](https://aws.amazon.com/blogs/mt/turn-your-amazon-cloudwatch-alarms-into-actionable-signals/)