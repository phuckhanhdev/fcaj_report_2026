# Detailed Event Report: AABW - AWS AI Build Week Workshop
**Date & Time:** 09:00 on 25/07/2026  
**Location:** 26th Floor, Bitexco Tower, No. 02 Hai Trieu Street, Sai Gon Ward, Ho Chi Minh City  
**Role:** Attendee  

---

## 🇬🇧 ENGLISH VERSION

### 1. Purpose of the Event
The workshop was designed as an intensive knowledge-sharing and recap session for the "AABW - AWS AI Build Week" hackathon, an event hosted in collaboration with the KNAI Fund (one of the biggest VCs in Ho Chi Minh City) [cite: 1, 5, 6, 7, 8]. The primary goal was to move beyond theoretical AI knowledge and provide attendees with practical insights into building "Agentic AI" [cite: 1]. The event featured the winning teams from the hackathon, who shared their end-to-end journeys—from ideation and architecture design to overcoming 24-hour development constraints—demonstrating how to solve real-world problems with viable AI solutions [cite: 1].

### 2. List of Speakers & Presenting Teams
*   **Event Hosts & Special Guests:**
    *   **Mr. Huynh Sa Hung:** Head of Solutions Architect of Vietnam [cite: 1].
    *   **Mr. Joseph Marasota:** Head of Technology. He delivered the opening keynote, reflecting on his 20-year career evolution from mainframes to AI, discussing Amazon's scale of 1 million+ robots, and inspiring the youth to act as the "human in the loop" for the next generation of automated systems [cite: 1].
*   **Presenting Teams (Hackathon Winners):**
    *   **One Team:** (Members: Anh Duy, Tran Dong, Doan Trung, Minh Viet, Anshul Roy) [cite: 7]. They built a multi-channel AI conversational ordering agent for KFC [cite: 1, 7].
    *   **Lùa Mình (Plan V):** (Members: Pham Tien Thuan Phat, Huynh Hoang Long, Le Minh Nghia, Tran Dai Vi, Nguyen An) [cite: 5]. They presented the "SA Professional Native App," an AI assistant for Solution Architects [cite: 2, 5].
    *   **3KA:** (Members: Huỳnh An Khương, Nguyễn Quốc Huy, Ngô Quang Khôi, Hoàng Lê Thành Đức, Đặng Nguyễn Phước Lộc, Đặng Trường Hưng) [cite: 8]. They built "S.H.E.P.H.E.R.D," an AI and computer vision system for crowd control and congestion prediction [cite: 3, 8].
    *   **Signal Scout:** (Members: Le Tan Luc, Do Hoang Hieu, Trieu Quoc Hao, Nguyen Van Duy Khiem, Nguyen Cong Minh, Nguyen Tran Minh Quan) [cite: 6]. They developed a complex AI system for Anti-Money Laundering (AML) and corporate strategy detection [cite: 3, 6].

### 3. Key Highlights & Detailed Learnings

#### A. Keynote Insight: The "New Mental Model"
Mr. Joseph Marasota highlighted that the industry is transforming at an unprecedented rate [cite: 1]. He advised young technologists to challenge the status quo, noting that while older generations focused on system stability ("do as little changes as possible"), the current era requires rapid, automated releases driven by AI agents [cite: 1]. 

#### B. Deep Dive into Team Projects & Technical Architectures
*   **One Team (KFC AI Ordering Agent):**
    *   *Problem:* Traditional apps cause friction (login, menu navigation), leading to lost momentum and abandoned orders [cite: 1, 7].
    *   *Solution:* An agent that operates directly within Zalo and WhatsApp. It understands natural language intent, uses tools to fetch menus via TinyFish, and manages cart states without forcing the user to switch apps [cite: 1, 7].
    *   *Technical takeaway:* Instead of using standard AWS Lambda functions which lack memory, they utilized "AgentCore" [cite: 1, 7]. This allowed the bot to remember past customer orders [cite: 1]. This architectural choice dropped infrastructure costs by 60%, achieving an end-to-end latency of just 3-5 seconds at $0.006 per order [cite: 1, 7].

*   **Lùa Mình / Plan V (SA Professional Native App):**
    *   *Problem:* Solution Architects often receive sudden requests to design complex cloud architectures and estimate costs within hours [cite: 2, 5].
    *   *Solution:* An AI application where an SA inputs a Business Requirement Document (BRD) [cite: 5]. The AI automatically generates an editable Draw.io architecture diagram, AWS cost estimates, and Terraform IaC (Infrastructure as Code) scripts [cite: 2, 5].
    *   *Technical takeaway:* The team heavily utilized Prompt and Agent Engineering to ensure the LLM outputs adhered to strict company templates (e.g., ensuring Lambdas are attached to VPCs) [cite: 2]. The architecture utilized AWS Fargate for the backend and Amazon Bedrock for AI processing [cite: 5].

*   **3KA (S.H.E.P.H.E.R.D - Crowd Control):**
    *   *Problem:* Airport and supermarket staff struggle to monitor multiple camera feeds manually to prevent bottlenecks [cite: 3, 8].
    *   *Solution:* A system that ingests live camera feeds to track crowd density and queue conditions, alerting staff before severe congestion occurs [cite: 3, 8].
    *   *Technical takeaway:* The team streamed video via AWS Kinesis Video Streams into a processing cluster utilizing YOLO and ByteTrack for object detection [cite: 3, 8]. An AgentCore (via Amazon Bedrock) acted as an "Operator Copilot," allowing staff to ask natural language questions about the crowd status [cite: 3, 8].

*   **Signal Scout (AML / Financial Detection):**
    *   *Problem:* Financial analysts waste time cross-referencing multiple systems to detect fraud like "Structuring" or "Smurfing" [cite: 3, 6].
    *   *Solution:* A multi-layer filtering system using an XGBoost model for fast initial detection, followed by an LLM orchestration layer [cite: 3].
    *   *Technical takeaway:* To prevent "AI Hallucination" in sensitive financial decisions, they employed a "Double LLM" strategy [cite: 3]. A master agent coordinated sub-agents (Crawler Subagent, Analysis Subagent) [cite: 6]. One LLM made an initial decision (Dismiss, Hold, Escalate), and a second LLM verified the reasoning based on strict rule bases before escalating to a human Dashboard [cite: 3, 6].

#### C. Hackathon Best Practices
All teams shared similar challenges: sleep deprivation, code failures at 3 AM, and scope creep [cite: 3, 8]. The unanimous advice for future hackathons:
1.  **Scope Control:** Build one feature perfectly rather than a massive, broken system. Define what "done" looks like early [cite: 3, 8].
2.  **Focus on the Business Problem:** The technology is just a tool; 70% of the winning criteria is based on how well the idea solves a real-world "pain point" (using tools like the Value Proposition Canvas) [cite: 1, 6].
3.  **Team Dynamics:** Delegate clearly (who codes, who designs, who pitches) and value the experience over the prize [cite: 3, 8].

### 4. What I Expect to Learn Next (Future Outlook)
Inspired by the deep technical implementations shown today, my next learning goals are:
1.  **Mastering Multi-Agent Orchestration & Double-Check Systems:** I want to study the "Double LLM" verification method used by Signal Scout to build highly reliable, low-hallucination AI systems for strict business rules [cite: 3, 6].
2.  **Streaming Data into AI:** Learn to integrate real-time data streams (like AWS Kinesis used by team 3KA) with LLMs via Amazon Bedrock to create "live-monitoring" agents [cite: 3, 8].
3.  **Agentic State Management:** Understand how to implement AgentCore and DynamoDB to maintain session states and long-term memory for chatbots, as successfully demonstrated by One Team to reduce costs [cite: 1, 7].
4.  **Applying the Business Canvas:** Practice framing my technical projects using the Value Proposition & Delivery Canvas to ensure they are viable for real-world enterprise adoption [cite: 1, 6].

### 5. Proof of Participation
`[Insert Self-Posted Image / Minh chứng hình ảnh tự đăng tại đây]`

---
---

## 🇻🇳 PHIÊN BẢN TIẾNG VIỆT

### 1. Mục đích sự kiện
Buổi workshop được thiết kế như một phiên tổng kết và chia sẻ kiến thức chuyên sâu từ cuộc thi hackathon "AABW - AWS AI Build Week", phối hợp tổ chức cùng KNAI Fund (một trong những quỹ đầu tư mạo hiểm lớn nhất tại TP.HCM) [cite: 1, 5, 6, 7, 8]. Mục tiêu chính là vượt ra khỏi lý thuyết AI khô khan, mang đến cho người tham dự góc nhìn thực tiễn về cách xây dựng "Agentic AI" [cite: 1]. Sự kiện có sự góp mặt của các đội chiến thắng từ cuộc thi, nơi họ chia sẻ toàn bộ hành trình – từ lên ý tưởng, thiết kế kiến trúc hệ thống, cho đến việc vượt qua áp lực 24 giờ code liên tục – để chứng minh cách giải quyết các bài toán kinh doanh bằng giải pháp AI thực tế [cite: 1].

### 2. Danh sách diễn giả & Các đội trình bày
*   **Khách mời & Lãnh đạo công nghệ:**
    *   **Ông Huỳnh Sa Hưng:** Head of Solutions Architect Việt Nam [cite: 1].
    *   **Ông Joseph Marasota:** Head of Technology. Ông đã có bài phát biểu khai mạc truyền cảm hứng, nhìn lại sự nghiệp 20 năm từ thời kỳ máy chủ mainframe cho đến kỷ nguyên AI, chia sẻ về quy mô hơn 1 triệu robot của Amazon và khuyên giới trẻ hãy đóng vai trò "con người trong vòng lặp" (human in the loop) để điều phối hệ thống tự động tương lai [cite: 1].
*   **Các đội thi trình bày (Đội chiến thắng):**
    *   **One Team:** (Thành viên: Anh Duy, Tran Dong, Doan Trung, Minh Viet, Anshul Roy) [cite: 7]. Xây dựng agent AI đặt hàng đa kênh cho KFC [cite: 1, 7].
    *   **Lùa Mình (Plan V):** (Thành viên: Pham Tien Thuan Phat, Huynh Hoang Long, Le Minh Nghia, Tran Dai Vi, Nguyen An) [cite: 5]. Trình bày "SA Professional Native App", một trợ lý AI dành riêng cho các Solution Architect [cite: 2, 5].
    *   **3KA:** (Thành viên: Huỳnh An Khương, Nguyễn Quốc Huy, Ngô Quang Khôi, Hoàng Lê Thành Đức, Đặng Nguyễn Phước Lộc, Đặng Trường Hưng) [cite: 8]. Xây dựng "S.H.E.P.H.E.R.D", hệ thống Computer Vision và AI để kiểm soát đám đông [cite: 3, 8].
    *   **Signal Scout:** (Thành viên: Le Tan Luc, Do Hoang Hieu, Trieu Quoc Hao, Nguyen Van Duy Khiem, Nguyen Cong Minh, Nguyen Tran Minh Quan) [cite: 6]. Phát triển hệ thống AI phức tạp chống rửa tiền (AML) và phân tích chiến lược doanh nghiệp [cite: 3, 6].

### 3. Điểm nhấn chính & Bài học chi tiết

#### A. Góc nhìn từ chuyên gia: "Mô hình tư duy mới"
Ông Joseph Marasota nhấn mạnh rằng ngành công nghiệp đang biến đổi với tốc độ chóng mặt [cite: 1]. Ông khuyên các kỹ sư trẻ nên mạnh dạn thách thức các quy chuẩn cũ. Nếu thế hệ trước tập trung vào sự ổn định của hệ thống ("càng ít thay đổi càng tốt"), thì kỷ nguyên hiện tại đòi hỏi việc release liên tục và tự động hóa cao độ bởi các AI agent [cite: 1].

#### B. Phân tích chuyên sâu về Dự án & Kiến trúc kỹ thuật
*   **One Team (AI nhận order KFC):**
    *   *Vấn đề:* Các ứng dụng truyền thống tạo ra rào cản (bắt đăng nhập, menu phức tạp), khiến khách hàng nản lòng và hủy đơn [cite: 1, 7].
    *   *Giải pháp:* Một AI agent hoạt động trực tiếp trên Zalo và WhatsApp. Nó hiểu ngôn ngữ tự nhiên, dùng tool để lấy menu (qua TinyFish) và quản lý giỏ hàng mà không bắt người dùng chuyển app [cite: 1, 7].
    *   *Bài học kỹ thuật:* Thay vì dùng hàm AWS Lambda thông thường (không có bộ nhớ), họ dùng "AgentCore" [cite: 1, 7]. Điều này giúp bot "nhớ" được lịch sử order của khách [cite: 1]. Lựa chọn kiến trúc này giúp giảm 60% chi phí hạ tầng, đạt độ trễ chỉ 3-5 giây với chi phí 0.006 USD/đơn hàng [cite: 1, 7].

*   **Lùa Mình / Plan V (App hỗ trợ Solution Architect):**
    *   *Vấn đề:* Các SA thường xuyên bị ép deadline phải thiết kế kiến trúc hạ tầng phức tạp và tính toán chi phí chỉ trong vài giờ [cite: 2, 5].
    *   *Giải pháp:* Một ứng dụng AI nơi SA chỉ cần nạp tài liệu yêu cầu (BRD) [cite: 5]. AI sẽ tự động vẽ sơ đồ kiến trúc trên Draw.io, lập bảng giá AWS và sinh ra code Terraform (IaC) [cite: 2, 5].
    *   *Bài học kỹ thuật:* Đội đã sử dụng kỹ năng Prompt và Agent Engineering rất tốt để ép LLM tuân thủ chặt chẽ các template chuẩn của công ty (ví dụ: Lambda bắt buộc phải nằm trong VPC) [cite: 2]. Hệ thống dùng AWS Fargate cho backend và Amazon Bedrock để xử lý AI [cite: 5].

*   **3KA (S.H.E.P.H.E.R.D - Kiểm soát đám đông):**
    *   *Vấn đề:* Nhân viên sân bay/siêu thị không thể quan sát thủ công hàng chục màn hình camera để phát hiện ùn tắc [cite: 3, 8].
    *   *Giải pháp:* Hệ thống nạp luồng camera trực tiếp để đếm số lượng người và tình trạng xếp hàng, từ đó cảnh báo nhân viên trước khi kẹt cứng [cite: 3, 8].
    *   *Bài học kỹ thuật:* Đội dùng AWS Kinesis Video Streams truyền video vào cụm xử lý dùng YOLO và ByteTrack để tracking [cite: 3, 8]. Một AgentCore (chạy qua Amazon Bedrock) đóng vai trò "Trợ lý điều hành", cho phép nhân viên chat bằng ngôn ngữ tự nhiên để hỏi về tình trạng đám đông tại các khu vực [cite: 3, 8].

*   **Signal Scout (Chống rửa tiền / Tài chính):**
    *   *Vấn đề:* Chuyên viên tài chính tốn quá nhiều thời gian để tra cứu nhiều hệ thống nhằm phát hiện các hành vi gian lận (chia nhỏ tiền, gom nguồn) [cite: 3, 6].
    *   *Giải pháp:* Hệ thống lọc nhiều lớp, dùng mô hình Machine Learning (XGBoost) để chấm điểm nhanh, sau đó đẩy qua lớp AI Agent để phân tích sâu [cite: 3].
    *   *Bài học kỹ thuật:* Để ngăn chặn việc AI "ảo giác" (hallucinate) sinh ra lỗi trong ngành tài chính, họ dùng chiến lược "Double LLM" [cite: 3]. Một Agent mẹ điều phối các Agent con (Crawler, Analysis) [cite: 6]. LLM thứ nhất sẽ ra quyết định (Bỏ qua, Giữ lại, Báo cáo), sau đó LLM thứ hai sẽ đối chiếu lại với bộ quy tắc cứng (Rule base) trước khi xuất bằng chứng ra Dashboard cho con người duyệt [cite: 3, 6].

#### C. Kinh nghiệm thi Hackathon thực chiến
Tất cả các đội đều chia sẻ những khó khăn chung: thiếu ngủ, code lỗi lúc 3h sáng, và ý tưởng bị phình to (scope creep) [cite: 3, 8]. Lời khuyên xương máu cho các cuộc thi sau:
1.  **Kiểm soát phạm vi (Scope):** Hãy làm một tính năng chạy hoàn hảo thay vì một hệ thống đồ sộ nhưng lỗi. Xác định rõ định nghĩa "hoàn thành" ngay từ đầu [cite: 3, 8].
2.  **Tập trung vào Bài toán Kinh doanh (Business Problem):** Công nghệ chỉ là công cụ; 70% yếu tố chiến thắng nằm ở việc ý tưởng có giải quyết được "nỗi đau" thực tế hay không (áp dụng các mô hình như Value Proposition Canvas) [cite: 1, 6].
3.  **Làm việc nhóm:** Phân chia nhiệm vụ cực kỳ rõ ràng (ai code, ai design, ai thuyết trình) và trân trọng trải nghiệm cùng nhau hơn là giải thưởng [cite: 3, 8].

### 4. Dự kiến học thêm (Kế hoạch tương lai)
Được truyền cảm hứng từ các giải pháp kỹ thuật chuyên sâu tại sự kiện, mục tiêu học tập tiếp theo của tôi là:
1.  **Làm chủ Multi-Agent Orchestration & Double-Check:** Học cách thiết lập hệ thống "Double LLM" (như đội Signal Scout) để các AI Agent tự kiểm tra chéo lẫn nhau, giúp giảm triệt để "ảo giác" khi làm các dự án yêu cầu tính chính xác cao [cite: 3, 6].
2.  **Tích hợp Stream Data vào AI:** Tìm hiểu cách đưa dữ liệu thời gian thực (ví dụ dùng AWS Kinesis như đội 3KA) vào LLM thông qua Amazon Bedrock để tạo ra các Agent có khả năng "giám sát trực tiếp" [cite: 3, 8].
3.  **Quản lý State cho Agent:** Thực hành kết hợp AgentCore và DynamoDB để lưu trữ trạng thái (session) và bộ nhớ dài hạn cho Chatbot, học theo cách tối ưu chi phí của One Team [cite: 1, 7].
4.  **Áp dụng Business Canvas:** Tập thói quen thiết lập "Value Proposition & Delivery Canvas" cho mọi dự án kỹ thuật cá nhân để đảm bảo sản phẩm làm ra có tính ứng dụng cao cho doanh nghiệp [cite: 1, 6].

### 5. Minh chứng tham gia
`[Hình ảnh minh chứng tôi tự đăng sẽ được chèn tại đây]`
