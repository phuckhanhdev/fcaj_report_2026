from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.engagement import SimpleEmailServiceSes
from diagrams.aws.integration import Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.aws.mobile import Amplify
from diagrams.aws.ml import Bedrock
from diagrams.aws.network import CloudFront, Route53
from diagrams.aws.security import SecretsManager, WAF
from diagrams.aws.storage import S3
from diagrams.onprem.client import User
from diagrams.saas.chat import Slack

# Graph configuration
graph_attr = {
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.5",
}

with Diagram(
    "LifeSync AI Calendar Architecture",
    show=False,
    direction="LR",
    filename="architecture_diagram",
    outformat="png",
    graph_attr=graph_attr,
):
    # Layer 1: Edge, CDN & Security
    with Cluster("Layer 1: Edge, CDN & Security"):
        user = User("User Browser")
        route53 = Route53("Route 53")
        waf = WAF("AWS WAF")
        cdn = CloudFront("CloudFront CDN")

    # Layer 2: Ingress & Compute
    with Cluster("Layer 2: Ingress & Compute"):
        amplify = Amplify("Amplify Hosting")

    # Layer 3: Database & Caching
    with Cluster("Layer 3: Database & Caching"):
        rds = RDS("RDS MySQL")

    # Layer 4: Storage & Files
    with Cluster("Layer 4: Storage & Files"):
        s3 = S3("S3 Storage")

    # Layer 5: Queue, Async & Cron
    with Cluster("Layer 5: Queue, Async & Cron"):
        eventbridge = Eventbridge("EventBridge Scheduler")
        worker = Lambda("Lambda Daily Worker")

    # Layer 6: Security, Auth & Monitoring
    with Cluster("Layer 6: Security, Auth & Monitoring"):
        secrets = SecretsManager("Secrets Manager")
        cloudwatch = Cloudwatch("CloudWatch Logs")

    # Layer 7: Third-party Integrations & Failovers
    with Cluster("Layer 7: External Integrations & Failovers"):
        bedrock = Bedrock("AWS Bedrock")
        gemini = Slack("Gemini API")
        ses = SimpleEmailServiceSes("Amazon SES")
        gmail = Slack("Google SMTP")

    # Data flow steps
    user >> Edge(label="1. User Request") >> route53
    user >> Edge(label="2. HTTPS Request") >> waf
    waf >> Edge(label="3. Clean Traffic") >> cdn
    cdn >> Edge(label="4. Forward SSR & API") >> amplify

    amplify >> Edge(label="5. Fetch Secrets") >> secrets
    amplify >> Edge(label="6. SQL Queries (CRUD)") >> rds
    amplify >> Edge(label="7. Generate Presigned URL") >> s3
    user >> Edge(label="8. Direct File Upload") >> s3

    amplify >> Edge(label="9a. Primary AI NLP") >> bedrock
    amplify >> Edge(style="dashed", label="9b. Fallback to Gemini") >> gemini

    amplify >> Edge(label="10a. Primary Email OTP") >> ses
    amplify >> Edge(style="dashed", label="10b. SES Fallback") >> gmail
    gmail >> Edge(label="11. Deliver Email") >> user

    eventbridge >> Edge(label="12. Daily Trigger (07:00 AM)") >> worker
    worker >> Edge(label="13. Query Today's Events") >> rds
    worker >> Edge(label="14. Dispatch Daily Schedule Email") >> gmail

    amplify >> Edge(style="dotted", label="System Logs") >> cloudwatch
    worker >> Edge(style="dotted", label="Worker Logs") >> cloudwatch