from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    
    # Add additional fields based on user type
    # For example:
    # if user_type == 'teacher':
    #     additional_field = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    specialty = models.CharField(max_length=255)
    resume = models.TextField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    account_no = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    tel = models.CharField(max_length=15)
    picture = models.BinaryField()
    resume_file = models.BinaryField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)