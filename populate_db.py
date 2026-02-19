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
        university="Lovely Professional University",
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
        title="Market Price Dashboard",
        description="A comprehensive dashboard tracking commodity prices across Indian markets, providing real-time insights into state and district-wise price trends with minimal, maximal, and modal price records.",
        technologies="Python, Django, Data Visualization, SQLite",
        github_link="https://github.com/genjitarunkumar/DASHBOARD",
        live_link=""
    )
    Project.objects.create(
        title="Django CI/CD Pipeline",
        description="Implementation of a robust Continuous Integration and Continuous Deployment pipeline for Django applications, ensuring seamless code delivery using GitHub Actions and Docker.",
        technologies="Django, GitHub Actions, Docker, CI/CD",
        github_link="https://github.com/genjitarunkumar/DJANGO_CICD.",
        live_link=""
    )
    Project.objects.create(
        title="AI Chatbot",
        description="An intelligent chatbot application designed to provide interactive responses and assist users with their queries effectively, utilizing modern NLP techniques.",
        technologies="Python, NLP, Django, REST API",
        github_link="https://github.com/genjitarunkumar/Chatbot",
        live_link=""
    )
    Project.objects.create(
        title="Django To-Do Application",
        description="A feature-rich task management application built with Django, featuring user authentication, task categorization, and an intuitive user interface.",
        technologies="Django, Bootstrap 5, SQLite, Authentication",
        github_link="https://github.com/genjitarunkumar/django-to---do-list-",
        live_link=""
    )
    print("4 projects created")

if __name__ == '__main__':
    populate()
