from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from main.models import Course

GENDER_CHOICES = (
    ('female', 'FEMALE'),
    ('male', 'MALE')
)

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    reg_no = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    is_student = models.BooleanField(default=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    course = models.ManyToManyField(Course)

    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])
    