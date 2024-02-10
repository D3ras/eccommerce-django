from django.shortcuts import render
from pooltables.models.gallery import Photo
from .utils import get_photo_paths
from django.views import View
def photos_gallery(request):
    photo_paths = get_photo_paths()
    photos = Photo.objects.all()  # You can query your Photo model for additional information if needed

    return render(request, 'gallery.html', {'photos': photos, 'photo_paths': photo_paths})
