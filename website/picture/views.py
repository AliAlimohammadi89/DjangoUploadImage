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

            imageedit(fileitem)
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

import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import filters
# from skimage.data import camera
from skimage.util import compare_images

def imageedit (filename):
    print ('edit')
    # path = r"1.jpg"
    path =  os.path.join(settings.MEDIA_ROOT, 'images', filename.name)
    image = cv2.imread(path)
    b, g, r = cv2.split(image)  # image
    image = g
    # image = camera()
    edge_roberts = filters.roberts(image)
    edge_sobel = filters.sobel(image)



    fig, axes = plt.subplots(ncols=4, sharex=True, sharey=True,
                             figsize=(8, 4))

    axes[0].imshow(image, cmap=plt.cm.gray)
    axes[0].set_title('original image')

    axes[1].imshow(edge_roberts, cmap=plt.cm.gray)
    axes[1].set_title('Roberts Edge Detection')

    axes[2].imshow(edge_sobel, cmap=plt.cm.gray)
    axes[2].set_title('Sobel Edge Detection')

    axes[3].imshow(edge_sobel, cmap=plt.cm.gray)
    axes[3].set_title('Sobel Edge Detection')

    for ax in axes:
        ax.axis('off')

    plt.tight_layout()
    plt.show()

