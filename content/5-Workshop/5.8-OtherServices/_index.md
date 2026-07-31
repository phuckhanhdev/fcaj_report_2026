---
title: "Other Services Setup"
date: 2026-07-31
weight: 8
chapter: false
pre: " <b> 5.8. </b> "
---

## Other Services Setup

This section covers the setup of non-AWS services that are required for LifeSync AI Calendar to function in production. These services work alongside the AWS infrastructure set up in previous sections.

---

## 1. Custom Domain with Mắt Bão (Vietnamese Domain Provider)

Mắt Bão (`matbao.net`) is the domain registrar used for `phuckhanh.id.vn`. Configure DNS to route traffic to the CloudFront distribution.

### Setup Steps

1. Log in to [id.matbao.net](https://id.matbao.net) → Select domain management for `phuckhanh.id.vn`

2. Go to **DNS Management** → Add 2 **CNAME Records** pointing to CloudFront:

   | Host | Type | Value | TTL |
   |---|---|---|---|
   | `@` (root) | CNAME | `dbpvljmyvgnai.cloudfront.net` | 3600 |
   | `www` | CNAME | `dbpvljmyvgnai.cloudfront.net` | 3600 |

   > **Note**: Some providers don't support CNAME on root (`@`). In that case, use **A Records**:
   > - `@` → Type `A` → Value: your EC2 Elastic IP (`3.104.121.77`)
   > - `www` → Type `A` → Value: your EC2 Elastic IP (`3.104.121.77`)

3. Wait 5–30 minutes for DNS propagation

4. Verify DNS propagation:
   ```bash
   nslookup phuckhanh.id.vn
   # Should return CloudFront or EC2 IP
   ```

---

## 2. SSL/TLS Certificate with Let's Encrypt (Certbot)

Certbot provides **free SSL/TLS certificates** from Let's Encrypt for your domain. This enables HTTPS on your EC2 Nginx server.

### Setup Steps

1. SSH into your EC2 instance and install Certbot:
   ```bash
   sudo apt install -y certbot python3-certbot-nginx
   ```

2. Request and automatically install the certificate:
   ```bash
   sudo certbot --nginx -d phuckhanh.id.vn -d www.phuckhanh.id.vn
   ```

3. Follow the interactive prompts:
   - Enter email for renewal notifications
   - Agree to Terms of Service
   - Choose option **2** (Redirect — force HTTPS for all HTTP requests)

4. Certbot automatically:
   - Obtains the certificate from Let's Encrypt
   - Modifies the Nginx configuration to enable HTTPS on port 443
   - Sets up auto-renewal (runs twice daily via systemd timer)

5. Test certificate renewal:
   ```bash
   sudo certbot renew --dry-run
   # Should complete without errors
   ```

> **Note**: If you are using CloudFront as your CDN (recommended), you may not need Certbot on EC2 — CloudFront handles HTTPS. Certbot is only needed if users access EC2 directly without CloudFront.

---

## 3. Google Gemini AI API

LifeSync AI Calendar uses **Google Gemini 2.5 Flash** for natural language scheduling intent parsing (converting "lunch tomorrow at noon" into structured calendar event data).

### Setup Steps

1. Go to [Google AI Studio](https://aistudio.google.com/) → Sign in with Google account

2. Click **Get API key** → **Create API key** → Copy the key

3. Add to your `.env.local` on EC2:
   ```bash
   GOOGLE_AI_API_KEY=AIzaSy...your-key-here
   ```

4. Restart the application:
   ```bash
   pm2 restart lifesync
   ```

### API Features Used

| Feature | Description |
|---|---|
| **Intent Parsing** | Converts natural language → structured event JSON (title, date, time, duration) |
| **Slot Filling** | Asks follow-up questions when information is incomplete |
| **Multi-turn Chat** | Maintains conversation context for 3 days |
| **Scheduling Strategy Selection** | AI determines which scientific scheduling strategy to apply |

### Cost
- Free tier: 15 requests per minute, 1 million tokens per minute
- For production usage with real users: upgrade to paid tier at ~$0.075 per 1M tokens

---

## 4. NextAuth.js Authentication

LifeSync AI Calendar uses **NextAuth.js** (now Auth.js) for user authentication with Google OAuth 2.0.

### Setup Steps

1. Go to [Google Cloud Console](https://console.cloud.google.com/) → **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth 2.0 Client IDs**

2. Configure:
   - **Application type**: Web application
   - **Authorized redirect URIs**: `https://phuckhanh.id.vn/api/auth/callback/google`

3. Copy **Client ID** and **Client Secret**

4. Add to `.env.local`:
   ```bash
   GOOGLE_CLIENT_ID=xxxxxx.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=GOCSPX-...
   NEXTAUTH_SECRET=<random-32-char-string>
   NEXTAUTH_URL=https://phuckhanh.id.vn
   ```

---

### ✅ All Services Setup Complete

Your complete LifeSync AI Calendar production stack is now running:

| Layer | Service | Status |
|---|---|---|
| **DNS** | Mắt Bão Domain | ✅ Configured |
| **CDN** | Amazon CloudFront | ✅ Active |
| **Security** | AWS WAF | ✅ Active |
| **SSL/TLS** | Let's Encrypt / CloudFront | ✅ Active |
| **App Server** | Amazon EC2 + Nginx + PM2 | ✅ Running |
| **Database** | Amazon RDS MySQL | ✅ Running |
| **File Storage** | Amazon S3 | ✅ Active |
| **AI Engine** | Google Gemini 2.5 Flash | ✅ Connected |
| **Auth** | NextAuth.js + Google OAuth | ✅ Active |
| **Crawler** | Lambda + EventBridge | ✅ Scheduled |
| **CI/CD** | GitHub Actions | ✅ Active |

**Next**: [Clean up Resources →](../5.9-Cleanup/)
