import numpy as np
import cv2

class SetupCam:
    @staticmethod
    def method_setup ():
        print("Starting cam setup")
        cap = cv2.VideoCapture(0)
        cap.set(3,480) # set Width
        cap.set(4,370) # set Height
        print("Done cam setup")
        return(cap)
