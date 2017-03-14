import cv2
import cv2.aruco as aruco
import numpy as np

ppi = 200 #Pixels per inch
pageWidth = 8.5 #Width of page in inches
pageHeight = 11 #Height of page in inches
size = 0.5 #Size of marker in inches
offset = 0.25 #Offset of marker from page edge in inches
mID = 27 #Marker id

#Versions in terms of pixels
pPageWidth = int(ppi*pageWidth)
pPageHeight = int(ppi*pageHeight)
pSize = int(ppi*size)
pOffset = int(ppi*offset)

def drawMarker(page, marker, leftX, rightX, topY, bottomY):
    page[int(topY):int(bottomY), int(leftX):int(rightX), 0] = marker
    page[int(topY):int(bottomY), int(leftX):int(rightX), 1] = marker
    page[int(topY):int(bottomY), int(leftX):int(rightX), 2] = marker

#Get dictionary
dict = aruco.getPredefinedDictionary(15);

#Create page
page = np.zeros((pPageHeight,pPageWidth,3), np.uint8)
page[:] = (255, 255, 255)

#Create marker
marker = aruco.drawMarker(dict, mID, pSize)

#Draw markers
drawMarker(page, marker, pOffset, pOffset+pSize, pOffset, pOffset+pSize) #Top left
drawMarker(page, marker, pPageWidth-pOffset-pSize, pPageWidth-pOffset, pOffset, pOffset+pSize) #Top right
drawMarker(page, marker, pOffset, pOffset+pSize, pPageHeight-pOffset-pSize, pPageHeight-pOffset) #Bottom left
drawMarker(page, marker, pPageWidth-pOffset-pSize, pPageWidth-pOffset, pPageHeight-pOffset-pSize, pPageHeight-pOffset) #Bottom right

#Show/save images
#cv2.imshow("Marker", marker)
cv2.imwrite("genpage.png", page)
rpage = cv2.resize(page, None,fx=0.3, fy=0.3)
cv2.imshow("Page", rpage)

cv2.waitKey(0)
