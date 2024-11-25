from realsense_camera import *

capture = cv2.VideoCapture(0)
#rs = RealsenseCamera()
#vid = cv2.VideoCapture(1)
num = 1
#Rit, bgr, depth = rs.get_frame_stream()



while True:
    #Rit, bgr, depth = rs.get_frame_stream()
    #cap = bgr
    isTrue, cap = capture.read()
    cv.imshow('Video', cap)
    #print(cap.shape)
    
    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/img' + str(num) + '.png', cap)
        #cv2.imwrite("gray" + str(num) +".jpg", cap)
        print("image saved!")
        num += 1

    cv2.imshow('Img',cap)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()