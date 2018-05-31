# import cv2
# vidcap = cv2.VideoCapture('MontezumaRevengewithIM.mp4')
# success,image = vidcap.read()
# count = 0
# success = True
# while success:
#       success,image = vidcap.read()
#       print('Read a new frame: ', success)
#       cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#       count += 1




import cv2
vidcap = cv2.VideoCapture('MontezumaRevengewithIM.mp4') #Video with full path or video name lying in the same directory
success,image = vidcap.read()
count = 1
success = True
path = "/home/ml/kkheta2/sam/sample_images/"   #Path to save the images
while success:
    success,image = vidcap.read()
    print('Read a new frame number: ', count)
    filename = "frame%d.jpg" % count
    fullfilename = path + filename
    #print(fullfilename)
    cv2.imwrite(fullfilename, image)     # save frame as JPEG file
    count += 1

