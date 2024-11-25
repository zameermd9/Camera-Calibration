import pyrealsense2 as rs
import cv
import numpy as np

pipeline = rs.pipeline()
pipeline.start(rs.config().enable_stream(640,480,rs.format.bgr8, 30))

frames = pipeline.wait_for_frames()
color_frame = frames.get_color_frame()
cv.imwrite("calibration_image.png", np.asanyarray(color_frame.get_data()))
pipeline.stop()

