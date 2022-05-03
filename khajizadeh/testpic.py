import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import filters
# from skimage.data import camera
from skimage.util import compare_images

path = "1.jpg"
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
