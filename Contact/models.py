from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = (
('Male', 'Male'),
('Female', 'Female'),
('P', 'Prefer not to answer'),
)


class Contact(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True, blank=True)
    nickname = models.TextField(max_length=64, null=True, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField()
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=8,
                              choices=GENDER_CHOICES, )
    bio = models.TextField(max_length=1024, null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='Contact_profile/', null=True, blank=True)


    def __str__(self):
        return self.name
