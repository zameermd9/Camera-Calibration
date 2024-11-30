Task:
Camera Calibration

GITHUB Link:
https://github.com/zameermd9/camera-calibration

Inputs:
1.open calibration.py file
2.Download the Images in GITHUB link and copy the images link as path and paste in line 19 (images = glob.glob(' ')) in python code

Things i did in Building this Code:
1.Built the code for the working of Realsense camera(realsense_camera.py)
2.Using a Checkerboard: I used a checkerboard with 8x6 squares to calibrate the camera because it’s a common and accurate tool for this purpose.
3.Finding Checkerboard Corners: My code detects the corners of the checkerboard in the images, which is needed for calibration.
4.Creating a 3D Grid: I made a 3D grid of points to represent the real positions of the checkerboard corners.
5.Preparing the Images: The program loads all .png images from a folder and converts them to black-and-white to make it easier to find the corners.
6.Improving Accuracy: After detecting the corners, I refined their positions to make them more accurate.
7.Storing the Data: I saved the real-world 3D points and their matching 2D points from the images.
8.Calibrating the Camera: Using this data, I calculated important camera details like its focus and how much it distorts the images.
9.Fixing Distortion: I fixed a sample image to show how the camera now takes clear, distortion-free pictures.
10.Saving Results: I saved the fixed images and the camera data (like focus and distortion values) so they can be reused later.
11.Checking the Results: I measured the error to ensure the calibration is accurate.
12.Making the Camera Useful: This code makes the camera ready for tasks like robotics, 3D modeling, or AR by ensuring the images are clear and undistorted.
















