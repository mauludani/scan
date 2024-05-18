import pyautogui
import requests
import time
import cv2
import numpy as np
from PIL import Image, ImageOps
from io import BytesIO

def capture_screen_area(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

def main(index):
    # Contoh pemanggilan fungsi capture_screen_area dengan koordinat (left, top) dan ukuran (width, height) yang diinginkan
    left = 0
    top = 100
    width = 66
    height = 800

    screenshot = capture_screen_area(left, top, width, height)
    img_h, img_w = screenshot.size

    screenshot_np = np.array(screenshot)

    # Define the new size
    new_size = (img_h * 3, img_w * 3)

    # Resize the image using OpenCV
    upscaled_img_np = cv2.resize(screenshot_np, new_size, interpolation=cv2.INTER_CUBIC)

    # Convert the upscaled image (NumPy array) back to a PIL Image
    upscaled_img = Image.fromarray(upscaled_img_np)

    # Display the upscaled image
    upscaled_img.show()
    # screenshot.show()  # Tampilkan tangkapan layar dalam jendela pop-up

if __name__ == "__main__":
    index = 0
    main(index)