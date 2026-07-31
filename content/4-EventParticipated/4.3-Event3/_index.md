---
title: "AABW - AWS AI Build Week Workshop"
date: 2026-07-25
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# Detailed Event Report: AABW - AWS AI Build Week Workshop

- **Date & Time:** 09:00 on 25/07/2026  
- **Location:** 26th Floor, Bitexco Tower, No. 02 Hai Trieu Street, Sai Gon Ward, Ho Chi Minh City  
- **Role:** Attendee  

---

### 1. Purpose of the Event

The workshop was designed as an intensive knowledge-sharing and recap session for the "AABW - AWS AI Build Week" hackathon, an event hosted in collaboration with the KNAI Fund (one of the biggest VCs in Ho Chi Minh City). The primary goal was to move beyond theoretical AI knowledge and provide attendees with practical insights into building **"Agentic AI"**. 

The event featured the winning teams from the hackathon, who shared their end-to-end journeys — from ideation and architecture design to overcoming 24-hour development constraints — demonstrating how to solve real-world problems with viable AI solutions.

---

### 2. List of Speakers & Presenting Teams

* **Event Hosts & Special Guests:**
  * **Mr. Huynh Sa Hung:** Head of Solutions Architecture, AWS Vietnam.
  * **Mr. Joseph Marasota:** Head of Technology. He delivered the opening keynote, reflecting on his 20-year career evolution from mainframes to AI, discussing Amazon's scale of 1 million+ robots, and inspiring the youth to act as the "human in the loop" for the next generation of automated systems.

* **Presenting Teams (Hackathon Winners):**
  * **One Team:** (Members: Anh Duy, Tran Dong, Doan Trung, Minh Viet, Anshul Roy). They built a multi-channel AI conversational ordering agent for KFC.
  * **Lùa Mình (Plan V):** (Members: Pham Tien Thuan Phat, Huynh Hoang Long, Le Minh Nghia, Tran Dai Vi, Nguyen An). They presented the "SA Professional Native App," an AI assistant for Solution Architects.
  * **3KA:** (Members: Huỳnh An Khương, Nguyễn Quốc Huy, Ngô Quang Khôi, Hoàng Lê Thành Đức, Đặng Nguyễn Phước Lộc, Đặng Trường Hưng). They built "S.H.E.P.H.E.R.D," an AI and computer vision system for crowd control and congestion prediction.
  * **Signal Scout:** (Members: Le Tan Luc, Do Hoang Hieu, Trieu Quoc Hao, Nguyen Van Duy Khiem, Nguyen Cong Minh, Nguyen Tran Minh Quan). They developed a complex AI system for Anti-Money Laundering (AML) and corporate strategy detection.

---

### 3. Key Highlights & Detailed Learnings

#### A. Keynote Insight: The "New Mental Model"
Mr. Joseph Marasota highlighted that the industry is transforming at an unprecedented rate. He advised young technologists to challenge the status quo, noting that while older generations focused on system stability ("do as little changes as possible"), the current era requires rapid, automated releases driven by AI agents.

#### B. Deep Dive into Team Projects & Technical Architectures

* **One Team (KFC AI Ordering Agent):**
  * *Problem:* Traditional apps cause friction (login, menu navigation), leading to lost momentum and abandoned orders.
  * *Solution:* An agent that operates directly within Zalo and WhatsApp. It understands natural language intent, uses tools to fetch menus via TinyFish, and manages cart states without forcing the user to switch apps.
  * *Technical Takeaway:* Instead of using standard AWS Lambda functions which lack memory, they utilized **AgentCore**. This allowed the bot to remember past customer orders. This architectural choice dropped infrastructure costs by 60%, achieving an end-to-end latency of just 3-5 seconds at $0.006 per order.

* **Lùa Mình / Plan V (SA Professional Native App):**
  * *Problem:* Solution Architects often receive sudden requests to design complex cloud architectures and estimate costs within hours.
  * *Solution:* An AI application where an SA inputs a Business Requirement Document (BRD). The AI automatically generates an editable Draw.io architecture diagram, AWS cost estimates, and Terraform IaC (Infrastructure as Code) scripts.
  * *Technical Takeaway:* The team heavily utilized Prompt and Agent Engineering to ensure the LLM outputs adhered to strict company templates (e.g., ensuring Lambdas are attached to VPCs). The architecture utilized AWS Fargate for the backend and Amazon Bedrock for AI processing.

* **3KA (S.H.E.P.H.E.R.D - Crowd Control):**
  * *Problem:* Airport and supermarket staff struggle to monitor multiple camera feeds manually to prevent bottlenecks.
  * *Solution:* A system that ingests live camera feeds to track crowd density and queue conditions, alerting staff before severe congestion occurs.
  * *Technical Takeaway:* The team streamed video via AWS Kinesis Video Streams into a processing cluster utilizing YOLO and ByteTrack for object detection. An AgentCore (via Amazon Bedrock) acted as an "Operator Copilot," allowing staff to ask natural language questions about the crowd status.

* **Signal Scout (AML / Financial Detection):**
  * *Problem:* Financial analysts waste time cross-referencing multiple systems to detect fraud like "Structuring" or "Smurfing".
  * *Solution:* A multi-layer filtering system using an XGBoost model for fast initial detection, followed by an LLM orchestration layer.
  * *Technical Takeaway:* To prevent "AI Hallucination" in sensitive financial decisions, they employed a **"Double LLM"** strategy. A master agent coordinated sub-agents (Crawler Subagent, Analysis Subagent). One LLM made an initial decision (Dismiss, Hold, Escalate), and a second LLM verified the reasoning based on strict rule bases before escalating to a human Dashboard.

#### C. Hackathon Best Practices
All teams shared similar challenges: sleep deprivation, code failures at 3 AM, and scope creep. The unanimous advice for future hackathons:
1. **Scope Control:** Build one feature perfectly rather than a massive, broken system. Define what "done" looks like early.
2. **Focus on the Business Problem:** The technology is just a tool; 70% of the winning criteria is based on how well the idea solves a real-world "pain point" (using tools like the Value Proposition Canvas).
3. **Team Dynamics:** Delegate clearly (who codes, who designs, who pitches) and value the experience over the prize.

---

### 4. Future Outlook (What I Expect to Learn Next)

Inspired by the deep technical implementations shown today, my next learning goals are:
1. **Mastering Multi-Agent Orchestration & Double-Check Systems:** Study the "Double LLM" verification method used by Signal Scout to build highly reliable, low-hallucination AI systems for strict business rules.
2. **Streaming Data into AI:** Learn to integrate real-time data streams (like AWS Kinesis used by team 3KA) with LLMs via Amazon Bedrock to create "live-monitoring" agents.
3. **Agentic State Management:** Understand how to implement AgentCore and DynamoDB to maintain session states and long-term memory for chatbots, as successfully demonstrated by One Team to reduce costs.
4. **Applying the Business Canvas:** Practice framing technical projects using the Value Proposition & Delivery Canvas to ensure they are viable for real-world enterprise adoption.

---

### 5. Proof of Participation & Event Gallery

<p align="center">
  <img src="/images/4-EventParticipated/picture/Event3/1785418082560.jpg" alt="AABW Event Photo 1" width="48%">
  <img src="/images/4-EventParticipated/picture/Event3/1785418082561.jpg" alt="AABW Event Photo 2" width="48%">
</p>

<p align="center">
  <img src="/images/4-EventParticipated/picture/Event3/1785418082562.jpg" alt="AABW Event Photo 3" width="48%">
  <img src="/images/4-EventParticipated/picture/Event3/1785418082563.jpg" alt="AABW Event Photo 4" width="48%">
</p>

<p align="center">
  <img src="/images/4-EventParticipated/picture/Event3/1785418082564.jpg" alt="AABW Event Photo 5" width="48%">
  <img src="/images/4-EventParticipated/picture/Event3/1785418082565.jpg" alt="AABW Event Photo 6" width="48%">
</p>

---

> Overall, the AABW AWS AI Build Week workshop provided invaluable technical insights and inspired new directions for building scalable Agentic AI applications on AWS.
