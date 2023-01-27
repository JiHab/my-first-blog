from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your models here.


class MyUser(User):
    def send_auth_url(self):
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            [MyUser.email],
            fail_silently=False,
        )