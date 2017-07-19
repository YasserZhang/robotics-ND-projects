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
image = mpimg.imread(filename)
plt.imshow(image)
plt.show()
print(image.dtype, image.shape, np.min(image), np.max(image))

# uint8 (160, 320, 3) 0 255