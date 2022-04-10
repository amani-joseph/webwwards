from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=200, blank=True)
    snapshot = ImageField(manual_crop='1280x720')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})