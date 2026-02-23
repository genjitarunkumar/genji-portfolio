from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'phone_number')
    search_fields = ('name', 'user__username')
    fieldsets = (
        ('Personal Info', {
            'fields': ('user', 'name', 'bio', 'profile_image', 'resume')
        }),
        ('Professional Details', {
            'fields': ('skills', 'education', 'experience')
        }),
        ('Social Links', {
            'fields': ('github', 'linkedin', 'twitter', 'phone_number')
        }),
    )
