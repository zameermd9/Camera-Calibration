import pyrealsense2 as rs
import cv
import numpy as np

pipeline = rs.pipeline()
pipeline.start(rs.config().enable_stream(640,480,rs.format.bgr8, 30))

frames = pipeline.wait_for_frames()

