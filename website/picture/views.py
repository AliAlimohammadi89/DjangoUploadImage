import os

import cv2
import matplotlib.pyplot as plt
from django.conf import settings
from django.shortcuts import render
from skimage import filters

from .forms import ImageForm


# import string
# from re import match
# from unittest import case


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        countofpic = int(request.POST.get('countofpic', None))
        functinRun(countofpic, request)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


from skimage.data import camera

def imageedit(request):
    filename = request.FILES['image']
    form = ImageForm(request.POST, request.FILES)
    form.save()
    path = os.path.join(settings.MEDIA_ROOT, 'images', filename.name)
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


def imageedit2(request):
    image = camera()
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

    return

def imageedit3(request):
    image = camera()
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

    return


def imageedit4(request):
    image = camera()
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

    return


def functinRun(i, request):
    if i == 1:

        imageedit(request)
        return

    elif i == 2:
        imageedit2(request)
        return

    elif i == 3:
        imageedit3(request)
        return

    elif i == 4:
        imageedit4(request)
        return
