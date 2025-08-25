from django.contrib import admin
from .models import Announcement, ResumeTemplate, Resume, ResumeSection

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at']

@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Resume)
admin.site.register(ResumeSection)