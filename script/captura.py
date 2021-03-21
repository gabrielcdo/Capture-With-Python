import cv2
import math
num=0

cap = cv2.VideoCapture('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov')
framer = cap.get(5)

while (cap.isOpened()):
    frameid = cap.get(1) # Frame Atual
    ret , frame = cap.read()
    if(ret != True):
        break
    if (frameid % (5*math.floor(framer))== 0):
        cv2.imwrite('./imagens/foto' + str(num)+'.png' , frame)
        num+=1



cap.release()

       
