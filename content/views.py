from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Video, Question
from .forms import VideoForm, QuestionForm

def home(request):
    return render(request, 'content/home.html')

@login_required
def dashboard(request):
    """
    Dashboard after user login with buttons to view uploaded videos and questions.
    """
    return render(request, 'content/dashboard.html')

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'content/video_list.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'content/video_detail.html', {'video': video})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'content/question_list.html', {'questions': questions})

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VideoForm()
    return render(request, 'content/upload_video.html', {'form': form})

@login_required
def upload_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = QuestionForm()
    return render(request, 'content/upload_question.html', {'form': form})

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'content/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'content/login.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect('home')
