
from django.contrib import admin
from . models import Message, Project, ProjectImage


@admin.register(Message)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', '__body__', 'date_send', 'replied']
    list_filter = ['replied']


@admin.register(ProjectImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
        model = Project
