---
title: "Setup AWS WAF"
date: 2026-07-31
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

## Setup AWS WAF (Web Application Firewall)

AWS WAF (Web Application Firewall) protects the LifeSync AI Calendar application from common web attacks. It is attached directly to the **CloudFront distribution** created in the previous step, filtering malicious traffic before it reaches the EC2 server.

**LifeSync WAF protects against:**
- **SQL Injection (SQLi)** — prevents attackers from manipulating the Amazon RDS MySQL database
- **OWASP Top 10 vulnerabilities** — common web application security risks
- **Cross-Site Scripting (XSS)** — prevents malicious scripts from being injected
- **Layer 7 DDoS** — rate limiting to block bot floods

---

### Step 1: Open AWS WAF Console

1. Go to **AWS Console** → Search **WAF & Shield** → Click **Protection packs (web ACLs)**

2. Click **Create protection pack (web ACL)**

> **Important**: Make sure the region is set to **Global (CloudFront)** in the top-right corner — WAF must be in Global scope to attach to CloudFront distributions.

![WAF Initial Setup](/images/5-Workshop/picture/waf/1_setup.png)

---

### Step 2: Describe Web ACL

3. **Tell us about your app**:
   - **App category**: `Web Application`
   - **App focus**: `Both API and web`

4. **Name and describe**:
   - **Name**: `LifeSync-WAF`
   - **Description**: `Web ACL protection for LifeSync AI Calendar`

---

### Step 3: Select Resources to Protect

5. **Select resources to protect**:
   - Click **Add CloudFront or Amplify resources**
   - Select your CloudFront distribution (`dbpvljmyvgnai.cloudfront.net`)
   - Click **Add**

![WAF Settings](/images/5-Workshop/picture/waf/2_setting.png)

---

### Step 4: Choose Protection Rules

6. **Choose initial protections**:
   - Select **`Build your own pack (You build it)`** — Estimated cost ~$7/month (most cost-effective)

7. Add the following **2 AWS Managed Rules** (click **Add rules**):

   | Rule Name | Rule Set | Protects Against |
   |---|---|---|
   | **AWSManagedRulesCommonRuleSet** | AWS Core rule set | OWASP Top 10, XSS, common exploits |
   | **AWSManagedRulesSQLiRuleSet** | SQL database | SQL Injection attacks on RDS MySQL |

8. For each rule, set **Action** to `Block`

![WAF Custom Rule Configuration](/images/5-Workshop/picture/waf/3_custom%20rule.png)

---

### Step 5: Configure Default Action

9. **Default action**: `Allow` — Allow all traffic that does not match any rules
   - The rules above will block malicious requests
   - All legitimate users will pass through normally

---

### Step 6: Review and Create

10. Review the summary:
    - **Name**: `LifeSync-WAF`
    - **Associated resources**: Your CloudFront distribution
    - **Rules**: 2 managed rules (Core + SQLi)
    - **Estimated monthly cost**: ~$7 (Web ACL $5 + 2 rules × $1)

11. Click **Create protection pack (web ACL)**

---

### Cost Breakdown

| Item | Cost |
|---|---|
| Web ACL | $5.00/month |
| AWSManagedRulesCommonRuleSet (1 rule) | $1.00/month |
| AWSManagedRulesSQLiRuleSet (1 rule) | $1.00/month |
| Request processing (< 1M/month) | ~$0.01/month |
| **Total** | **~$7.01/month** |

> All WAF costs are covered by **AWS Credits** — no out-of-pocket expense.

---

### ✅ WAF Setup Complete

Your application is now protected by:
- **AWS WAF** with Web ACL `LifeSync-WAF` attached to CloudFront
- **OWASP Top 10** protection via AWS Core Rule Set
- **SQL Injection** protection for your Amazon RDS MySQL database
- All traffic flows through: Internet → CloudFront → WAF → EC2 → RDS

**Next**: [Setup AWS Lambda & EventBridge →](../5.7-Lambda-EventBridge/)
