from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Projects data
projects = [
    {
        "name": "Portfolio Website",
        "description": "A modern, responsive portfolio built with Flask and modern CSS, featuring smooth animations and dark mode support",
        "technologies": ["Python", "Flask", "HTML5", "CSS3", "JavaScript"],
        "image": "portfolio.jpg",
        "github": "https://github.com/Saifudheenpv/portfolio",
        "live": "https://your-portfolio.onrender.com"
    },
    {
        "name": "CI/CD Pipeline",
        "description": "Automated deployment pipeline using GitHub Actions and Render, implementing continuous integration and deployment",
        "technologies": ["GitHub Actions", "Python", "Docker", "Render"],
        "image": "cicd.jpg",
        "github": "https://github.com/Saifudheenpv/portfolio",
        "live": "https://your-portfolio.onrender.com"
    }
]

# Skills data
skills = {
    "languages": ["Python", "JavaScript", "HTML5", "CSS3", "Shell Scripting"],
    "frameworks": ["Flask", "Django", "React", "Bootstrap"],
    "tools": ["Git", "GitHub", "VS Code", "Docker", "Jenkins"],
    "cloud": ["AWS", "Azure", "Google Cloud"],
    "databases": ["SQLite", "MongoDB", "PostgreSQL"]
}

@app.route('/')
def home():
    return render_template('index.html', projects=projects, skills=skills)

@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)