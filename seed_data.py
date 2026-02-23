import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.contrib.auth.models import User
from accounts_app.models import Profile
from projects_app.models import Project

def seed():
    # Create Admin
    admin_user, created = User.objects.get_or_create(username='admin')
    if created:
        admin_user.set_password('adminpass123')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print("Admin user created.")

    # Create/Update Profile with CV details
    profile, created = Profile.objects.get_or_create(user=admin_user)
    profile.name = "Tarun Kumar Genji"
    profile.bio = "Computer Science & Engineering student at Lovely Professional University. Passionate about AI, Machine Learning, and Web Technologies. Experienced in building intelligent solutions like AI Chatbots and Health Monitoring Systems."
    profile.skills = "Python C++ C JavaScript HTML CSS MySQL PowerBI ML GitHub Git VSCode"
    profile.education = """Lovely Professional University - B.Tech CSE (CGPA: 6.60)
Sri Viswa Junior College - Intermediate (85.4%)
Chalapathi Public School - Matriculation (100%)"""
    profile.experience = """Internship @ Cipher Schools - Data Structures & Algorithms
Internship @ CSE Pathshala - C Programming Fundamentals
Social Networks - NPTEL Certificate
Responsive Web Design - FreeCodeCamp"""
    profile.github = "https://github.com/genjitarunkumar"
    profile.linkedin = "https://linkedin.com/in/tarun-kumar123"
    profile.twitter = "#"
    profile.phone_number = "919494959711"
    profile.save()
    print("Profile updated with CV data.")

    # Create Sample Projects from CV
    projects = [
        {
            'title': 'Agriculture AI Chat Bot',
            'slug': 'agriculture-ai-chatbot',
            'description': 'Developed an AI-powered chatbot to assist farmers with crop planning and yield estimation. Implemented ML-based logic to provide fertilizer recommendations, profit analysis, and farming insights.',
            'tech_stack': 'Python Streamlit Machine-Learning',
            'github_link': 'https://github.com/genjitarunkumar',
            'live_demo': 'https://genji-portfolio-1.onrender.com'
        },
        {
            'title': 'Pulse Monitoring System',
            'slug': 'pulse-monitoring-system',
            'description': 'Designed a health monitoring solution using biomedical sensors to measure pulse rate and vital parameters. Applied real-time signal processing and peak detection algorithms.',
            'tech_stack': 'Biomedical-Sensors Embedded-Systems Microcontrollers',
            'github_link': 'https://github.com/genjitarunkumar',
            'live_demo': 'https://genji-portfolio-1.onrender.com'
        }
    ]

    for p in projects:
        Project.objects.get_or_create(slug=p['slug'], defaults=p)
    print("Projects updated.")

if __name__ == "__main__":
    seed()
