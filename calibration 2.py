import cv2
import glob
import pickle

################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################

chessboardSize = (8, 6)  # Adjust to your checkerboard's internal corner dimensions
frameSize = (640, 480)   # Define the resolution of your images

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)

size_of_chessboard_squares_mm = 20  # You can adjust the size of your chessboard squares in mm
objp = objp * size_of_chessboard_squares_mm  # Scale the object points by the size of each square

# Arrays to store object points and image points from all the images
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# Glob pattern to find all images in your folder (make sure this path is correct)
images = glob.glob('/Users/zameerhussainmohammed/Desktop/camera calibration2/images/*.png')
print("Images found:", images)  # Debugging line

# Loop through all the images and find the chessboard corners
for image in images:
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)

    # If corners are found, refine the corners and save the points
    if ret == True:
        print(f"Corners found in {image}")  # Debugging line
        objpoints.append(objp)  # Add the object points
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)  # Refine corner locations
        imgpoints.append(corners2)  # Add the refined corners to imgpoints

        # Draw and display the corners on the image
        cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1000)  # Display each image for 1000 ms
    else:
        print(f"No corners found in {image}")  # Debugging line

# Close any OpenCV windows
cv.destroyAllWindows()

# Perform calibration only if valid points were found
if len(objpoints) > 0 and len(imgpoints) > 0:
    ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)

    # Save the camera calibration results for later use
    pickle.dump((cameraMatrix, dist), open("calibration.pkl", "wb"))
    pickle.dump(cameraMatrix, open("cameraMatrix.pkl", "wb"))
    pickle.dump(dist, open("dist.pkl", "wb"))

    print("CameraMatrix:", cameraMatrix)
    print("Dist:", dist)

    # Reprojection Error
    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
        error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2) / len(imgpoints2)
        mean_error += error

    print("Total reprojection error: {}".format(mean_error / len(objpoints)))
else:
    print("No valid images with detected corners for calibration.")
