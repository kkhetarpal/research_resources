from os import listdir
from os.path import isfile, join
import numpy
import cv2

mypath='/home/ml/kkheta2/tmp/unreal_checkpoints/llarla/foveate_alpha0.65/zero_shot_tinted_flipcoin'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
#for n in range(0, len(onlyfiles)):
for n in range(0, 1200):
      images[n] = cv2.imread( join(mypath,onlyfiles[n]))
      #cv2.imshow('video',images[n])
      #cv2.waitKey(1)
print n


path = '/home/ml/kkheta2/tmp/unreal_checkpoints/llarla/'
filename = 'UnrealFoveateNavMazeStatic01zero_shot_tinted_flipcoin.mp4'
output = path + filename
#frame = cv2.imread('/home/ml/kkheta2/sam/sample_images/processedframes/frame1.jpg')
frame = cv2.imread('/home/ml/kkheta2/tmp/unreal_checkpoints/llarla/foveate_alpha0.65/zero_shot_tinted_flipcoin/000000.png')
cv2.imshow('video',frame)
cv2.waitKey(1)
height, width, channels = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
#fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

print len(images)
#for img in range(0,len(images)):
for img in range(0,1200):
    frame = images[img]
    out.write(frame)
    #cv2.imshow('video',frame)
out.release()
cv2.destroyAllWindows()


