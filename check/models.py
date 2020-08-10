from django.db import models
from django.urls import reverse
# Create your models here.
class files(models.Model):
    file1= models.FileField()
    file2 = models.FileField()


    def get_absolute_url(self):
        return reverse('result',)

