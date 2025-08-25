from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile, name='profile'),
    path('templates/', views.resume_templates, name='resume_templates'),
    path('resume/create/', views.create_resume, name='create_resume'),
    path('resume/<int:resume_id>/edit/', views.edit_resume_sections, name='edit_resume_sections'),
    path('resume/<int:resume_id>/delete/', views.delete_resume, name='delete_resume'),
    path('resume/<int:resume_id>/clone/', views.clone_resume, name='clone_resume'),
    path('resume/<int:resume_id>/view/', views.view_resume, name='view_resume'),
    path('resume/<int:resume_id>/export/pdf/', views.export_pdf, name='export_pdf'),
    path('resume/<int:resume_id>/export/docx/', views.export_docx, name='export_docx'),
    path('section/<int:section_id>/delete/', views.delete_resume_section, name='delete_resume_section'),
    path('announcements/', views.announcements, name='announcements'),
    path('announcement/create/', views.create_announcement, name='create_announcement'),
    path('announcement/<int:announcement_id>/edit/', views.edit_announcement, name='edit_announcement'),
    path('announcement/<int:announcement_id>/delete/', views.delete_announcement, name='delete_announcement'),
    path('resumes/', views.resume_list, name='resume_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)