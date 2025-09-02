import matplotlib.pyplot as plt
import numpy as np
import cv2
def plot_images(image1 , title1 ,image2 , title2 ):
    print(image1.shape)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
    f.tight_layout()
    if len(image1.shape)==2:
        cmap = 'gray'
        
    else:
        cmap = None
    ax1.imshow(image1, cmap = cmap)
    ax1.set_title(title1, fontsize=50)
    ax2.imshow(image2 ,cmap='gray')
    ax2.set_title(title2, fontsize=50)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.) 


def draw_lane(original_img, binary_warped, left_fitx, right_fitx, ploty, Minv,
              left_curvature=None, right_curvature=None, vehicle_offset=None, xm_per_pix=3.7/700):
    # 1. Create an empty image
    color_warp = np.zeros_like(original_img).astype(np.uint8)

    # 2. Lane points
    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
    pts = np.hstack((pts_left, pts_right))  # for polygon fill

    # 3. Fill polygon (green, transparent later)
    cv2.fillPoly(color_warp, [pts.astype(np.int32)], (0, 255, 0))

    # 4. Draw lane borders
    cv2.polylines(color_warp, [pts_left.astype(np.int32)], isClosed=False, color=(255, 255, 0), thickness=15)  # Blue left
    cv2.polylines(color_warp, [pts_right.astype(np.int32)], isClosed=False, color=(255, 0, 255), thickness=15) # Red right

    # 5. Warp back to original perspective
    newwarp = cv2.warpPerspective(color_warp, Minv, (original_img.shape[1], original_img.shape[0]))

    # 6. Blend with original (0.3 transparency for fill)
    result = cv2.addWeighted(original_img, 1, newwarp, 0.3, 0)


    # 7. Overlay curvature and vehicle offset
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    thickness = 2
    line_type = cv2.LINE_AA

    cv2.putText(result, f'Left Curvature: {left_curvature:.2f} m',
                (50, 50), font, font_scale, font_color, thickness, line_type)
    cv2.putText(result, f'Right Curvature: {right_curvature:.2f} m',
                (50, 100), font, font_scale, font_color, thickness, line_type)
    cv2.putText(result, f'Vehicle Offset: {vehicle_offset:.2f} m',
                (50, 150), font, font_scale, font_color, thickness, line_type)

    # 8. Show result
    plt.figure(figsize=(10,6))
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
    return result
