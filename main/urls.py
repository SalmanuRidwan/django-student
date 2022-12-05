from django.urls import path
from .views import SignUpView, home, CourseRegistrationView, dashboard, courses, students, student

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', home, name='home'),
    path('courses-new/', CourseRegistrationView.as_view(), name="courses-new"),
    path('dashboard/', dashboard, name='dashboard'),
    path('courses/', courses, name='courses'),
    path('students/', students, name='students'),
    path('students/<int:id>/', student, name='student'),
]
