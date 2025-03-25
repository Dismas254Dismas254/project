from django import forms
from .models import Video, Question

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file','thumbnail']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
