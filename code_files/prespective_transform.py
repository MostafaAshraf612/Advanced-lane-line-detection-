import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load image

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

def warp_image(image, src = None, dst = None):
    """
    Warps an image to a top-down (bird's-eye) perspective.

    Parameters:
    - image: input image
    - src: source points (trapezoid)
    - dst: destination points (rectangle)

    Returns:
    - warped: bird's-eye view of the image
    - M: perspective transform matrix
    """
    # Get image height and width
    h, w = image.shape[:2]
    # Source points (corners of the trapezoid in the original image)
    # These should roughly surround the lane lines in the perspective view
    if src == None :
        src = np.array([
            [242, 684],  # Bottom-left
            [1050, 677], # Bottom-right
            [750, 491],  # Top-right
            [541, 487]   # Top-left
        ], dtype=np.float32)

    # Destination points (corners of the rectangle for bird's-eye view)
    # Mapping the trapezoid to a rectangle
    if dst == None :
        dst = np.array([
            [w*0.25, h],  # Bottom-left
            [w*0.75, h],  # Bottom-right
            [w*0.75, 0],  # Top-right
            [w*0.25, 0]   # Top-left
        ], dtype=np.float32)

    # Compute the perspective transform matrix from src to dst
    M = cv2.getPerspectiveTransform(src, dst)

    # Apply the perspective warp
    warped = cv2.warpPerspective(image, M, (w, h))  # pyright: ignore[reportCallIssue, reportArgumentType]

    return warped, M


def unwarp_image(image,src = None, dst = None):
    """
    Reverts a bird's-eye image back to the original perspective.

    Parameters:
    - image: input warped image
    - src: source points (trapezoid)
    - dst: destination points (rectangle)

    Returns:
    - warped: image transformed back to original perspective
    - Minv: inverse perspective transform matrix
    """
    # Get image height and width
    h, w = image.shape[:2]
    # Source points (corners of the trapezoid in the original image)
    # These should roughly surround the lane lines in the perspective view
    if src == None :
        src = np.array([
            [242, 684],  # Bottom-left
            [1050, 677], # Bottom-right
            [750, 491],  # Top-right
            [541, 487]   # Top-left
        ], dtype=np.float32)

    # Destination points (corners of the rectangle for bird's-eye view)
    # Mapping the trapezoid to a rectangle
    if dst == None :
        dst = np.array([
            [w*0.25, h],  # Bottom-left
            [w*0.75, h],  # Bottom-right
            [w*0.75, 0],  # Top-right
            [w*0.25, 0]   # Top-left
        ], dtype=np.float32)

    # Compute the inverse perspective transform from dst to src
    Minv = cv2.getPerspectiveTransform(dst, src)

    # Apply the inverse warp
    warped = cv2.warpPerspective(image, Minv, (w, h))  # pyright: ignore[reportCallIssue, reportArgumentType]

    return warped, Minv
