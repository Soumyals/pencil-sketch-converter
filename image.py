#Image to pencil sketch convertion project:-
import cv2
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

# Load the image
def load_image():
    global image
    file_path = filedialog.askopenfilename()
    image = cv2.imread(file_path)
    create_sobel(image)
    #display_sketch(sketch_sobel)
    sketch = create_sketch(image)
    display_sketch(sketch)
    
def create_sobel(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
    sobelx = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    edges= cv2.Canny(image=blur_img,threshold1=100,threshold2=100)# canny edge detection
    h, w = img.shape[0:2]
    neww = 800
    newh = int(neww*(h/w))
    sobelx = cv2.resize(sobelx, (neww, newh))
    sobely = cv2.resize(sobely, (neww, newh))
    sobelxy = cv2.resize(sobelxy, (neww, newh))
    cv2.namedWindow("Sobel X", cv2.WINDOW_NORMAL)
    # Display Sobel Edge Detection Images
    cv2.imshow("Sobel X", sobelx)
    cv2.resizeWindow("Sobel X", 800, 800)
    cv2.waitKey(0)
    cv2.namedWindow("Sobel Y", cv2.WINDOW_NORMAL)
    cv2.imshow("Sobel Y", sobely)
    cv2.resizeWindow("Sobel Y", 800, 800)
    cv2.waitKey(0)
    cv2.namedWindow("Sobel X Y using Sobel() function", cv2.WINDOW_NORMAL)
    cv2.imshow("Sobel X Y using Sobel() function", sobelxy)
    cv2.resizeWindow("Sobel X Y using Sobel() function", 800, 800)
    cv2.waitKey(0)
    cv2.namedWindow("canny edge detection",cv2.WINDOW_NORMAL)
    cv2.imshow("canny edge detection",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Convert the image to sketch
def create_sketch(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
    edges = cv2.Canny(blur_img, 10, 30)
    inverted = cv2.bitwise_not(edges)
    h, w = img.shape[0:2]
    neww = 800
    newh = int(neww*(h/w))
    sketch = cv2.normalize(inverted, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    sketch = cv2.resize(sketch, (neww, newh))
    return sketch

# Display the sketch
def display_sketch(sketch):
    cv2.namedWindow("Sketch", cv2.WINDOW_NORMAL)
    cv2.imshow("Sketch", sketch)
    cv2.resizeWindow("Sketch", 800, 800)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Create the GUI
root = tk.Tk()
root.title("Image to Sketch Converter")

load_button = tk.Button(text="insert Image", command=load_image)
load_button.pack()

root.mainloop()