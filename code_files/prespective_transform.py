import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load image
image = cv2.imread('test_images/straight_lines1.jpg')
h, w = image.shape[:2] # pyright: ignore[reportOptionalMemberAccess]
'''this is an ai generated Open cv click on image to get the src points automatically'''
'''
clicked_points = []
# Mouse callback function
def click_event(event, x, y, flags, param):
    global clicked_points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(clicked_points) < 4:
            clicked_points.append([x, y])
            cv2.circle(image, (x, y), 5, (0, 0, 255), -1) # pyright: ignore[reportCallIssue, reportArgumentType]
            cv2.putText(image, str(len(clicked_points)), (x+10, y-10), # pyright: ignore[reportArgumentType]
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1) # type: ignore
            cv2.imshow("Select 4 Points", image) # pyright: ignore[reportCallIssue, reportArgumentType]

        if len(clicked_points) == 4:
            cv2.destroyAllWindows()

# Show image and set callback
cv2.imshow("Select 4 Points", image) # pyright: ignore[reportCallIssue, reportArgumentType]
cv2.setMouseCallback("Select 4 Points", click_event)
cv2.waitKey(0)

if len(clicked_points) != 4:
    raise ValueError(f"You clicked {len(clicked_points)} points. Need exactly 4.")

# Convert points
src = np.array(clicked_points, dtype=np.float32)'''
src = np.array([
    [242, 684],
    [1050, 677],
    [750, 491],
    [541, 487]
], dtype=np.float32)
# Destination rectangle
dst = np.array([
    [w*0.25, h],
    [w*0.75, h],
    [w*0.75, 0],
    [w*0.25, 0]
], dtype=np.float32)
def warp_image(image ,src= src , dst = dst):
    # Perspective transform
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, M, (w, h)) # pyright: ignore[reportCallIssue, reportArgumentType]
    return warped ,M
def unwarp_image(image ,src= src , dst = dst):
    # Perspective transform
    Minv = cv2.getPerspectiveTransform(dst, src)
    warped = cv2.warpPerspective(image, Minv, (w, h)) # pyright: ignore[reportCallIssue, reportArgumentType]
    return warped , Minv
