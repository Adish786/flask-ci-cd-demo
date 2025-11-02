# Flask Application with Jenkins CI/CD Pipeline

This project demonstrates a CI/CD pipeline for a Flask application using Jenkins.

## Prerequisites

- Jenkins server with the following plugins:
  - Pipeline
  - GitHub Integration
  - Email Extension
  - JUnit
- Python 3.8+
- Git

## Setup Instructions

### 1. Jenkins Configuration

1. Install required plugins in Jenkins:
   - Pipeline
   - GitHub plugin
   - Email Extension Plugin
   - JUnit Plugin

2. Configure system settings:
   - Set up SMTP server for email notifications
   - Configure Python installation

### 2. Jenkins Job Setup

1. Create a new Pipeline job in Jenkins
2. Configure the pipeline to use "Pipeline script from SCM"
3. Set SCM to Git and provide your repository URL
4. Set branch specifier to `*/main`
5. Script path should be `Jenkinsfile`

### 3. Pipeline Stages

The pipeline consists of three main stages:

- **Build**: Creates virtual environment and installs dependencies
- **Test**: Runs unit tests using pytest
- **Deploy**: Deploys to staging environment if tests pass

### 4. Notifications

Email notifications are sent for:
- Successful builds
- Failed builds

### 5. Triggers

The pipeline automatically triggers when changes are pushed to the main branch.

## Local Development

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run application
python app.py

#Additional Details
https://www.jenkins.io/doc/book/pipeline/docker/
https://plugins.jenkins.io/slack/       // slack notification implementation
