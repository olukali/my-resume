# Flask Resume App

A modern, responsive portfolio website built with Flask, featuring a clean and professional design. This application serves as a dynamic resume/portfolio that showcases professional experience, skills, and projects in an interactive web format.

## Application Overview

### Features
- Responsive design that works on all devices
- Modern UI with smooth animations and transitions
- Print-friendly layout for PDF generation
- Progressive Web App (PWA) capabilities
- Accessibility-compliant design
- SEO-optimized structure

### Components
- `app.py`: Flask application entry point
- `templates/index.html`: Main HTML template with embedded CSS
- `static/manifest.json`: PWA manifest file
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration

### Technologies Used
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3
- **Design**: 
  - CSS Grid and Flexbox for layout
  - CSS Custom Properties for theming 
  - CSS Animations and Transitions
- **Optimization**:
  - CSS containment for performance
  - Lazy loading for images
  - Font optimization
  - Content caching
- **Development**:
  - Python virtual environment
  - Docker containerization

## Ubuntu Deployment
```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip

# Clone project directory
git clone https://github.com/kserge2001/docker-resume-app.git
cd docker-resume-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the app
export FLASK_APP=app.py
python -m flask run --host=0.0.0.0 --port=5001
```

## Alpine Linux Deployment
```bash
# Install dependencies
apk update
apk add python3 py3-pip

# Clone project directory
git clone https://github.com/kserge2001/docker-resume-app.git
cd docker-resume-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the app
export FLASK_APP=app.py
python -m flask run --host=0.0.0.0 --port=5001
```

## Red Hat Enterprise Linux Deployment
```bash
# Install dependencies
sudo dnf update
sudo dnf install python3 python3-pip

# Clone project directory
git clone https://github.com/kserge2001/docker-resume-app.git
cd docker-resume-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the app
export FLASK_APP=app.py
python -m flask run --host=0.0.0.0 --port=5001
```

## Amazon Linux 2 Deployment
```bash
# Install dependencies
sudo yum update
sudo yum install python3 python3-pip

# Clone project directory
git clone https://github.com/kserge2001/docker-resume-app.git
cd docker-resume-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the app
export FLASK_APP=app.py
python -m flask run --host=0.0.0.0 --port=5001
```

## Docker Deployment

# Dockerfile
Create a file named `Dockerfile` with the following content:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

ENV FLASK_APP=app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
```
# docker commands
```bash
# Build the Docker image
docker build -t flask-resume-app .

# Run the container
docker run -d -p 5001:5001 flask-resume-app
```
