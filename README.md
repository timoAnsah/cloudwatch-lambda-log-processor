# CloudWatch Logs + AWS Lambda Log Processor

## Overview

This project demonstrates how to use AWS Lambda to process real-time logs from Amazon CloudWatch Logs. The Lambda function decodes, filters, and prints log data automatically. This simulates a basic serverless monitoring pipeline.

## Purpose & Motivation

I created this project to:
- Practice real-world AWS serverless architecture
- Understand how CloudWatch Logs can trigger Lambda
- Build DevOps/Cloud Engineering portfolio with event-driven solutions

## AWS Services Used

- Amazon CloudWatch Logs
- AWS Lambda
- AWS IAM (execution role)

## Architecture

CloudWatch Log Group
│
▼
Subscription Filter
│
▼
AWS Lambda
(processes logs)


## 📁 Folder Structure

cloudwatch-lambda-log-processor/
- README.md
- lambda/
- process_logs.py
- cloudformation/
- cloudwatch-log-subscription.yaml
- screenshots/


## Portfolio Highlights

This project demonstrates:
- Cloud-native log processing
- Event-driven AWS architecture
- Lambda scripting and IAM configuration

---
