import numpy as np
import cv
import glob
import pickle

chessboardSize = (8, 6) 
frameSize = (640, 480)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30)