from django.contrib import admin
from .models import Video, Question

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')  # Display title & upload date
    search_fields = ('title',)  # Allow searching by title
    list_filter = ('upload_date',)  # Filter by date

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'upload_date')  # Display question & date
    search_fields = ('question_text',)  # Allow searching by question
    list_filter = ('upload_date',)  # Filter by date
