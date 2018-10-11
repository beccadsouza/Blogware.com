from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(User,models.Model):
    usertype = models.CharField(max_length = 10)


    def __str__(self):
        return ' '.join(list([self.username,self.first_name,self.last_name,self.usertype]))

