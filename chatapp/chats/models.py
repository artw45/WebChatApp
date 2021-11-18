from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    connectionid = models.CharField(max_length=30)
    fakecount = models.IntegerField(default=0)  
    commonchatid = models.CharField(max_length=30)  
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.contact.user.username

