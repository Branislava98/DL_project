import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import os
os.environ["NPY_ALLOW_DEPRECATED_API"] = "1"
import cv2
import numpy as np

img1 = cv2.imread("output/output_image.png")
img2 = cv2.imread("output/test_output_image.png")

# Computing the pixel-wise difference between the two images
difference = cv2.subtract(img1, img2)

# Computing image similarity (in percentages)
similarity = (np.sum(difference == 0) / difference.size) * 100

if similarity > 80:
	print("Test passed")
else:
	print("Test failed")
print("Image similarity: ", similarity, "%")
