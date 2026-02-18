import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Profile, Skill, Project, ContactMessage

def populate():
    # Clear existing if they look like placeholders or just clear all for a fresh start
    print("Cleaning database...")
    Profile.objects.all().delete()
    Skill.objects.all().delete()
    Project.objects.all().delete()
    ContactMessage.objects.all().delete()

    print("Populating database...")
    # Profile
    Profile.objects.create(
        name="Tarun Kumar Genji",
        branch="Computer Science Engineering",
        university="Andhra University",
        email="tarunkumargenji@gmail.com",
        phone_number="919494959711",
        summary="A dedicated Software Engineer specializing in building robust and scalable web applications using Python and Django. Passionate about clean code, performance optimization, and creating intuitive user experiences."
    )
    print("Profile created")
    
    # Skills
    skills = ["Python", "Django", "JavaScript", "HTML5/CSS3", "Bootstrap 5", "React", "PostgreSQL", "Git", "REST APIs", "Docker"]
    for s in skills:
        Skill.objects.create(skill_name=s)
    print(f"{len(skills)} skills created")

    # Projects
    Project.objects.create(
        title="AI-Powered Portfolio",
        description="A modern portfolio website featuring dynamic animations, glassmorphism design, and a Django backend with WhatsApp integration.",
        technologies="Django, Bootstrap 5, AOS Animation, SQLite",
        github_link="https://github.com/genjitarunkumar/genji-portfolio",
        live_link="https://genji-portfolio.herokuapp.com"
    )
    Project.objects.create(
        title="EcoTrack - Sustainability App",
        description="A mobile-responsive web application that helps users track their carbon footprint and suggests sustainable alternatives for daily activities.",
        technologies="React, Node.js, MongoDB, Chart.js",
        github_link="https://github.com/genjitarunkumar/ecotrack",
        live_link="https://ecotrack.example.com"
    )
    Project.objects.create(
        title="CloudScale - Infrastructure Manager",
        description="A dashboard for monitoring and managing multi-cloud infrastructure, providing real-time alerts and resource optimization suggestions.",
        technologies="Python, Flask, AWS SDK, Vue.js",
        github_link="https://github.com/genjitarunkumar/cloudscale",
        live_link="https://cloudscale.example.com"
    )
    print("3 projects created")

if __name__ == '__main__':
    populate()
