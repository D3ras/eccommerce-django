import os
from django.conf import settings

def get_photo_paths():
    # Specify the folder path where your photos are stored
    folder_path = os.path.join(settings.MEDIA_ROOT, 'images')

    # List all files in the folder
    photo_paths = [os.path.join('images', filename) for filename in os.listdir(images)]

    return photo_paths
