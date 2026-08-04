---
title: "AWS Agentic AI & Bedrock AgentCore Workshop"
date: 2026-08-02
weight: 4
chapter: false
pre: " <b> 4.4. </b> "
---

# Detailed Event Report: AWS Agentic AI Workshop & Amazon Bedrock AgentCore Masterclass

- **Date & Time:** 09:00 - 17:00, August 02, 2026  
- **Location:** 36th Floor, AWS Vietnam Office, Bitexco Financial Tower, No. 02 Hai Trieu, District 1, Ho Chi Minh City  
- **Role:** Attendee & Hands-on Lab Participant  

---

### 1. Purpose of the Event

The intensive Masterclass & Workshop was designed for Cloud Engineers and FCAJ Interns to master production-ready **Agentic AI** architectures on AWS. The primary goal was to bridge the gap between theoretical Large Language Models (LLMs) and real-world Autonomous AI Agent deployments on AWS cloud infrastructure.

The workshop focused comprehensively on the **Amazon Bedrock AgentCore** ecosystem — a dedicated suite of services providing foundational infrastructure building blocks for AI Agents, including **Runtime, Gateway, Identity, Memory, Observability, and Guardrails**, combined with direct hands-on practice using the **Strands Framework** and **AgentCore CLI**.

---

### 2. Speakers & Facilitators

* **Keynote Speakers & AWS Architecture Experts:**
  * **Mr. Hai Anh:** Senior Solutions Architect at AWS Vietnam — Led the hands-on lab sessions and provided deep-dive guidance on enterprise infrastructure integration.
  * **AWS Vietnam Solutions Engineering Team:** Delivered over 100 technical slides covering Agentic System design patterns, Model Context Protocol (MCP), and cloud security standards.

---

### 3. Key Technical Highlights & Learnings

#### A. Agentic AI Mental Model & The Autonomous Spectrum
- **Evolution from Simple LLM to Multi-Agent Systems:**
  * *Simple Assistant*: Basic prompt-response mechanism relying solely on static LLM knowledge.
  * *Single Autonomous Agent*: Goal-aware system capable of reasoning, step planning, and automated tool execution.
  * *Multi-Agent System*: Interconnected specialized agents communicating to break down, delegate, and execute complex, long-running background tasks.
- **Balancing Deterministic Workflows vs. Full Autonomy:** Enterprise workloads (especially in banking and finance) require clear boundaries, maintaining deterministic workflows with human-in-the-loop oversight.

#### B. Amazon Bedrock AgentCore & Gateway Architecture

- **AgentCore Gateway — Secure Middleware Orchestration:**
  * Serves as an isolated, secure proxy between AI Agents and backend target tools.
  * Supports **Inbound & Outbound Authentication** (OAuth 2.0, API Keys, Machine-to-Machine M2M Tokens, and IAM Policies).
  * Ingests multiple target types: REST API Gateways, AWS Lambda Targets, OpenAPI Specifications, and **MCP (Model Context Protocol) Server Targets**.

- **Model Context Protocol (MCP) & Semantic Tool Discovery:**
  * Instead of hardcoding API endpoints, AgentCore encapsulates tools using the **MCP Schema** JSON standard (Name, Description, Required Parameters).
  * Leverages built-in **Semantic Search** within the AgentCore architecture, allowing agents to dynamically query and select the most relevant tools out of hundreds of registered targets.

- **Enterprise Security, Guardrails & Observability:**
  * **Guardrails Hooks**: Inbound and Outbound hooks sanitize data, preventing PII (Personally Identifiable Information) or proprietary corporate data leaks before reaching end-users.
  * **AWS PrivateLink Integration**: Enables private, secure communication between on-premise enterprise clients or isolated VPCs and AgentCore Gateways without traversing the public internet.
  * **Full CloudWatch Observability**: Logs audit traces, execution metrics, and security alerts to **Amazon CloudWatch** for compliance auditing and granular cost attribution.

#### C. Hands-On Lab Experience

During the practical workshop, I developed a hands-on project named **"Returns & Refunds Assistant"** utilizing a modern developer stack:
1. Environment Setup: **Node.js 20+**, **Python 3.12+**, **`uv` / `uvx`** package runner, **AWS CLI v2**, **AWS CDK v2**, and **`@aws/agentcore` CLI**.
2. Workflow Execution: Used **AgentCore CLI** for local testing (`agentcore dev`), defined MCP Tool Schemas, and deployed agent infrastructure to AWS (`agentcore deploy`).

---

### 4. Future Application to LifeSync AI Calendar Project

The technical concepts acquired from this workshop will be directly integrated into the **LifeSync AI Calendar** platform:
1. **Standardizing Tool Interfaces with MCP:** Re-architecting automation components (Lambda CGV Crawler, CSP Scheduler) into MCP Tool Schemas for seamless LLM tool calling.
2. **Implementing Privacy Guardrails:** Adding Guardrail hooks to scrub user sensitive data (e.g., exact GPS coordinates, personal daily routines) prior to LLM processing.
3. **Enhancing System Observability:** Configuring Amazon CloudWatch Logs Insights to track tool-calling latency, success rates, and real-time API invocation costs.

---

### 5. Proof of Participation & Event Gallery

<p align="center">
  <img src="images/4-EventParticipated/picture/Event4/myEventTicket.png" alt="Official AWS Agentic AI Workshop Ticket" width="70%">
</p>
<p align="center"><i>Figure 4.4.1: Official Event Ticket for AWS Agentic AI Workshop & Bedrock AgentCore Masterclass (August 02, 2026)</i></p>

<br>

<p align="center">
  <img src="images/4-EventParticipated/picture/Event4/minhchung1.jpg" alt="Hands-On Lab Practice at AWS Office" width="48%">
  <img src="images/4-EventParticipated/picture/Event4/minhchung2.jpg" alt="Amazon Bedrock AgentCore Architecture Presentation" width="48%">
</p>
<p align="center"><i>Figures 4.4.2 & 4.4.3: Hands-On Lab development and AgentCore architecture lecture at AWS Vietnam Office (36th Floor Bitexco)</i></p>

---

> **Summary:** The AWS Agentic AI Workshop on August 02, 2026, provided actionable engineering patterns for production AI Agents, empowering me to master Amazon Bedrock AgentCore, MCP protocols, and enterprise cloud security.
