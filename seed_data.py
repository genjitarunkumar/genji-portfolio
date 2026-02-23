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

    # Create Profile
    Profile.objects.get_or_create(
        user=admin_user,
        defaults={
            'name': 'Genji Tarun Kumar',
            'bio': 'Full-stack Developer passionate about high-performance web applications and premium design aesthetics.',
            'skills': 'Python Django Docker PostgreSQL JavaScript React REST-API CI/CD',
            'education': 'B.Tech in Computer Science',
            'experience': 'Freelance Web Developer (2022 - Present)\nBuilt multiple full-stack applications for diverse clients.'
        }
    )
    print("Profile created/verified.")

    # Create Sample Projects
    projects = [
        {
            'title': 'E-Commerce Platform',
            'slug': 'ecommerce-platform',
            'description': 'A full-featured e-commerce site with payment integration, inventory management, and user authentication.',
            'tech_stack': 'Django Docker PostgreSQL Redis',
            'github_link': 'https://github.com/genjitarunkumar',
            'live_demo': 'https://genji-portfolio-1.onrender.com'
        },
        {
            'title': 'Smart AI Chatbot',
            'slug': 'smart-ai-chatbot',
            'description': 'An intelligent chatbot using natural language processing to handle customer inquiries in real-time.',
            'tech_stack': 'Python OpenAI API React FastAPI',
            'github_link': 'https://github.com/genjitarunkumar',
            'live_demo': 'https://genji-portfolio-1.onrender.com'
        },
        {
            'title': 'Real-time Analytics Dashboard',
            'slug': 'analytics-dashboard',
            'description': 'A high-performance dashboard that visualizes server metrics and user behavior in real-time.',
            'tech_stack': 'Django-Channels WebSockets Chart.js',
            'github_link': 'https://github.com/genjitarunkumar',
            'live_demo': 'https://genji-portfolio-1.onrender.com'
        }
    ]

    for p in projects:
        Project.objects.get_or_create(slug=p['slug'], defaults=p)
    print("Projects seeded.")

if __name__ == "__main__":
    seed()
