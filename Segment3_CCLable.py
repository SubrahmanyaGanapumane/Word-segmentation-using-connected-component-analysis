# Import the cv2 library
import cv2
import numpy as np
# Read the image you want connected components of
img = cv2.imread('0303.jpg',0)

binimg=cv2.medianBlur(img,5)
invimg=cv2.bitwise_not(img)
kernel = np.ones((3,10),np.uint8)*255
dilation=cv2.dilate(invimg,kernel,iterations=2)
orgimg=cv2.bitwise_not(dilation)
# Threshold it so it becomes binary
ret, thresh = cv2.threshold(dilation,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# You need to choose 4 or 8 for connectivity type
connectivity = 4  
# Perform the operation
output = cv2.connectedComponentsWithStats(thresh, connectivity)
# Get the results
# The first cell is the number of labels
num_labels = output[0]
# The second cell is the label matrix
labels = output[1]
# The third cell is the stat matrix
stats = output[2]
# The fourth cell is the centroid matrix
centroids = output[3]

cv2.imwrite('crop.jpg',dilation)
cv2.imwrite('cropnot.jpg',orgimg)
cv2.imwrite('croplabels.jpg',labels)
print num_labels

for i in range(len(stats)):
    y=stats[i][0]
    w=stats[i][2]
    x=stats[i][1]
    h=stats[i][3]
    crop=img[x:x+h,y:y+w]
    cv2.imwrite("out/"+str(i)+'.jpg', crop)
    #cv2.imshow("d",crop)
    #cv2.waitKey(0)
    
    
