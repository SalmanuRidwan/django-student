from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Course
from users.models import CustomUser

User = CustomUser


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    return render(request, 'home.html')


class CourseRegistrationView(CreateView):
    form_class = CourseForm
    success_url = reverse_lazy('courses')
    template_name = 'courses-new.html'

def dashboard(request):
    return render(request, 'dashboard.html')

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def students(request):
    students = User.objects.all()
    return render(request, 'students.html', {'students': students})

def student(request, id):
    student = User.objects.get(id=id)
    return render(request, 'student.html', {'student': student})