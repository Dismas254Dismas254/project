from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]  # Show first 50 characters in admin panel
