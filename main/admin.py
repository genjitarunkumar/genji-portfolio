from django.contrib import admin
from .models import Profile, Skill, Project, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)
    list_filter = ('created_date',)

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(ContactMessage)
