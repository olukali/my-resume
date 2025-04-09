from flask import Flask, render_template, send_file

import os

from io import BytesIO

from reportlab.lib.pagesizes import letter

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from reportlab.lib.styles import getSampleStyleSheet



app = Flask(__name__)



@app.route('/')

def home():

    return render_template('index.html')



@app.route('/download-pdf')

def download_pdf():

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)

    styles = getSampleStyleSheet()

    story = []



    # Updated resume content for PDF

    story.append(Paragraph("John Doe", styles['Title']))

    story.append(Paragraph("DevOps Engineer", styles['Heading2']))

    story.append(Paragraph("john.doe@example.com", styles['Normal']))

    story.append(Paragraph("Total Experience: 8+ Years", styles['Normal']))

    story.append(Spacer(1, 12))



    story.append(Paragraph("Professional Summary", styles['Heading2']))

    story.append(Paragraph("Experienced DevOps Engineer with over 8 years in automating, optimizing, and managing cloud infrastructure. Proficient in Docker, Kubernetes, AWS, Terraform, and bash scripting, with a proven track record of implementing CI/CD pipelines and container orchestration. Skilled in Linux server administration and infrastructure as code, delivering scalable and secure solutions.", styles['Normal']))

    story.append(Spacer(1, 12))



    story.append(Paragraph("Education", styles['Heading2']))

    story.append(Paragraph("B.S. in Computer Science - University of Tech City (2011-2015)", styles['Normal']))

    story.append(Paragraph("Certified Kubernetes Administrator (CKA) - Linux Foundation (2019)", styles['Normal']))

    story.append(Paragraph("AWS Certified Solutions Architect - Amazon Web Services (2020)", styles['Normal']))

    story.append(Spacer(1, 12))



    story.append(Paragraph("Skills", styles['Heading2']))

    story.append(Paragraph("• Docker • Kubernetes • AWS • CI/CD • Linux • Terraform • Bash", styles['Normal']))

    story.append(Spacer(1, 12))



    story.append(Paragraph("Experience", styles['Heading2']))

    story.append(Paragraph("Nexlify Tech - DevOps Engineer (2021-Present)", styles['Normal']))

    story.append(Paragraph("• Automated deployments using Jenkins and Docker for microservices", styles['Normal']))

    story.append(Paragraph("• Wrote Terraform scripts to provision AWS infrastructure", styles['Normal']))

    story.append(Paragraph("• Managed Kubernetes clusters for microservices", styles['Normal']))

    story.append(Paragraph("• Developed bash scripts for log rotation on Linux servers", styles['Normal']))

    story.append(Paragraph("• Configured AWS ECS for container orchestration", styles['Normal']))

    story.append(Paragraph("• Implemented CI/CD pipelines with GitHub Actions", styles['Normal']))

    story.append(Paragraph("• Optimized AWS costs using Terraform modules", styles['Normal']))

    story.append(Paragraph("• Monitored systems with Prometheus and Grafana", styles['Normal']))

    story.append(Paragraph("• Secured Linux servers with custom bash scripts", styles['Normal']))

    story.append(Paragraph("• Migrated on-prem apps to AWS using Docker", styles['Normal']))

    story.append(Paragraph("• Automated backups with AWS S3 and bash", styles['Normal']))

    story.append(Paragraph("• Used Terraform to manage VPC and subnets", styles['Normal']))

    story.append(Paragraph("• Deployed applications on EKS using Helm", styles['Normal']))

    story.append(Paragraph("• Created bash scripts for system health checks", styles['Normal']))

    story.append(Paragraph("• Managed IAM roles with Terraform for security", styles['Normal']))

    story.append(Paragraph("• Set up AWS Lambda functions for automation", styles['Normal']))

    story.append(Spacer(1, 12))



    story.append(Paragraph("CloudWave Solutions - Cloud Engineer (2018-2021)", styles['Normal']))

    story.append(Paragraph("• Designed AWS architecture for scalable apps", styles['Normal']))

    story.append(Paragraph("• Used Terraform to deploy EC2 instances", styles['Normal']))

    story.append(Paragraph("• Wrote bash scripts for automated server setup", styles['Normal']))

    story.append(Paragraph("• Managed Docker containers on AWS ECS", styles['Normal']))

    story.append(Paragraph("• Configured AWS CloudWatch for monitoring", styles['Normal']))

    story.append(Paragraph("• Automated S3 bucket creation with Terraform", styles['Normal']))

    story.append(Paragraph("• Hardened Linux servers for security compliance", styles['Normal']))

    story.append(Paragraph("• Created bash scripts for backup automation", styles['Normal']))

    story.append(Paragraph("• Set up AWS RDS with Terraform for databases", styles['Normal']))

    story.append(Paragraph("• Migrated legacy apps to Docker containers", styles['Normal']))

    story.append(Paragraph("• Used AWS CLI with bash for automation", styles['Normal']))

    story.append(Paragraph("• Configured VPC peering with Terraform", styles['Normal']))

    story.append(Paragraph("• Monitored Linux servers with custom scripts", styles['Normal']))

    story.append(Paragraph("• Deployed static sites on S3 with Terraform", styles['Normal']))

    story.append(Paragraph("• Managed AWS Auto Scaling for high availability", styles['Normal']))

    story.append(Paragraph("• Optimized EC2 performance with bash scripts", styles['Normal']))

    story.append(Spacer(1, 12))



    story.append(Paragraph("SysCore Innovations - System Administrator (2015-2018)", styles['Normal']))

    story.append(Paragraph("• Managed Linux servers for internal apps", styles['Normal']))

    story.append(Paragraph("• Wrote bash scripts for user management", styles['Normal']))

    story.append(Paragraph("• Automated backups with cron and bash", styles['Normal']))

    story.append(Paragraph("• Configured Apache on Linux for web hosting", styles['Normal']))

    story.append(Paragraph("• Monitored server performance with bash scripts", styles['Normal']))

    story.append(Paragraph("• Set up NFS for shared storage on Linux", styles['Normal']))

    story.append(Paragraph("• Managed user permissions with bash scripts", styles['Normal']))

    story.append(Paragraph("• Deployed Docker for internal tools", styles['Normal']))

    story.append(Paragraph("• Created bash scripts for log analysis", styles['Normal']))

    story.append(Paragraph("• Hardened Linux servers with security patches", styles['Normal']))

    story.append(Paragraph("• Automated system updates with bash", styles['Normal']))

    story.append(Paragraph("• Configured SSH for secure access", styles['Normal']))

    story.append(Paragraph("• Monitored disk usage with custom scripts", styles['Normal']))

    story.append(Paragraph("• Set up LAMP stack on Linux servers", styles['Normal']))

    story.append(Paragraph("• Managed cron jobs for scheduled tasks", styles['Normal']))

    story.append(Paragraph("• Optimized server performance with bash", styles['Normal']))

    story.append(Spacer(1, 12))



    story.append(Paragraph("Projects", styles['Heading2']))

    story.append(Paragraph("CI/CD Pipeline: Built automated deployment system using Jenkins, Docker, and bash scripts for zero-downtime deployments", styles['Normal']))

    story.append(Paragraph("Container Orchestration: Implemented Kubernetes clusters on AWS EKS with Terraform, automated scaling with bash scripts", styles['Normal']))

    story.append(Paragraph("Infrastructure Automation: Used Terraform to provision AWS resources, wrote bash scripts for Linux server configuration", styles['Normal']))



    doc.build(story)

    buffer.seek(0)

    

    return send_file(buffer, as_attachment=True, download_name='resume.pdf', mimetype='application/pdf')



if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)
