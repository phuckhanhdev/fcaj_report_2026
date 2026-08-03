# FCAJ 2026 Internship Report & Portfolio Site

> **First Cloud AI Journey (FCAJ 2026)** — Amazon Web Services Vietnam Co., Ltd.  
> **Student:** Nguyen Phuc Khanh (Nguyễn Phúc Khánh)  
> **Major:** Computer Engineering — Ho Chi Minh City University of Technology (VNU-HCM)  
> **Internship Period:** June 15, 2026 – July 31, 2026 (8-Week Program)  
> **Live Production App:** [https://phuckhanh.id.vn](https://phuckhanh.id.vn)

---

## 📌 About This Repository

This repository contains the complete, bilingual (English & Vietnamese) Hugo documentation site and automated LaTeX PDF report generator for the **First Cloud AI Journey (FCAJ 2026)** internship program at **AWS Vietnam**.

The portfolio showcases the end-to-end development, cloud architecture design, security hardening, and deployment of **LifeSync AI Calendar** — a scientific AI-powered smart scheduling platform built with Next.js 16, Amazon EC2, Amazon RDS MySQL, Amazon S3, Amazon CloudFront CDN, AWS WAF, AWS Lambda, Amazon EventBridge, and Google Gemini 2.5 Flash.

---

## 📚 Portfolio Structure

```
content/
├── 1-Worklog/                 # 8-Week detailed journal (On-site schedules, incidents & resolutions)
├── 2-Proposal/                # LifeSync AI Calendar project blueprint & AWS architecture
├── 3-BlogsPosted/             # 4 In-depth technical articles (Bedrock, DevOps Agent, CloudWatch)
│   ├── 3.1-Blog1/             # Amazon Bedrock vs Amazon SageMaker
│   ├── 3.2-Blog2/             # Automated CI/CD Troubleshooting with AWS DevOps Agent
│   ├── 3.3-Blog3/             # Optimizing CloudWatch Alarms (3-Right Framework)
│   └── 3.4-Blog4/             # Protecting Sensitive Log Data with CloudWatch Data Protection
├── 4-EventParticipated/       # 4 Major technical seminars & hackathons
│   ├── 4.1-Event1/            # Swinburne Cloud Mastery (04/07/2026)
│   ├── 4.2-Event2/            # GenAI-powered App-DB Modernization Workshop (27/06/2026)
│   ├── 4.3-Event3/            # AABW - AWS AI Build Week Workshop (25/07/2026)
│   └── 4.4-Event4/            # Swinburne Cloud Mastery Roundup
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

## ⚡ Automated Environment Setup

One-click scripts are provided to install all prerequisites (Hugo Extended, Pandoc, LaTeX, Python 3 & PyYAML):

- **macOS Users:**
  ```bash
  ./setup_mac.sh
  ```
- **Windows Users:**
  Double-click `setup_win.bat` or run:
  ```cmd
  setup_win.bat
  ```
- **Python Dependencies Only:**
  ```bash
  pip install -r requirements.txt
  ```

---

## 🚀 Local Development & PDF Compilation

### 1. Running Hugo Site Locally

```bash
hugo server -D
```
- English Site: `http://localhost:1313/`
- Vietnamese Site: `http://localhost:1313/vi/`

### 2. Generating LaTeX Content & Compiling PDFs

```bash
# Convert Markdown content to LaTeX format
python3 scripts/convert_hugo_to_latex.py

# Compile Vietnamese and English PDF reports
cd report
latexmk -pdf -g main.tex
latexmk -pdf -g main_en.tex
```

---

## 🤖 CI/CD & Automated GitHub Releases

Upon pushing commits to the `main` branch, the [GitHub Actions Workflow](.github/workflows/hugo.yml) automatically:

1. Builds and deploys the Hugo site to **GitHub Pages**.
2. Runs `convert_hugo_to_latex.py` and compiles both **Vietnamese (`report_vn.pdf`)** and **English (`report_en.pdf`)** reports using TeX Live.
3. Automatically publishes/updates a **GitHub Release (Tag: `latest`)** containing `report_vn.pdf`, `report_en.pdf`, and `latex_source.zip`.

---

## 🛠️ Key Technologies & Theme

- **SSG Engine:** Hugo Extended
- **Theme:** Hugo Learn Theme (Customized for FCAJ AWS Reports)
- **Deployment:** Static Hosting (GitHub Pages / AWS Amplify / CloudFront)
- **Document Pipeline:** Markdown ➔ Pandoc ➔ LaTeX ➔ PDF via `latexmk`
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
