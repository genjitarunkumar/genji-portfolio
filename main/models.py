from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    university = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    summary = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
