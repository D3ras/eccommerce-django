from django.db import models
from .customer import CustomUser
import os

def get_upload_path(instance, filename):
    # This function will determine the file upload path
    return os.path.join('images', filename)

class Photo(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    title = models.CharField(max_length=100)
    def __str__(self):
          return self.title
class Like(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

class Review(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField()

class Rating(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
