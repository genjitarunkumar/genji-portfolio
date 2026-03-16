import urllib.request
import json
from django.core.management.base import BaseCommand
from projects_app.models import Project


class Command(BaseCommand):
    help = 'Sync GitHub repositories as portfolio projects'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, default='genjitarunkumar', help='GitHub username')

    def handle(self, *args, **options):
        username = options['username']
        self.stdout.write(f'Fetching repositories for GitHub user: {username}')

        url = f'https://api.github.com/users/{username}/repos?sort=updated&per_page=100'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        try:
            with urllib.request.urlopen(req) as response:
                repos = json.loads(response.read().decode())
        except Exception as e:
            self.stderr.write(f'Error fetching repos: {e}')
            return

        created = 0
        updated = 0

        for repo in repos:
            if repo.get('fork'):
                continue

            title = repo['name'].replace('-', ' ').replace('_', ' ').title()
            description = repo.get('description') or f'A project built using {repo.get("language") or "various technologies"}.'
            github_link = repo['html_url']
            live_demo = repo.get('homepage') or ''
            tech_stack = repo.get('language') or 'Python'
            base_slug = repo['name'].lower().replace('_', '-')

            project = Project.objects.filter(github_link=github_link).first()
            if project:
                project.title = title
                project.description = description
                project.tech_stack = tech_stack
                project.live_demo = live_demo
                project.save()
                updated += 1
                self.stdout.write(f'  Updated: {title}')
            else:
                slug = base_slug
                counter = 1
                while Project.objects.filter(slug=slug).exists():
                    slug = f'{base_slug}-{counter}'
                    counter += 1

                Project.objects.create(
                    title=title,
                    slug=slug,
                    description=description,
                    tech_stack=tech_stack,
                    github_link=github_link,
                    live_demo=live_demo,
                )
                created += 1
                self.stdout.write(f'  Created: {title}')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {created} projects created, {updated} projects updated from GitHub.'
        ))
