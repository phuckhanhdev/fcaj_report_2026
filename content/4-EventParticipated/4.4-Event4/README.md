# macOS Setup Guide — Returns & Refunds Assistant (Strands + AgentCore)

This guide walks another Kiro user through installing every dependency needed to run this workshop project on macOS (Intel or Apple Silicon). Follow the steps in order — later tools (AgentCore CLI, AWS CDK) depend on Node.js being installed first, and uv/Python tooling is independent of the Node.js stack.

Estimated time: 15–20 minutes.

---

## Prerequisites checklist

| # | Tool | Minimum version | Why it's needed |
|---|------|------------------|------------------|
| 1 | Node.js | 20+ | Runs the AgentCore CLI (`@aws/agentcore`), which is distributed as an npm package |
| 2 | Python | 3.12+ | Runs the Strands agent code and the Lambda function handlers |
| 3 | AgentCore CLI (`@aws/agentcore`) | latest | Scaffolds, tests locally (`agentcore dev`), deploys (`agentcore deploy`), and manages agents |
| 4 | AWS CDK | latest v2 | The AgentCore CLI uses CDK under the hood to provision Runtime/Gateway/Memory infrastructure |
| 5 | uv | latest | Fast Python package/dependency manager; also used to run MCP servers via `uvx` |
| 6 | AWS CLI credentials | AWS CLI v2 | Grants access to Amazon Bedrock foundation models and AgentCore control-plane APIs |

---

## 1. Install Node.js 20+

The AgentCore CLI requires Node.js 20 or later.

Recommended: install via nvm so you can switch Node versions per project without needing sudo:

```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Restart your terminal, or reload your shell profile
source ~/.zshrc   # or ~/.bash_profile depending on your shell

# Install and use Node.js 20 LTS
nvm install 20
nvm use 20
```

Alternative: Homebrew

```bash
brew install node@20
brew link node@20 --force
```

Verify:

```bash
node --version   # should print v20.x.x or later
npm --version
```

---

## 2. Install Python 3.12+

Strands agent code and the Lambda function handlers in this project require Python 3.12 or later.

Recommended: Homebrew

```bash
brew install python@3.12
```

This installs `python3.12` alongside your system Python without overwriting it. Verify:

```bash
python3.12 --version   # should print Python 3.12.x
```

Alternative: pyenv (useful if you need to juggle multiple Python versions across projects):

```bash
brew install pyenv
pyenv install 3.12
pyenv global 3.12
```

> You do not strictly need to make 3.12 your global `python3` — `uv` can manage per-project Python versions for you.

---

## 3. Install uv (Python package manager)

`uv` is used to run MCP servers (`uvx <package>`) and to manage the agent's Python dependencies (`uv sync`) declared in `pyproject.toml`.

Recommended: official standalone installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternative: Homebrew

```bash
brew install uv
```

Restart your terminal (or source your shell profile) so `uv` is on your PATH, then verify:

```bash
uv --version
```

> `uvx` ships with `uv` — no separate install needed. It is used later to run the AWS Documentation MCP server and the Strands Agents MCP server from `.kiro/settings/mcp.json`.

---

## 4. Install AWS CLI v2 and configure credentials

The AWS CLI is needed to verify identity, run diagnostic commands, and is a dependency for tools that shell out to `aws` under the hood.

Install (official pkg installer):

```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

Verify:

```bash
aws --version   # should print aws-cli/2.x.x
```

Configure credentials using the access key, secret key, and session token from the workshop event page:

```bash
export AWS_ACCESS_KEY_ID=<your-access-key>
export AWS_SECRET_ACCESS_KEY=<your-secret-key>
export AWS_SESSION_TOKEN=<your-session-token>
export AWS_DEFAULT_REGION=us-west-2
```

Verify access:

```bash
aws sts get-caller-identity --no-cli-pager
```

> Reminder: every `aws` CLI command in this project should include `--no-cli-pager` and target region us-west-2, per the project's steering rules.

---

## 5. Install the AgentCore CLI

The AgentCore CLI (`@aws/agentcore`) scaffolds, runs locally, deploys, and manages AgentCore resources (Runtime, Gateway, Memory, Identity, Harness). It is distributed as an npm package and requires Node.js 20+.

```bash
npm install -g @aws/agentcore
```

Verify:

```bash
agentcore --version
```

---

## 6. Install AWS CDK

The AgentCore CLI provisions infrastructure (Runtime, Gateway, Memory, IAM roles) through AWS CDK behind the scenes, so the CDK CLI must be available on your machine.

```bash
npm install -g aws-cdk
```

Verify:

```bash
cdk --version
```

One-time CDK bootstrap for your AWS account/region (only needs to be run once per account+region combination):

```bash
cdk bootstrap aws://<your-account-id>/us-west-2
```

> You can get `<your-account-id>` from the output of `aws sts get-caller-identity --no-cli-pager`.

---

## Verification: run all checks at once

```bash
node --version
python3.12 --version
uv --version
aws --version
agentcore --version
cdk --version
aws sts get-caller-identity --no-cli-pager
```

If every command prints a version (and the identity check returns your account/user ARN) without error, the environment is ready.

---

## Next step

Open Kiro in your project folder and continue with Lab 1 · Workshop Setup from `lab-prompts.md`:

```bash
mkdir -p ~/ReturnsRefundsAgentProject
cd ~/ReturnsRefundsAgentProject
kiro .
```
