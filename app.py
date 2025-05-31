from flask import Flask, render_template

app = Flask(__name__)

# Sample projects data
projects = [
    {
        "name": "Portfolio Website",
        "description": "A responsive portfolio built with Flask and HTML/CSS"
    },
    {
        "name": "CI/CD Pipeline",
        "description": "Automated deployment pipeline using GitHub Actions"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)