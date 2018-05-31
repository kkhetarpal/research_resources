import os, cv2, sys
import numpy as np
import random
import skimage
from skimage import data
from skimage import color


def add_gaussian_noise(image):
    out = skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True)
    return out



def colorize(image, hue, saturation=1):
    """ Add color of the given hue to an RGB image.

    By default, set the saturation to 1 so that the colors pop!
    """
    hsv = color.rgb2hsv(image)
    hsv[:, :, 1] = saturation
    hsv[:, :, 0] = hue
    return color.hsv2rgb(hsv)


def change_background_color(image, hue):
    tinted_image = colorize(image, hue, saturation=0.5)
    return tinted_image


sampled_frames = []
# Test Code for a sequence of images added noise to them
# Aim is to introduce flickering in these images
imgs_test_path = '/home/ml/kkheta2/sam/sample_images/test/'
name1 = 'OriginalImage.jpg'
name2 = 'frame20.jpg'
name3 = 'frame30.jpg'
name4 = 'frame40.jpg'
fullfilename1 = imgs_test_path + name1
image1 = cv2.imread(fullfilename1)
sampled_frames.append(image1)
fullfilename2 = imgs_test_path + name2
image2 = cv2.imread(fullfilename2)
sampled_frames.append(image2)
fullfilename3 = imgs_test_path + name3
image3 = cv2.imread(fullfilename3)
sampled_frames.append(image3)
fullfilename4 = imgs_test_path + name4
image4 = cv2.imread(fullfilename4)
sampled_frames.append(image4)



flickered_frames = []
#Testing noise/flicker effect
for k in range(len(sampled_frames)-1):
    #temp = add_gaussian_noise(sampled_frames[k])
    hue = random.uniform(0, 1)
    temp = change_background_color(sampled_frames[k], hue)
    flickered_frames.append(temp)



for flickerimg, img in zip(flickered_frames, sampled_frames):
    cv2.imshow("Flicker Img", flickerimg)
    cv2.waitKey(0)
    cv2.imshow("Input", img)
    cv2.waitKey(0)