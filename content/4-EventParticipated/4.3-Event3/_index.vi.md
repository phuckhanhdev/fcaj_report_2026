---
title: "Event 3"
date: 2026-07-25
weight: 1
chapter: false
pre: " <b> 4.3. </b> "
---

# Bài thu hoạch: “AABW - AWS AI Build Week Workshop”

### Mục Đích Của Sự Kiện

- Chia sẻ những góc nhìn thực tiễn từ trải nghiệm hackathon AABW - AWS AI Build Week
- Khám phá cách các giải pháp Agentic AI thực tế được thiết kế và triển khai
- Nhấn mạnh những quyết định kiến trúc kỹ thuật đằng sau các sản phẩm AI thành công
- Đóng góp cảm hứng cho việc học tập tiếp theo về xây dựng hệ thống AI đáng tin cậy và có khả năng mở rộng

### Thông Tin Sự Kiện

- **Thời gian:** 09:00 ngày 25/07/2026
- **Địa điểm:** Tầng 26, Bitexco Tower, số 02 Hai Trieu, phường Sài Gòn, TP. Hồ Chí Minh
- **Vai trò:** Người tham dự

### Danh Sách Diễn Giả

- **Ông Huỳnh Sa Hưng** – Head of Solutions Architect Việt Nam
- **Ông Joseph Marasota** – Head of Technology
- **Các đội trình bày:** One Team, Lùa Mình (Plan V), 3KA và Signal Scout

### Nội Dung Nổi Bật

#### Phát biểu khai mạc: “mô hình tư duy mới”

- Ngành công nghiệp đang thay đổi với tốc độ chưa từng có, và các kỹ sư trẻ cần thích nghi nhanh hơn
- Ông Joseph Marasota khuyến khích mọi người thách thức những giả định cũ và đi xa hơn khỏi các hệ thống “ổn định nhưng chậm”
- Kỷ nguyên hiện tại ưu tiên việc release nhanh, tự động hóa cao và vận hành bằng các AI agent cùng sự can thiệp của con người trong vòng lặp

#### Phân tích sâu các dự án hackathon chiến thắng

- One Team xây dựng agent AI đặt hàng đa kênh cho KFC, hoạt động trực tiếp trên Zalo và WhatsApp
- Lùa Mình (Plan V) phát triển “SA Professional Native App” để hỗ trợ các Solution Architect tạo sơ đồ kiến trúc, ước tính chi phí AWS và sinh code Terraform từ tài liệu BRD
- 3KA xây dựng “S.H.E.P.H.E.R.D”, hệ thống computer vision và AI cho việc kiểm soát đám đông và dự báo ùn tắc bằng luồng camera trực tiếp
- Signal Scout phát triển hệ thống AI phức tạp cho AML và phân tích chiến lược doanh nghiệp bằng cách kết hợp lọc nhiều lớp và phân tích đa agent

#### Những bài học kỹ thuật nổi bật từ các đội

- **One Team:** Thay thế mô hình Lambda truyền thống bằng AgentCore để cung cấp bộ nhớ cho bot, giảm chi phí hạ tầng tới 60% và đạt độ trễ thấp với chi phí khá nhỏ trên mỗi đơn hàng
- **Lùa Mình / Plan V:** Sử dụng prompt engineering và agent engineering để buộc LLM tuân thủ đúng các template doanh nghiệp và tạo ra đầu ra thực tế cho các kiến trúc sư
- **3KA:** Kết hợp AWS Kinesis Video Streams, YOLO, ByteTrack và AgentCore để xây dựng trợ lý giám sát thời gian thực cho tình trạng đám đông
- **Signal Scout:** Áp dụng chiến lược “Double LLM” để giảm hiện tượng hallucination và tăng độ tin cậy trong các tình huống doanh nghiệp nhạy cảm

### Những Gì Học Được

#### Tư Duy

- **Business-first approach**: Những ý tưởng mạnh nhất đều giải quyết đúng nỗi đau thực tế, không chỉ minh họa công nghệ
- **Thử nghiệm thực tế**: Kết quả tốt nhất đến từ việc xây dựng nhanh, học từ sai sót và cải thiện liên tục
- **Human-in-the-loop**: AI nên hỗ trợ con người thay vì thay thế quyết định con người trong những tình huống quan trọng

#### Kiến Trúc Kỹ Thuật

- **Thiết kế agentic**: Xây dựng hệ thống AI có bộ nhớ, công cụ và trạng thái có thể làm cho chúng hữu ích hơn nhiều trong môi trường production
- **Tích hợp dữ liệu thời gian thực**: Các nguồn dữ liệu như video và stream sự kiện có thể được kết nối với AI agent để tạo trải nghiệm giám sát trực tiếp
- **Kỹ thuật độ tin cậy**: Các lớp kiểm tra, quy tắc nghiệp vụ và điều phối đa agent là yếu tố cần thiết cho AI đáng tin cậy

#### Bài học từ hackathon

- **Kiểm soát phạm vi**: Một tính năng được triển khai hoàn chỉnh tốt hơn một hệ thống lớn nhưng dễ vỡ dưới áp lực phức tạp
- **Điều phối nhóm**: Việc phân chia vai trò rõ ràng giữa coding, thiết kế và pitching là rất quan trọng
- **Học hỏi quan trọng hơn chiến thắng**: Trải nghiệm và bài học thu được từ quá trình này có giá trị ngang với giải thưởng

### Ứng Dụng Vào Công Việc

- **Nghiên cứu orchestration đa agent**: Tìm hiểu cách nhiều agent có thể phối hợp an toàn và hiệu quả
- **Học thiết kế agent có trạng thái**: Hiểu cách lưu giữ ngữ cảnh và bộ nhớ dài hạn trong các ứng dụng AI
- **Thử nghiệm AI theo stream**: Kết nối nguồn dữ liệu thời gian thực vào hệ thống dựa trên LLM để tạo hành vi năng động hơn
- **Định hình dự án theo giá trị kinh doanh**: Áp dụng tư duy value proposition và delivery để giữ cho công việc kỹ thuật luôn phù hợp với nhu cầu thực tế

### Trải Nghiệm Trong Sự Kiện

Tham gia **workshop AABW - AWS AI Build Week** là một trải nghiệm rất đáng giá vì nó kết nối đổi mới công nghệ với ứng dụng kinh doanh thực tế. Sự kiện giúp tôi có một bức tranh rõ ràng hơn về cách các hệ thống AI hiện đại có thể chuyển từ ý tưởng sang triển khai thực tế khi có kiến trúc, công cụ và vận hành nhóm đúng cách.

#### Học hỏi từ góc nhìn chuyên gia

- Các bài keynote và buổi chia sẻ từ khách mời mang lại cảm hứng mạnh mẽ để nghĩ vượt ra khỏi phát triển phần mềm truyền thống và chuyển sang các workflow tự động, AI-driven hơn
- Các bài trình bày từ các đội chiến thắng cho thấy cách một ý tưởng có thể biến thành giải pháp hoạt động ngay cả trong môi trường áp lực thời gian

#### Tiếp cận hiểu biết kỹ thuật thực tế

- Tôi học được cách các đội khác nhau tiếp cận cùng một thử thách AI theo nhiều hướng khác nhau, từ agent hội thoại cho đến computer vision và phân tích tài chính
- Các ví dụ cũng làm rõ cách các lựa chọn kiến trúc như AgentCore, Bedrock, Kinesis và Fargate ảnh hưởng đến hiệu suất, chi phí và độ tin cậy của hệ thống

#### Nhìn thấy cách bài toán kinh doanh định hình thiết kế kỹ thuật

- Mỗi dự án không chỉ ấn tượng về mặt kỹ thuật mà còn gắn với bài toán kinh doanh cụ thể như đặt hàng, hỗ trợ kiến trúc, quản lý đám đông hoặc phát hiện gian lận
- Điều này củng cố tầm quan trọng của việc thiết kế giải pháp AI theo value proposition rõ ràng thay vì chỉ tập trung vào công nghệ

#### Bài học rút ra

- Các giải pháp AI mạnh nhất luôn kết hợp chiều sâu kỹ thuật với bối cảnh tổ chức và kinh doanh rõ ràng
- Độ tin cậy, hiệu quả chi phí và khả năng giải thích đều quan trọng không kém khả năng của mô hình
- Xây dựng với AI không chỉ là viết code, mà còn là tạo ra hệ thống đáng tin cậy và thật sự có thể được áp dụng trong thực tế

#### Một số hình ảnh khi tham gia sự kiện

*Thêm các hình ảnh của bạn tại đây*

> Tổng thể, sự kiện không chỉ cung cấp kiến thức kỹ thuật mà còn mở rộng góc nhìn của tôi về cách tư duy về thiết kế sản phẩm AI, kiến trúc hệ thống và con đường phát triển trong tương lai.
