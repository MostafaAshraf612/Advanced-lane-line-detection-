import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import glob 
import pickle
def get_calibration_points(images_file_name , chessboard_dim = (8,6)):
    # chessboard_dim using the Width x Height format as that's what Opencv use 
    image_points   = [] # 2D array containing the image points in image plane (flat x-y plane)
    object_points  = [] # 3D array containing the image points in real world plane (x,y,z plane)
    images_paths = glob.glob(images_file_name)
    for path in images_paths:
        #getting object points for each image
        objp = np.zeros((chessboard_dim[0]*chessboard_dim[1] , 3) , np.float32)
        objp[:,:2] = np.mgrid[0:chessboard_dim[0] ,0:chessboard_dim[1]].T.reshape(-1,2) 
        image = cv2.imread(path)
        gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY) # pyright: ignore[reportCallIssue, reportArgumentType]
        ret , corners = cv2.findChessboardCorners(gray , chessboard_dim ,None) # pyright: ignore[reportArgumentType]
        if ret == True:
            image_points.append(corners)
            object_points.append(objp)
            image = cv2.drawChessboardCorners(image ,chessboard_dim ,corners,ret) # pyright: ignore[reportArgumentType, reportCallIssue]
            #plt.imshow(image)
    return object_points , image_points 

def undistort_img (image):
    object_points , image_points  = get_calibration_points('calibration_wide/GO*.jpg')
    retval, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(object_points , image_points ,(image.shape[1],image.shape[0]) , None , None) # pyright: ignore[reportCallIssue, reportArgumentType]
    undist = cv2.undistort(image ,cameraMatrix ,distCoeffs, None ,cameraMatrix)
    return undist
