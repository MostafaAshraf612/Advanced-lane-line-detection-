# 🚗 Advanced Lane Detection and Vehicle Positioning

![Python](https://img.shields.io/badge/Python-3.x-blue) ![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green) ![NumPy](https://img.shields.io/badge/NumPy-1.x-orange) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔍 Project Overview
This project implements a **robust lane detection system** using Python and OpenCV. It processes images and videos from a front-facing vehicle camera to detect lane lines, calculate lane curvature, and determine the vehicle’s position relative to the lane center. The system outputs **visual overlays** showing detected lanes, curvature, and vehicle offset, which are critical for autonomous driving, ADAS (Advanced Driver Assistance Systems), and robotics applications.

---

## 🛠 Key Features
- Image and video processing for lane detection  
- Color and gradient thresholding for robust line detection  
- Perspective transform for a bird’s-eye view of lanes  
- Polynomial fitting to calculate lane curvature  
- Vehicle offset calculation from lane center  
- Visualization of lanes, curvature, and offset  
- Modular and extensible for research or integration  

---

## ⚙️ How It Works
1. **Image Preprocessing**  
   - Convert images to grayscale or HLS color space  
   - Apply Gaussian blur for noise reduction  
   - Apply gradient and color thresholding to create binary images  

2. **Perspective Transform**  
   - Converts camera view to a bird’s-eye view  
   - Makes lane lines appear parallel for easier detection  

3. **Lane Pixel Detection**  
   - Detect left and right lane pixels using sliding windows  
   - Identify continuous lane lines in the binary image  

4. **Polynomial Fitting**  
   - Fit a second-degree polynomial to lane pixels  
   - Calculate lane curvature in meters  

5. **Vehicle Position**  
   - Compute the vehicle’s offset from lane center  
   - Determine if vehicle is drifting or centered  

6. **Visualization**  
   - Overlay detected lanes on original images/videos  
   - Display curvature and vehicle offset  

---

## 🎯 Applications
- Autonomous driving research  
- Driver assistance system prototyping  
- Robotics navigation along lanes  
- Educational purposes for computer vision learning  

---

## 📈 Example Output

**Image Output:**  
![Lane Detection Example](images/lane_example.png)  

**Video Output:**  
![Lane Detection Video GIF](images/lane_video.gif)  

*Note: Add your own images or GIFs to `images/` folder for a live preview.*

---

## 💻 Technologies Used
- Python 3.x  
- OpenCV  
- NumPy  
- Matplotlib  
- MoviePy  

---

## 🚀 Installation & Usage
1. Clone the repository:
```bash
git clone https://github.com/MostafaAshraf612/Advanced-lane-line-detection-.git

