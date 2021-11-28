import cv2


def edgeMask(image,lineSize,blurValue):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    grayBlur=cv2.medianBlur(gray,blurValue)
    edges=cv2.adaptiveThreshold(grayBlur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,lineSize,blurValue)
    return edges


video = cv2.VideoCapture(0)
a=0
while True:
    a+=1
    check, frame=video.read()
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)
    if key%256 == 32:
        break


showPic = cv2.imwrite("Pic.jpg",frame)
print(showPic)
video.release()
cv2.destroyAllWindows()
path = r'Pic.jpg'
img = cv2.imread(path)
line_size = 7
blur_value = 3
edges = edgeMask(img, line_size, blur_value)
colorImage = cv2.bilateralFilter(img, 9, 300, 300)
cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=edges)
cv2.imshow("Edges",cartoonImage)
cv2.imwrite("Cartoon.jpg",cartoonImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
