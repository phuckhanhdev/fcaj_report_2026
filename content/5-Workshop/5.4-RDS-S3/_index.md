---
title: "Setup Amazon RDS & S3"
date: 2026-07-31
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

## Setup Amazon RDS & Amazon S3

In this section, you will set up **Amazon RDS MySQL** as the application database and **Amazon S3** for user avatar image storage.

---

## Part A: Amazon RDS MySQL

Amazon RDS (Relational Database Service) provides a managed MySQL 8.0 database for LifeSync AI Calendar. It stores all user accounts, calendar events, AI chat history, and CGV cinema scheduling data.

### Step 1: Create RDS MySQL Instance

1. Go to **AWS Console** → Search **RDS** → Click **Create database**

2. Configure:
   - **Choose a database creation method**: Standard create
   - **Engine type**: MySQL
   - **Engine Version**: MySQL 8.0.x
   - **Templates**: Free tier
   - **DB instance identifier**: `lifesync-calendar`
   - **Master username**: `admin`
   - **Master password**: Create a strong password and save it securely

3. **DB Instance Class**: `db.t2.micro` (Free Tier)

4. **Storage**: 20 GiB gp2 (Free Tier), disable auto-scaling

### Step 2: Configure Connectivity

5. **VPC**: Default VPC
6. **Public access**: **Yes** (Required for EC2 to connect via endpoint hostname)
7. **VPC Security group**: Create new
   - Security group name: `lifesync-rds-sg`

8. **Additional configuration** → **Initial database name**: `lifesync_db`

9. Click **Create database** → Wait 5–10 minutes for the instance to be available

### Step 3: Configure RDS Security Group

10. Go to the new security group `lifesync-rds-sg` → **Inbound rules** → **Edit inbound rules**

11. Add a rule:
    - **Type**: MySQL/Aurora
    - **Port**: 3306
    - **Source**: Custom → Select the Security Group of your EC2 instance (`LifeSync-Server`)

    > This allows only your EC2 instance to connect to the database — blocking all public internet access to MySQL.

### Step 4: Get the RDS Endpoint

12. Go back to the RDS instance → Copy the **Endpoint** (e.g., `lifesync-calendar.xxxxxxxx.ap-southeast-2.rds.amazonaws.com`)

13. Update your `.env.local` on EC2:
    ```bash
    RDS_HOST=lifesync-calendar.xxxxxxxx.ap-southeast-2.rds.amazonaws.com
    RDS_USER=admin
    RDS_PASSWORD=<your-password>
    RDS_DATABASE=lifesync_db
    ```

### Step 5: Run Database Schema Migration

14. SSH into EC2 and run the migration script:
    ```bash
    cd /home/ubuntu/ai_calendar_fcaj
    node src/database/migrate.js
    ```

    This creates the following core tables:
    - `USER`: `User_ID`, `Email`, `Name`, `Gender`, `Latitude`, `Longitude`, `Avatar_Url`, `Zodiac_Sign`
    - `EVENT`: `Event_ID`, `User_ID`, `Title`, `Start_Time`, `End_Time`, `Category`, `Color`
    - `AI_CHAT_HISTORY`: `Chat_ID`, `User_ID`, `Role`, `Content`, `Created_At`
    - `CGV_MOVIE`: `Movie_ID`, `Title`, `Duration_Minutes`, `Genre`, `Showtimes_Json`
    - `FRIEND_INVITE`: `Invite_ID`, `From_User_ID`, `To_User_ID`, `Status`

---

## Part B: Amazon S3

Amazon S3 stores user avatar image files. The application uses **Presigned URLs** to allow direct browser-to-S3 upload without routing through the EC2 server.

### Step 1: Create S3 Bucket

1. Go to **AWS Console** → Search **S3** → Click **Create bucket**

2. Configure:
   - **Bucket name**: `lifesync-avatar-bucket`
   - **AWS Region**: `ap-southeast-2`
   - **Block all public access**: **Uncheck** "Block all public access" → Acknowledge

3. Click **Create bucket**

### Step 2: Configure CORS Policy

4. Go into the bucket → **Permissions** tab → **Cross-origin resource sharing (CORS)**

5. Click **Edit** and paste:
   ```json
   [
     {
       "AllowedHeaders": ["*"],
       "AllowedMethods": ["PUT", "GET"],
       "AllowedOrigins": ["https://phuckhanh.id.vn", "http://localhost:3000"],
       "ExposeHeaders": ["ETag"]
     }
   ]
   ```

6. Click **Save changes**

### Step 3: Configure Bucket Policy (Public Read for Avatars)

7. Still in **Permissions** tab → **Bucket policy** → **Edit**:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::lifesync-avatar-bucket/*"
       }
     ]
   }
   ```

8. Click **Save changes**

### Step 4: How Presigned URL Upload Works

The avatar upload flow is:
1. Browser calls `/api/upload/presign` (Next.js API Route on EC2)
2. EC2 server generates a **Presigned URL** valid for 60 seconds using the IAM user credentials
3. Browser uploads the file **directly to S3** using the Presigned URL (no data passes through EC2)
4. The S3 public URL is saved to `USER.Avatar_Url` in RDS MySQL

---

### ✅ RDS & S3 Setup Complete

- **Amazon RDS MySQL** is running at endpoint `lifesync-calendar.xxxxxxxx.ap-southeast-2.rds.amazonaws.com`
- **Amazon S3** bucket `lifesync-avatar-bucket` is ready with CORS and public read access for avatars
- Schema migration has created all required database tables

**Next**: [Setup Amazon CloudFront →](../5.5-CloudFront/)
