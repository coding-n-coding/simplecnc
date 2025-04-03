from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Cnc(models.Model):
    topic = models.CharField(max_length=250)
    image = models.ImageField(upload_to='cnc\pics', blank=True, null=True, max_length=252)
    decs = HTMLField(blank=True, null=True)
    file = models.FileField(upload_to='cnc\pics', blank=True, null=True)
    date = models.DateField(auto_now_add=True)