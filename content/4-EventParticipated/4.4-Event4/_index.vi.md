---
title: "AWS Agentic AI & Bedrock AgentCore Workshop"
date: 2026-08-02
weight: 4
chapter: false
pre: " <b> 4.4. </b> "
---

# Báo cáo Chi tiết Sự kiện: AWS Agentic AI Workshop & Amazon Bedrock AgentCore Masterclass

- **Thời gian:** 09:00 - 17:00, Ngày 02/08/2026  
- **Địa điểm:** Tầng 36, Văn phòng AWS Việt Nam, Tòa nhà Bitexco, Số 02 Hải Triều, Q.1, TP. Hồ Chí Minh  
- **Vai trò:** Người tham dự thực hành (Attendee & Hands-on Lab Participant)  

---

### 1. Mục đích sự kiện

Chương trình Masterclass & Workshop chuyên sâu được thiết kế dành cho các Kỹ sư Đám mây và Thực tập sinh FCAJ nhằm làm chủ kiến trúc **Agentic AI** tin cậy trên môi trường sản xuất. Mục tiêu chính của sự kiện là thu hẹp khoảng cách giữa các mô hình ngôn ngữ lớn (LLM) lý thuyết và quy trình triển khai ứng dụng tự chủ (Autonomous AI Agents) thực tế trên hạ tầng đám mây AWS.

Sự kiện tập trung khai thác toàn bộ hệ sinh thái **Amazon Bedrock AgentCore** — bộ dịch vụ chuyên dụng cung cấp các thành phần hạ tầng cốt lõi cho AI Agent bao gồm: **Runtime, Gateway, Identity, Memory, Observability và Guardrails**, kết hợp thực hành trực tiếp qua khung phát triển **Strands Framework** và bộ công cụ **AgentCore CLI**.

---

### 2. Danh sách Diễn giả & Hướng dẫn viên

* **Diễn giả chính & Chuyên gia Kiến trúc AWS:**
  * **Mr. Hải Anh:** Senior Solutions Architect tại AWS Việt Nam — Trực tiếp hướng dẫn phần thực hành Hands-on Lab và giải đáp thắc mắc về tích hợp hạ tầng Enterprise.
  * **Đội ngũ Kỹ sư Giải pháp AWS Việt Nam:** Trình bày hơn 100 slide chuyên sâu về lý thuyết thiết kế Agentic System, chuẩn giao tiếp MCP (Model Context Protocol) và các mô hình bảo mật trên AWS Cloud.

---

### 3. Nội dung Nổi bật & Bài học Kỹ thuật Chuyên sâu

#### A. Mô hình Tư duy Agentic AI & Mức độ Tự chủ (Autonomous Spectrum)
- **Tiến hóa từ LLM đơn thuần đến Multi-Agent System:**
  * *Simple Assistant*: Chỉ hoạt động theo cơ chế Hỏi - Đáp (Prompt - Response) cơ bản dựa trên tri thức có sẵn của LLM.
  * *Single Autonomous Agent*: Tự nhận biết mục tiêu, lên kế hoạch (*Reasoning & Planning*) và tự động kích hoạt công cụ (*Tool Execution*) để hoàn thành nhiệm vụ.
  * *Multi-Agent System*: Hệ thống gồm nhiều AI Agent chuyên biệt tương tác với nhau; phân chia và xử lý các tác vụ phức tạp, chạy ngầm lâu dài (*Long-running background jobs*).
- **Cân bằng giữa Deterministic Workflow & Fully Autonomous:** Doanh nghiệp cần xác định rõ ranh giới tự động hóa. Với các tác vụ tài chính/ngân hàng, hệ thống cần duy trì *Deterministic Workflow* có sự giám sát của con người (*Human-in-the-loop*).

#### B. Điểm nhấn Kiến trúc Amazon Bedrock AgentCore & Gateway

- **AgentCore Gateway — Lớp điều phối trung gian bảo mật:**
  * Gateway đóng vai trò là "điểm trung chuyển" an toàn giữa Agent và các hệ thống backend/dịch vụ ngoài.
  * Tích hợp **Inbound & Outbound Authentication** (hỗ trợ OAuth 2.0, API Key, Token Machine-to-Machine M2M và IAM Policies).
  * Hỗ trợ đa dạng chuẩn Target: REST API Gateway, AWS Lambda Target, OpenAPI Spec, và **MCP Server Target**.

- **Chuẩn giao tiếp Model Context Protocol (MCP) & Semantic Search:**
  * Thay vì gọi cứng URL API endpoint như trước đây, AgentCore bao bọc các công cụ (Tools) qua chuẩn **MCP Schema** định dạng JSON (gồm Name, Description, Required Parameters).
  * Ứng dụng thuật toán **Semantic Search** trực tiếp trong AgentCore Architecture để khi có hàng trăm Agent/Tools khác nhau, hệ thống tự động trích xuất và chọn lọc đúng công cụ phù hợp nhất với yêu cầu hiện tại.

- **Bảo mật, Guardrails & Observability cấp Doanh nghiệp:**
  * **Guardrails Hooks**: Thiết lập 2 điểm Hook kiểm soát (Inbound từ Agent tới Gateway và Outbound từ Gateway về Agent). Lớp này chủ động quét và ngăn chặn rò rỉ dữ liệu nhạy cảm (PII - Personally Identifiable Information) hoặc dữ liệu nội bộ doanh nghiệp.
  * **AWS PrivateLink Integration**: Giải pháp kết nối riêng tư cho doanh nghiệp Enterprise có hạ tầng On-Premise hoặc VPC riêng, truyền dữ liệu an toàn đến AgentCore Gateway mà không đi qua Internet công cộng.
  * **Full CloudWatch Observability**: Ghi nhận toàn bộ vết truy cập (Trace Logs), Metrics và Audit Alerts trên **Amazon CloudWatch** phục vụ kiểm toán bảo mật và tính phí chi tiết.

#### C. Trải nghiệm Thực hành Hands-On Lab

Trong phần thực hành trực tiếp, tôi đã tự tay khởi tạo dự án mẫu **"Returns & Refunds Assistant"** trên máy chủ cá nhân với bộ công cụ phát triển hiện đại:
1. Thiết lập môi trường chuẩn: **Node.js 20+**, **Python 3.12+**, trình quản lý gói siêu tốc **`uv` / `uvx`**, **AWS CLI v2**, **AWS CDK v2** và **`@aws/agentcore` CLI**.
2. Sử dụng **AgentCore CLI** để kiểm thử cục bộ (`agentcore dev`), định nghĩa Tool Schema qua MCP Server và tự động triển khai hạ tầng đám mây lên AWS (`agentcore deploy`).

---

### 4. Kế hoạch Ứng dụng vào Dự án LifeSync AI Calendar

Những kiến thức chuyên sâu từ sự kiện là tiền đề quan trọng để tôi tiếp tục nâng cấp hệ thống **LifeSync AI Calendar**:
1. **Chuẩn hóa Tool Interface với MCP Protocol:** Chuyển đổi các module tự động hóa (như Lambda CGV Crawler, CSP Scheduler Solver) sang chuẩn MCP Schema để AI Engine (Gemini / Bedrock) nhận diện và kích hoạt linh hoạt hơn.
2. **Triển khai Guardrails bảo vệ thông tin cá nhân:** Tích hợp lớp kiểm soát Guardrail để mã hóa/lược bỏ các thông tin nhạy cảm của người dùng (như vị trí GPS chính xác, lịch trình cá nhân) trước khi truyền sang LLM.
3. **Tăng cường khả năng Giám sát (Observability):** Cấu hình Amazon CloudWatch Logs Insights để theo dõi độ trễ (latency), tỷ lệ thành công của Tool Calling và chi phí API thời gian thực.

---

### 5. Minh chứng Tham gia & Thư viện Hình ảnh

<p align="center">
  <img src="images/4-EventParticipated/picture/Event4/myEventTicket.png" alt="Vé tham dự sự kiện chính thức AWS Agentic AI Workshop" width="70%">
</p>
<p align="center"><i>Hình 4.4.1: Vé tham dự sự kiện chính thức AWS Agentic AI Workshop & Bedrock AgentCore Masterclass (02/08/2026)</i></p>

<br>

<p align="center">
  <img src="images/4-EventParticipated/picture/Event4/minhchung1.jpg" alt="Thực hành Hands-On Lab tại Văn phòng AWS" width="48%">
  <img src="images/4-EventParticipated/picture/Event4/minhchung2.jpg" alt="Trình bày Slide Kiến trúc Amazon Bedrock AgentCore" width="48%">
</p>
<p align="center"><i>Hình 4.4.2 & 4.4.3: Hình ảnh thực hành Hands-On Lab và theo dõi bài giảng kiến trúc AgentCore tại Văn phòng AWS Việt Nam (Tầng 36 Bitexco)</i></p>

---

> **Tổng kết:** Sự kiện AWS Agentic AI Workshop ngày 02/08/2026 đã cung cấp bức tranh toàn cảnh về kiến trúc sản xuất của AI Agent, giúp tôi làm chủ công cụ Amazon Bedrock AgentCore và áp dụng trực tiếp các tiêu chuẩn bảo mật, MCP protocol vào sản phẩm thực tế.
