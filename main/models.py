from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)

class Course(models.Model):
    name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return f'{self.name} - {self.course_code}'
