---
title: "AABW - AWS AI Build Week Workshop"
date: 2026-07-25
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# Báo cáo Chi tiết Sự kiện: AABW - AWS AI Build Week Workshop

- **Thời gian:** 09:00 ngày 25/07/2026  
- **Địa điểm:** Tầng 26, Tòa nhà Bitexco, Số 02 Hải Triều, Phường Sài Gòn, TP. Hồ Chí Minh  
- **Vai trò:** Người tham dự (Attendee)  

---

### 1. Mục đích sự kiện

Buổi workshop được thiết kế như một phiên tổng kết và chia sẻ kiến thức chuyên sâu từ cuộc thi hackathon "AABW - AWS AI Build Week", phối hợp tổ chức cùng KNAI Fund (một trong những quỹ đầu tư mạo hiểm lớn nhất tại TP.HCM). Mục tiêu chính là vượt ra khỏi lý thuyết AI khô khan, mang đến cho người tham dự góc nhìn thực tiễn về cách xây dựng **"Agentic AI"**. 

Sự kiện có sự góp mặt của các đội chiến thắng từ cuộc thi, nơi họ chia sẻ toàn bộ hành trình – từ lên ý tưởng, thiết kế kiến trúc hệ thống, cho đến việc vượt qua áp lực 24 giờ code liên tục – để chứng minh cách giải quyết các bài toán kinh doanh bằng giải pháp AI thực tế.

---

### 2. Danh sách diễn giả & Các đội trình bày

* **Khách mời & Lãnh đạo công nghệ:**
  * **Ông Huỳnh Sạ Hùng:** Head of Solutions Architect Việt Nam.
  * **Ông Joseph Marasota:** Head of Technology. Ông đã có bài phát biểu khai mạc truyền cảm hứng, nhìn lại sự nghiệp 20 năm từ thời kỳ máy chủ mainframe cho đến kỷ nguyên AI, chia sẻ về quy mô hơn 1 triệu robot của Amazon và khuyên giới trẻ hãy đóng vai trò "con người trong vòng lặp" (*human in the loop*) để điều phối hệ thống tự động tương lai.

* **Các đội thi trình bày (Đội chiến thắng):**
  * **One Team:** (Thành viên: Anh Duy, Tran Dong, Doan Trung, Minh Viet, Anshul Roy). Xây dựng agent AI đặt hàng đa kênh cho KFC.
  * **Plan V:** (Thành viên: Pham Tien Thuan Phat, Huynh Hoang Long, Le Minh Nghia, Tran Dai Vi, Nguyen An). Trình bày "SA Professional Native App", một trợ lý AI dành riêng cho các Solution Architect.
  * **3KA:** (Thành viên: Huỳnh An Khương, Nguyễn Quốc Huy, Ngô Quang Khôi, Hoàng Lê Thành Đức, Đặng Nguyễn Phước Lộc, Đặng Trường Hưng). Xây dựng "S.H.E.P.H.E.R.D", hệ thống Computer Vision và AI để kiểm soát đám đông.
  * **Signal Scout:** (Thành viên: Le Tan Luc, Do Hoang Hieu, Trieu Quoc Hao, Nguyen Van Duy Khiem, Nguyen Cong Minh, Nguyen Tran Minh Quan). Phát triển hệ thống AI phức tạp chống rửa tiền (AML) và phân tích chiến lược doanh nghiệp.

---

### 3. Điểm nhấn chính & Bài học chi tiết

#### A. Góc nhìn từ chuyên gia: "Mô hình tư duy mới"
Ông Joseph Marasota nhấn mạnh rằng ngành công nghiệp đang biến đổi với tốc độ chóng mặt. Ông khuyên các kỹ sư trẻ nên mạnh dạn thách thức các quy chuẩn cũ. Nếu thế hệ trước tập trung vào sự ổn định của hệ thống ("càng ít thay đổi càng tốt"), thì kỷ nguyên hiện tại đòi hỏi việc release liên tục và tự động hóa cao độ bởi các AI agent.

#### B. Phân tích chuyên sâu về Dự án & Kiến trúc kỹ thuật

* **One Team (AI nhận order KFC):**
  * *Vấn đề:* Các ứng dụng truyền thống tạo ra rào cản (bắt đăng nhập, menu phức tạp), khiến khách hàng nản lòng và hủy đơn.
  * *Giải pháp:* Một AI agent hoạt động trực tiếp trên Zalo và WhatsApp. Nó hiểu ngôn ngữ tự nhiên, dùng tool để lấy menu (qua TinyFish) và quản lý giỏ hàng mà không bắt người dùng chuyển app.
  * *Bài học kỹ thuật:* Thay vì dùng hàm AWS Lambda thông thường (không có bộ nhớ), họ dùng **"AgentCore"**. Điều này giúp bot "nhớ" được lịch sử order của khách. Lựa chọn kiến trúc này giúp giảm 60% chi phí hạ tầng, đạt độ trễ chỉ 3-5 giây với chi phí 0.006 USD/đơn hàng.

* **Plan V (App hỗ trợ Solution Architect):**
  * *Vấn đề:* Các SA thường xuyên bị ép deadline phải thiết kế kiến trúc hạ tầng phức tạp và tính toán chi phí chỉ trong vài giờ.
  * *Giải pháp:* Một ứng dụng AI nơi SA chỉ cần nạp tài liệu yêu cầu (BRD). AI sẽ tự động vẽ sơ đồ kiến trúc trên Draw.io, lập bảng giá AWS và sinh ra code Terraform (IaC).
  * *Bài học kỹ thuật:* Đội đã sử dụng kỹ năng Prompt và Agent Engineering rất tốt để ép LLM tuân thủ chặt chẽ các template chuẩn của công ty (ví dụ: Lambda bắt buộc phải nằm trong VPC). Hệ thống dùng AWS Fargate cho backend và Amazon Bedrock để xử lý AI.

* **3KA (S.H.E.P.H.E.R.D - Kiểm soát đám đông):**
  * *Vấn đề:* Nhân viên sân bay/siêu thị không thể quan sát thủ công hàng chục màn hình camera để phát hiện ùn tắc.
  * *Giải pháp:* Hệ thống nạp luồng camera trực tiếp để đếm số lượng người và tình trạng xếp hàng, từ đó cảnh báo nhân viên trước khi kẹt cứng.
  * *Bài học kỹ thuật:* Đội dùng AWS Kinesis Video Streams truyền video vào cụm xử lý dùng YOLO và ByteTrack để tracking. Một AgentCore (chạy qua Amazon Bedrock) đóng vai trò "Trợ lý điều hành", cho phép nhân viên chat bằng ngôn ngữ tự nhiên để hỏi về tình trạng đám đông tại các khu vực.

* **Signal Scout (Chống rửa tiền / Tài chính):**
  * *Vấn đề:* Chuyên viên tài chính tốn quá nhiều thời gian để tra cứu nhiều hệ thống nhằm phát hiện các hành vi gian lận (chia nhỏ tiền, gom nguồn).
  * *Giải pháp:* Hệ thống lọc nhiều lớp, dùng mô hình Machine Learning (XGBoost) để chấm điểm nhanh, sau đó đẩy qua lớp AI Agent để phân tích sâu.
  * *Bài học kỹ thuật:* Để ngăn chặn việc AI "ảo giác" (*hallucinate*) sinh ra lỗi trong ngành tài chính, họ dùng chiến lược **"Double LLM"**. Một Agent mẹ điều phối các Agent con (Crawler, Analysis). LLM thứ nhất sẽ ra quyết định (Bỏ qua, Giữ lại, Báo cáo), sau đó LLM thứ hai sẽ đối chiếu lại với bộ quy tắc cứng (*Rule base*) trước khi xuất bằng chứng ra Dashboard cho con người duyệt.

#### C. Kinh nghiệm thi Hackathon thực chiến
Tất cả các đội đều chia sẻ những khó khăn chung: thiếu ngủ, code lỗi lúc 3h sáng, và ý tưởng bị phình to (*scope creep*). Lời khuyên xương máu cho các cuộc thi sau:
1. **Kiểm soát phạm vi (Scope):** Hãy làm một tính năng chạy hoàn hảo thay vì một hệ thống đồ sộ nhưng lỗi. Xác định rõ định nghĩa "hoàn thành" ngay từ đầu.
2. **Tập trung vào Bài toán Kinh doanh (Business Problem):** Công nghệ chỉ là công cụ; 70% yếu tố chiến thắng nằm ở việc ý tưởng có giải quyết được "nỗi đau" thực tế hay không (áp dụng các mô hình như Value Proposition Canvas).
3. **Làm việc nhóm:** Phân chia nhiệm vụ cực kỳ rõ ràng (ai code, ai design, ai thuyết trình) và trân trọng trải nghiệm cùng nhau hơn là giải thưởng.

---

### 4. Dự kiến học thêm (Kế hoạch tương lai)

Được truyền cảm hứng từ các giải pháp kỹ thuật chuyên sâu tại sự kiện, mục tiêu học tập tiếp theo của tôi là:
1. **Làm chủ Multi-Agent Orchestration & Double-Check:** Học cách thiết lập hệ thống "Double LLM" (như đội Signal Scout) để các AI Agent tự kiểm tra chéo lẫn nhau, giúp giảm triệt để "ảo giác" khi làm các dự án yêu cầu tính chính xác cao.
2. **Tích hợp Stream Data vào AI:** Tìm hiểu cách đưa dữ liệu thời gian thực (ví dụ dùng AWS Kinesis như đội 3KA) vào LLM thông qua Amazon Bedrock để tạo ra các Agent có khả năng "giám sát trực tiếp".
3. **Quản lý State cho Agent:** Thực hành kết hợp AgentCore và DynamoDB để lưu trữ trạng thái (session) và bộ nhớ dài hạn cho Chatbot, học theo cách tối ưu chi phí của One Team.
4. **Áp dụng Business Canvas:** Tập thói quen thiết lập "Value Proposition & Delivery Canvas" cho mọi dự án kỹ thuật cá nhân để đảm bảo sản phẩm làm ra có tính ứng dụng cao cho doanh nghiệp.

---

### 5. Minh chứng tham gia & Thư viện hình ảnh

<p align="center">
  <img src="images/4-EventParticipated/picture/Event3/1785418082560.jpg" alt="AABW Event Photo 1" width="48%">
  <img src="images/4-EventParticipated/picture/Event3/1785418082561.jpg" alt="AABW Event Photo 2" width="48%">
</p>

<p align="center">
  <img src="images/4-EventParticipated/picture/Event3/1785418082562.jpg" alt="AABW Event Photo 3" width="48%">
  <img src="images/4-EventParticipated/picture/Event3/1785418082563.jpg" alt="AABW Event Photo 4" width="48%">
</p>

<p align="center">
  <img src="images/4-EventParticipated/picture/Event3/1785418082564.jpg" alt="AABW Event Photo 5" width="48%">
  <img src="images/4-EventParticipated/picture/Event3/1785418082565.jpg" alt="AABW Event Photo 6" width="48%">
</p>

---

> Tổng kết: Sự kiện AABW AWS AI Build Week mang lại nhiều giá trị kỹ thuật thực chiến và định hướng phát triển các ứng dụng Agentic AI tiên tiến trên AWS.
