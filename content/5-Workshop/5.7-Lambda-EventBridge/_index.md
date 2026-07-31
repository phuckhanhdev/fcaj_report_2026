---
title: "Setup Lambda & EventBridge"
date: 2026-07-31
weight: 7
chapter: false
pre: " <b> 5.7. </b> "
---

## Setup AWS Lambda & Amazon EventBridge

**AWS Lambda** and **Amazon EventBridge** work together to automate the weekly CGV cinema data crawler for LifeSync AI Calendar.

- **AWS Lambda** runs the crawler code (Node.js 20.x) to scrape CGV cinema data and update the `CGV_MOVIE` table in Amazon RDS MySQL
- **Amazon EventBridge Scheduler** triggers the Lambda function every **Monday at 00:00 AM (Vietnam time / UTC+7)**

---

## Part A: AWS Lambda — CGV Movie Crawler Function

### Step 1: Create Lambda Function

1. Go to **AWS Console** → Search **Lambda** → Click **Create function**

2. Configure:
   - **Author from scratch**
   - **Function name**: `cgv-movie-crawler`
   - **Runtime**: Node.js 20.x
   - **Architecture**: x86_64
   - **Execution role**: Create a new role with basic Lambda permissions

3. Click **Create function**

![Lambda Function Setup](images/5-Workshop/picture/lambda/cgv_movie_crawler/1_setup.png)

---

### Step 2: Configure Environment Variables

4. In the Lambda function → **Configuration** tab → **Environment variables** → **Edit**

5. Add the following variables:

   | Key | Value |
   |---|---|
   | `RDS_HOST` | Your RDS endpoint hostname |
   | `RDS_USER` | `admin` |
   | `RDS_PASSWORD` | Your RDS password |
   | `RDS_DATABASE` | `lifesync_db` |

6. Click **Save**

![Lambda Environment Variables Setup](images/5-Workshop/picture/lambda/cgv_movie_crawler/2_envSetup.png)

---

### Step 3: Deploy Lambda Code

7. The crawler function fetches CGV movie and showtime data from the CGV API and upserts it into the `CGV_MOVIE` table.

8. **Option A — Direct code editor** (for simple functions):
   - Click **Code** tab → Paste your crawler code into `index.mjs`

9. **Option B — Upload ZIP package** (recommended for Node.js with `node_modules`):
   ```bash
   # On your local machine:
   mkdir cgv-crawler && cd cgv-crawler
   npm init -y
   npm install mysql2 axios
   cp /path/to/your/crawler/index.mjs .
   zip -r cgv-crawler.zip .
   ```
   - In Lambda → **Code** tab → **Upload from** → `.zip file` → Upload `cgv-crawler.zip`

10. Set the **Handler** to `index.handler`

---

### Step 4: Configure Lambda Timeout & Memory

11. In **Configuration** tab → **General configuration** → **Edit**:
    - **Memory**: `256 MB` (sufficient for the crawler)
    - **Timeout**: `5 minutes` (CGV API calls can be slow)
    - Click **Save**

---

### Step 5: Test the Lambda Function

12. Click **Test** → **Create new test event**:
    - **Event name**: `ManualCrawlTest`
    - **Event JSON**: `{}`
    - Click **Save** → Click **Test**

13. Check the execution results — successful output should show movies upserted into RDS

---

## Part B: Amazon EventBridge — Weekly Cron Scheduler

### Step 1: Create EventBridge Schedule

1. Go to **AWS Console** → Search **EventBridge** → Click **Scheduler** → **Schedules** → **Create schedule**

![EventBridge Scheduler](images/5-Workshop/picture/eventBridge/1_scheduler.png)

---

### Step 2: Configure Schedule Name & Cron

2. **Schedule name**: `cgv-weekly-crawler`

3. **Schedule pattern**: Select **Recurring schedule** → **Cron-based schedule**

4. **Cron expression**: `cron(0 17 ? * SUN *)`
   - This runs at **17:00 UTC on Sunday** = **00:00 AM Monday Vietnam time (UTC+7)**

5. **Flexible time window**: `Off` (run exactly on time)

![EventBridge Name & Config](images/5-Workshop/picture/eventBridge/2_name%26config.png)

---

### Step 3: Select Target (Lambda Function)

6. **Target**: Select **AWS Lambda** → **Invoke**

7. **Lambda function**: Select `cgv-movie-crawler`

8. **Payload**: `{}` (empty — the crawler doesn't need input)

![EventBridge Target Selected](images/5-Workshop/picture/eventBridge/3_target_selected.png)

---

### Step 4: Configure Permissions

9. **Execution role**: Select **Create new role for this schedule** — EventBridge will automatically create an IAM role with permission to invoke the Lambda function

10. Click **Next** → Review → Click **Create schedule**

![EventBridge Review](images/5-Workshop/picture/eventBridge/4_review.png)

---

### Cron Expression Reference

| Expression | Meaning |
|---|---|
| `cron(0 17 ? * SUN *)` | Every Sunday at 17:00 UTC (Monday 00:00 VN) |
| `cron(0 0 ? * MON *)` | Every Monday at 00:00 UTC |
| `cron(0 */6 * * ? *)` | Every 6 hours |

---

### ✅ Lambda & EventBridge Setup Complete

The automation pipeline is now active:
- **Every Sunday at 17:00 UTC** (Monday 00:00 AM Vietnam time), EventBridge triggers the `cgv-movie-crawler` Lambda function
- The Lambda fetches the latest CGV movie showtimes and updates the `CGV_MOVIE` table in Amazon RDS MySQL
- Users will always see up-to-date cinema schedules when planning movie outings

**Next**: [Other Services Setup →](../5.8-OtherServices/)
