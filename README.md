# bank-app-aws
Secure Banking Application Infrastructure on AWS

If you mean **"Secure Banking Application Infrastructure on AWS"**, you don't need to build a real banking app. Instead, create the **cloud infrastructure** that could securely host one. This is an excellent AWS + DevOps portfolio project.

## Project Architecture

```text
                     Internet
                         │
                   Route 53 (Optional)
                         │
                    Application Load Balancer
                         │
          ┌──────────────┴──────────────┐
          │                             │
      EC2 (Web Server)             EC2 (Web Server)
          │                             │
          └──────────────┬──────────────┘
                         │
                   Private Subnet
                         │
                    RDS MySQL Database
                         │
                    Amazon S3 (Backups)
                         │
             CloudWatch + SNS Monitoring
                         │
                IAM + Security Groups
```

---

# AWS Services Used

| Service                   | Purpose                        |
| ------------------------- | ------------------------------ |
| EC2                       | Web/Application Server         |
| VPC                       | Private Network                |
| Public & Private Subnets  | Security                       |
| Internet Gateway          | Internet Access                |
| NAT Gateway               | Internet for Private Instances |
| Application Load Balancer | Load Balancing                 |
| Auto Scaling              | High Availability              |
| RDS MySQL                 | Database                       |
| S3                        | Document & Backup Storage      |
| IAM                       | User Permissions               |
| CloudWatch                | Monitoring                     |
| SNS                       | Alerts                         |
| AWS Backup                | Database Backup                |
| KMS                       | Encryption                     |
| Secrets Manager           | Store DB Password              |

---

# Features

### User Login

* Login Page
* Password Authentication

---

### Account Dashboard

* Account Balance
* Transaction History
* Mini Statement

---

### Money Transfer (Dummy)

* Transfer Form
* Success Message

(No real banking API required.)

---

### Secure Storage

Store

* KYC Documents
* Bank Statements
* Profile Images

inside Amazon S3.

---

### Database

RDS MySQL Tables

```
Users

user_id
name
email
password
balance
```

```
Transactions

id
sender
receiver
amount
date
```

---

# Security Features

✅ HTTPS

Use

* AWS Certificate Manager
* Load Balancer

---

### IAM

Create

* Admin
* Developer
* Auditor

roles.

---

### Security Groups

Allow only

```
Internet
↓

ALB : 80,443

↓

EC2 : 8080

↓

RDS :3306 only from EC2
```

---

### Encryption

Enable

* S3 Encryption
* RDS Encryption
* KMS Keys

---

### Secrets Manager

Store

* Database Username
* Password

instead of hardcoding them.

---

# Monitoring

CloudWatch

Monitor

* CPU
* Memory
* Disk
* Network

SNS

Send Email Alert

```
CPU > 70%

↓

Email Notification
```

---

# High Availability

Create

* 2 Availability Zones

Deploy

```
AZ1

EC2

↓

AZ2

EC2
```

Use

* Auto Scaling
* Load Balancer

---

# DevOps Integration

GitHub

↓

Jenkins

↓

Build

↓

Docker Image

↓

Push to Docker Hub / Amazon ECR

↓

Deploy to EC2

---

# Folder Structure

```
bank-app/

├── frontend/

├── backend/

├── terraform/

├── docker/

├── jenkins/

├── nginx/

├── sql/

├── README.md
```

---

# Technologies

* HTML
* CSS
* JavaScript
* Node.js / Spring Boot / Python Flask (choose one)
* MySQL
* Docker
* Jenkins
* GitHub
* Terraform
* AWS

---

# Skills You'll Demonstrate

* AWS VPC Design
* EC2 Deployment
* IAM
* RDS
* S3
* Load Balancer
* Auto Scaling
* CloudWatch
* SNS
* Docker
* Jenkins
* Terraform
* Git
* Linux Administration
* Networking
* Cloud Security

---

## Project Flow

```text
User
   │
   ▼
Application Load Balancer
   │
   ▼
EC2 Web Server (Docker Container)
   │
   ▼
Backend API
   │
   ▼
Amazon RDS MySQL
   │
   ▼
Amazon S3 (Documents)
```

## Why this project is valuable

This project closely mirrors how many organizations design secure web application infrastructure. It demonstrates networking, security, automation, monitoring, and deployment skills that are relevant for **Cloud Engineer**, **DevOps Engineer**, and **System Administrator** roles.

If you're building this as a final-year project, I can guide you step by step—from creating the AWS VPC to deploying the application, configuring Docker and Jenkins, and automating the infrastructure with Terraform.
