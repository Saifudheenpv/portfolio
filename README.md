# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, featuring smooth animations, dark mode support, and a clean design.

## 🌟 Features

- Responsive design that works on all devices
- Dark mode support
- Smooth animations and transitions
- Project showcase section
- Skills display
- Contact information
- Modern UI with CSS animations
- SEO friendly

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render
- **Version Control**: Git, GitHub
- **CI/CD**: GitHub Actions

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Saifudheenpv/portfolio.git
   cd portfolio
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally**
   ```bash
   python app.py
   ```
   The website will be available at `http://localhost:5000`

## 📁 Project Structure

```
portfolio/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # For deployment on Render
├── static/
│   ├── css/
│   │   └── style.css  # Main stylesheet
│   ├── js/
│   │   └── main.js    # JavaScript functionality
│   └── images/        # Project images
└── templates/
    └── index.html     # Main template
```

## 🚀 Deployment

This project is deployed on Render. To deploy your own version:

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## 🎨 Customization

1. **Update Personal Information**
   - Edit `templates/index.html` to update your name, title, and about section
   - Modify contact information and social media links

2. **Add Projects**
   - Edit the `projects` list in `app.py`
   - Add project images to `static/images/`

3. **Modify Skills**
   - Update the `skills` dictionary in `app.py`

4. **Change Colors**
   - Edit CSS variables in `static/css/style.css`

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Saifudheen PV**
- GitHub: [@Saifudheenpv](https://github.com/Saifudheenpv)
- LinkedIn: [Saifudheen PV](https://linkedin.com/in/saifudheenpv)

## 🙏 Acknowledgments

- Font Awesome for icons
- Google Fonts for typography
- Unsplash for stock images 