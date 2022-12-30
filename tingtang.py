import cv2
import time 
import numpy as np 

#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

#Starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)
bg = 0

#Capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg, axis=1)

#Reading the captured frame until the camera is open
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis=1)

hsv = cv2.cvtColor(img, cvv2.COLOR_BGR2HSV)


lower_red = np.array([0, 120, 50])
upper_red = np.array([10, 255, 255])
mask_1 = cv2.inRanger(hsv, lower_red, upper_red)

lower_red = np.array([170, 120, 70])
upper_red = np.array([180, 255, 255])
mask_2 = cv2.inRanger(hsv, lower_red, upper_red)

mask_1 = mask_1 + mask_2

mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

mask_2 = cv2.bitwise_not(mask_1)


res_1 = cv2.bitwise_and(img, img, mask=mask_2)

res_2 = cv2.bitwise_and(bg, bg, mask=mask_2)

final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
output_file.write(final_output)

cv2.imshow("magic", final_output)
cv2.waitKey(1)


cap.release()
out.release()
cv2.destroyAllWindows()