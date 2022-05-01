import os
import random

from PIL import Image
from django.shortcuts import render

from .forms import ImageForm
from django.conf import settings

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            fileitem = request.FILES['image']
            countofpic = request.POST.get('countofpic', None)
            form.save()
            img_obj = form.instance
            imagelistName = []
            for x in range(int(countofpic)):
                imagelistName.append(uploadMultiImage(fileitem))
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'imagelistName': imagelistName})
    else:
        form = ImageForm()
        return render(request, 'index.html', {'form': form})


def uploadMultiImage(fileitem):
    filename = fileitem.name
    randoms = str(random.randint(1000, 99999)) + str('-')
    newFileName = randoms + filename
    UPLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'images', filename)
    img = Image.open(UPLOAD_DIR)
    img2 = img.size
    resized_img = img.resize((500, 500))
    UPLOAD_DIR1 = os.path.join(settings.MEDIA_ROOT, 'images', newFileName)
    resized_img.save(UPLOAD_DIR1)
    return (newFileName)
