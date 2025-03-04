from django.urls import path
from .views import home, dashboard, video_list, video_detail, question_list, upload_video, upload_question, register, user_login, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:video_id>/', video_detail, name='video_detail'),
    path('questions/', question_list, name='question_list'),
    path('upload/video/', upload_video, name='upload_video'),
    path('upload/question/', upload_question, name='upload_question'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
