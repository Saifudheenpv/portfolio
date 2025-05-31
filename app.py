from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Projects data
projects = [
    {
        "name": "Portfolio Website with CI/CD",
        "description": "A modern portfolio website with automated CI/CD pipeline using GitHub Actions and Render deployment",
        "technologies": ["Python", "Flask", "GitHub Actions", "Docker", "Render"],
        "image": "portfolio.jpg",
        "github": "https://github.com/Saifudheenpv/portfolio",
        "live": "https://portfolio-wd3b.onrender.com"
    },
    {
        "name": "DevOps Pipeline Automation",
        "description": "Automated CI/CD pipeline implementation with GitHub Actions, Docker containerization, and cloud deployment",
        "technologies": ["GitHub Actions", "Docker", "Python", "AWS", "Jenkins"],
        "image": "cicd.jpg",
        "github": "https://github.com/Saifudheenpv/flask-ci-cd",
        "live": "https://flask-ci-cd.onrender.com"
    }
]

# Skills data
skills = {
    "DevOps Tools": ["Docker", "Kubernetes", "Jenkins", "GitHub Actions", "GitLab CI"],
    "Cloud Platforms": ["AWS", "Azure", "Google Cloud", "DigitalOcean"],
    "Programming": ["Python", "Shell Scripting", "JavaScript", "HTML/CSS"],
    "Infrastructure": ["Terraform", "Ansible", "Puppet", "Chef"],
    "Monitoring": ["Prometheus", "Grafana", "ELK Stack", "Nagios"]
}

@app.route('/')
def home():
    return render_template('index.html', projects=projects, skills=skills)

@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)