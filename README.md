# FCAJ 2026 Internship Report & Portfolio Site

> **First Cloud AI Journey (FCAJ 2026)** — Amazon Web Services Vietnam Co., Ltd.  
> **Student:** Nguyen Phuc Khanh (Nguyễn Phúc Khánh)  
> **Major:** Computer Engineering — Ho Chi Minh City University of Technology (VNU-HCM)  
> **Internship Period:** June 15, 2026 – August 15, 2026  
> **Live Production App:** [https://phuckhanh.id.vn](https://phuckhanh.id.vn)

---

## 📌 About This Repository

This repository contains the complete, bilingual (English & Vietnamese) Hugo documentation site for the **First Cloud AI Journey (FCAJ 2026)** internship program at **AWS Vietnam**.

The portfolio showcases the end-to-end development, cloud architecture design, security hardening, and deployment of **LifeSync AI Calendar** — a scientific AI-powered smart scheduling platform built with Next.js 16, Amazon EC2, Amazon RDS MySQL, Amazon S3, Amazon CloudFront CDN, AWS WAF, AWS Lambda, Amazon EventBridge, and Google Gemini 2.5 Flash.

---

## 📚 Portfolio Structure

```
content/
├── 1-Worklog/                 # 12-Week detailed journal (On-site schedules, incidents & resolutions)
├── 2-Proposal/                # LifeSync AI Calendar project blueprint & AWS architecture
├── 3-BlogsPosted/             # 4 In-depth technical articles (Bedrock, DevOps Agent, CloudWatch)
│   ├── 3.1-Blog1/             # Amazon Bedrock vs Amazon SageMaker
│   ├── 3.2-Blog2/             # Automated CI/CD Troubleshooting with AWS DevOps Agent
│   ├── 3.3-Blog3/             # Optimizing CloudWatch Alarms (3-Right Framework)
│   └── 3.4-Blog4/             # Protecting Sensitive Log Data with CloudWatch Data Protection
├── 4-EventParticipated/       # 3 Major technical seminars & hackathons
│   ├── 4.1-Event1/            # Swinburne Cloud Mastery (04/07/2026)
│   ├── 4.2-Event2/            # GenAI-powered App-DB Modernization Workshop (27/06/2026)
│   └── 4.3-Event3/            # AABW - AWS AI Build Week Workshop (25/07/2026)
├── 5-Workshop/                # 9-Step AWS Production Deployment Workshop
│   ├── 5.1-Workshop-overview/ # Architecture & scope overview
│   ├── 5.2-Prerequiste/       # Tools, IAM & environment setup
│   ├── 5.3-EC2/               # EC2, Nginx, PM2 & GitHub Actions CI/CD
│   ├── 5.4-RDS-S3/            # RDS MySQL & S3 Presigned URL avatar storage
│   ├── 5.5-CloudFront/        # Global CDN distribution & HTTPS redirection
│   ├── 5.6-WAF/               # Web ACL, Core Rules & SQL Injection protection
│   ├── 5.7-Lambda-EventBridge/# CGV cinema crawler & weekly EventBridge cron
│   ├── 5.8-OtherServices/     # Custom domain, Certbot SSL, Gemini AI & NextAuth
│   └── 5.9-Cleanup/           # Safe resource teardown order & cost table
├── 6-Self-evaluation/         # Performance self-assessment & acquired cloud engineering skills
└── 7-Feedback/                # Insights on interning at AWS Vietnam & program feedback
```

---

## 🚀 Local Development Setup

### Prerequisites

- [Hugo Extended](https://gohugo.io/) (v0.150.0 or higher recommended)
- [Git](https://git-scm.com/)

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/phuckhanh/fcaj_report_2026.git
   cd fcaj_report_2026
   ```

2. Start the local Hugo server:
   ```bash
   hugo server -D
   ```

3. Open your browser and navigate to:
   - English Site: `http://localhost:1313/`
   - Vietnamese Site: `http://localhost:1313/vi/`

### Building Production Site

To generate static files in the `public/` directory for deployment:
```bash
hugo --minify
```

---

## 🛠️ Key Technologies & Theme

- **SSG Engine:** Hugo v0.163.1 Extended
- **Theme:** Hugo Learn Theme (Customized for FCAJ AWS Reports)
- **Deployment:** Static Hosting (GitHub Pages / AWS Amplify / CloudFront)
- **Languages:** Dual-language support (English `en` & Vietnamese `vi`)

---

## 👤 Author Information

- **Student:** Nguyễn Phúc Khánh (Nguyen Phuc Khanh)
- **Email:** phuckhanhbusiness@gmail.com
- **Phone:** +84 949.191.399
- **University:** Ho Chi Minh City University of Technology (VNU-HCM)
- **Major:** Computer Engineering (Class MT23KTM1)
- **Company:** Amazon Web Services Vietnam Company Limited (AWS Vietnam)
- **Bootcamp:** Workforce Bootcamp — First Cloud AI Journey (FCAJ 2026)
