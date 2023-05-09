# importing the necessary modules.
import cv2
import numpy as np

# loading the JPEG image from Github.
image = cv2.imread('/Users/tareq/Documents/Uni/SE226/labs/Lab7/pic.jpeg')

# splitting the image into its color channels.
blue, green, red = cv2.split(image)

# showing the individual color channels.
cv2.imshow('Blue', blue)
cv2.imshow('Green', green)
cv2.imshow('Red', red)

# creating a new picture with only red and blue colors and show it.
red_blue_Image = cv2.merge([blue, np.zeros_like(green), red])
cv2.imshow("Red-Blue Image", red_blue_Image)

# combining the modified color channels back into a single image and show it.
original_Image = cv2.merge([blue, green, red])
cv2.imshow('Combined Image', original_Image)

# end
cv2.waitKey(0)
cv2.destroyAllWindows()