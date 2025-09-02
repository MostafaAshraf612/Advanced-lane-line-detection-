import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from camera_calibration import undistort_img
from plot import plot_images
from plot import draw_lane
from thresholding import apply_thresholding
from prespective_transform import warp_image
from prespective_transform import unwarp_image
from lane_detection import fit_polynomial
from lane_detection import measure_curvature_real
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import VideoClip
import cv2
from tqdm import tqdm
'''
#-----------------------1. Calibrate Camera(if not calibrated) and Undistort Images ------------------------#
image = mpimg.imread('test_images/test2.jpg')
undistorted_image = undistort_img(image)
plot_images(image ,'Original Image' , undistorted_image , 'Undistorted Image')


#-----------------------2. Use color transforms, gradients, etc., to create a thresholded binary image ------------------------#
thresholded_image = apply_thresholding(undistorted_image , 3 , (20,100) , (170,255))
plot_images(undistorted_image ,'Undistorted Image' , thresholded_image , 'thresholded Image')


#-----------------------3. Apply a perspective transform to rectify binary image ("birds-eye view") ------------------------#
warped_image ,_= warp_image(thresholded_image)
plot_images( thresholded_image , 'thresholded Image' , warped_image , 'Warped (Bird Eye View) Image')

#-----------------------4. Detect lane pixels and fit to find the lane boundaryand Determine the curvature of the lane and vehicle position with respect to center. ------------------------#
left_fit_coeff , right_fit_coeff , left_fitx , right_fitx ,ploty = fit_polynomial(warped_image)
left_curvature , right_curvature , offset = measure_curvature_real(warped_image, xm_per_pix=3.7/700, ym_per_pix=30/720) # pyright: ignore[reportAssignmentType]
print('left curvature is {} m and right_curvature is {} ' .format(left_curvature , right_curvature))
print('vehicle offset {} ' .format( offset))
#-----------------------5.  ------------------------#
unwarped_imag , Minv = unwarp_image(warped_image)
draw_lane(image , unwarped_imag , left_fitx , right_fitx, ploty , Minv ,left_curvature ,right_curvature ,offset)
plt.show()
'''
def detect_lane(image):
    undistorted_image = undistort_img(image)
    #-----------------------2. Use color transforms, gradients, etc., to create a thresholded binary image ------------------------#
    thresholded_image = apply_thresholding(undistorted_image , 3 , (20,100) , (170,255))
    #-----------------------3. Apply a perspective transform to rectify binary image ("birds-eye view") ------------------------#
    warped_image ,_= warp_image(thresholded_image)
    #-----------------------4. Detect lane pixels and fit to find the lane boundaryand Determine the curvature of the lane and vehicle position with respect to center. ------------------------#
    left_fit_coeff , right_fit_coeff , left_fitx , right_fitx ,ploty = fit_polynomial(warped_image)
    left_curvature , right_curvature , offset = measure_curvature_real(warped_image, xm_per_pix=3.7/700, ym_per_pix=30/720) # pyright: ignore[reportAssignmentType]
    #-----------------------5.  ------------------------#
    unwarped_imag , Minv = unwarp_image(warped_image)
    return draw_lane(image , unwarped_imag , left_fitx , right_fitx, ploty , Minv ,left_curvature ,right_curvature ,offset)



## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4").subclip(0,5)
def video_lane_detection(video_path : str  ,output_video_name : str):
    # -------------------------------
    # LOAD VIDEO
    # -------------------------------
    input_video = video_path  # replace with full path if needed
    clip = VideoFileClip(input_video)  
    duration = min(5, clip.duration)  # avoids subclip
    # test on first 5 seconds

    # -------------------------------
    # PROCESS FRAMES
    # -------------------------------
    def make_frame(t):
        frame = clip.get_frame(t)
        return detect_lane(frame)

    processed_clip = VideoClip(make_frame, duration=duration)

    # -------------------------------
    # SAVE OUTPUT VIDEO
    # -------------------------------
    output_video = "ALLD_project.mp4"
    processed_clip.write_videofile(output_video, fps=clip.fps, audio=False)

    return('Video Processing is done!')



def video_lane_detection2(video_path : str  ,output_video_name : str):
    # Open input video
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # total frames

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_name, fourcc, fps, (width, height))

    # Progress bar
    pbar = tqdm(total=total_frames, desc="Processing video", unit="frame")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        processed = detect_lane(frame)
        processed_bgr = cv2.cvtColor(processed, cv2.COLOR_RGB2BGR)
        out.write(processed_bgr)
        pbar.update(1)

    pbar.close()
    cap.release()
    out.release()
    return print("Processing complete! Saved as", output_video_name)

video_lane_detection2('project_video.mp4' , 'ALLD_project.mp4')