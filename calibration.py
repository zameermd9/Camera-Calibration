import numpy as np
import cv
import glob
import pickle

chessboardSize = (8, 6) 
frameSize = (640, 480)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30)

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)

objpoints = []  
imgpoints = []
images = glob.glob('/Users/zameerhussainmohammed/Desktop/camera calibration2/images/*.png')

for image in images:
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
    if ret:
        objpoints.append(objp)
        imgpoints.append(cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria))
        cv.drawChessboardCorners(img, chessboardSize, corners, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
cv.destroyAllWindows()
if objpoints and imgpoints:
    ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    pickle.dump((cameraMatrix, dist), open("calibration.pkl", "wb"))
    print("CameraMatrix:", cameraMatrix, "\nDist:", dist)


      
    

