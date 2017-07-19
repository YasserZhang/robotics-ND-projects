# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:00:33 2017

@author: flyin
"""


# Import some packages from matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#import numpy as np
import numpy as np

# Uncomment the next line for use in a Jupyter notebook
#%matplotlib inline

# Define the filename, read and plot the image
filename = 'sample.jpg'
"""
image = mpimg.imread(filename)
plt.imshow(image)
plt.show()
print(image.dtype, image.shape, np.min(image), np.max(image))
"""
# uint8 (160, 320, 3) 0 255

# Define color selection criteria
###### TODO: MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
red_threshold = 160
green_threshold = 160
blue_threshold = 160
######
rgb_threshold = (red_threshold, green_threshold, blue_threshold)
# pixels below the thresholds
colorsel = color_thresh(image, rgb_thresh=rgb_threshold)

# Display the original image and binary               
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)

ax2.imshow(colorsel, cmap='gray')
ax2.set_title('Your Result', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
