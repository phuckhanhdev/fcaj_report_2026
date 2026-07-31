---
title: "Setup Amazon CloudFront"
date: 2026-07-31
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

## Setup Amazon CloudFront

Amazon CloudFront is a global Content Delivery Network (CDN) that sits in front of your EC2 server. It provides:
- **Faster page loads** by caching content at edge locations worldwide
- **IP masking** — hides your EC2 Elastic IP from the public internet
- **HTTPS enforcement** via AWS-managed SSL certificates
- **AWS WAF integration** — the WAF attaches directly to CloudFront (covered in Section 5.6)

---

### Step 1: Open CloudFront Console

1. Go to **AWS Console** → Search **CloudFront** → Click **Create distribution**

![CloudFront Create Distribution](images/5-Workshop/picture/cloudfront/1_setup.png)

---

### Step 2: Configure Origin

2. **Distribution type**: Select **Web** (standard web application)

3. **Origin type**: Select **Other** *(for custom domain / EC2 server)*

4. **Origin domain**: Enter your domain or Elastic IP:
   - If you have a domain: `phuckhanh.id.vn`
   - If no domain yet: `3.104.121.77` (your EC2 Elastic IP)

5. **Protocol**: HTTP only (EC2 handles HTTP, CloudFront handles HTTPS)

![CloudFront Name Configuration](images/5-Workshop/picture/cloudfront/2_name.png)

---

### Step 3: Configure Default Cache Behavior

6. **Viewer protocol policy**: `Redirect HTTP to HTTPS`
   - All HTTP requests are automatically redirected to HTTPS

7. **Allowed HTTP methods**: `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`
   - Required for Next.js Server Actions, API Routes, and form submissions

8. **Cache policy**: Select `CachingDisabled` for dynamic Next.js content
   - Or use `CachingOptimized` for static assets only

![CloudFront Origin Setup](images/5-Workshop/picture/cloudfront/3_origin%20setup.png)

---

### Step 4: Configure Settings

9. **Alternate domain names (CNAME)**: Enter your custom domains:
   - `phuckhanh.id.vn`
   - `www.phuckhanh.id.vn`

   > Skip this if you don't have a custom domain yet — you can use the CloudFront domain directly (e.g., `dbpvljmyvgnai.cloudfront.net`)

10. **Custom SSL certificate**: Request or import an AWS Certificate Manager (ACM) certificate
    - Click **Request certificate** → Enter your domain → Complete DNS validation
    - Or skip if using CloudFront domain only

11. **Default root object**: Enter `index.html` (optional for Next.js apps)

![CloudFront Final Settings](images/5-Workshop/picture/cloudfront/4_cloudFront%20settings.png)

12. Click **Create distribution** → Wait 5–10 minutes for deployment to complete

---

### Step 5: Note Your CloudFront Domain

13. After creation, copy the **Distribution domain name** (e.g., `dbpvljmyvgnai.cloudfront.net`)

    This is your new public URL. You can:
    - Access it directly: `https://dbpvljmyvgnai.cloudfront.net`
    - Or point your custom domain DNS to it (covered in Section 5.8 — Other Services)

---

### Important: CloudFront Cache Invalidation

When you deploy new code, CloudFront may still serve cached old content. To force cache refresh:

```bash
aws cloudfront create-invalidation \
  --distribution-id YOUR_DISTRIBUTION_ID \
  --paths "/*"
```

Or do it in the AWS Console: **CloudFront** → Select your distribution → **Invalidations** → **Create invalidation** → Enter `/*`

---

### ✅ CloudFront Setup Complete

Your application now has:
- A **global CDN** distribution point at `dbpvljmyvgnai.cloudfront.net`
- **Automatic HTTPS** with HTTP → HTTPS redirect
- **IP masking** — EC2 IP is not exposed publicly
- Ready for **AWS WAF** attachment in the next step

**Next**: [Setup AWS WAF →](../5.6-WAF/)
