import pyautogui
import pytesseract
import cv2
import numpy as np
from PIL import Image, ImageOps

def capture_screen_area(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

def replace_green_and_red_with_black(image):
    # Convert PIL Image to NumPy array
    image_np = np.array(image)

    # Define color thresholds for red and green
    lower_red = np.array([0, 0, 100])
    upper_red = np.array([80, 80, 255])
    lower_green = np.array([0, 100, 0])
    upper_green = np.array([80, 255, 80])

    # Create masks for red and green colors
    red_mask = cv2.inRange(image_np, lower_red, upper_red)
    green_mask = cv2.inRange(image_np, lower_green, upper_green)

    # Combine masks
    mask = red_mask | green_mask

    # Replace red and green with black
    image_np[mask != 0] = [0, 0, 0]

    # Convert back to PIL Image
    return Image.fromarray(image_np)

def main(index):
    # Example of calling capture_screen_area with desired coordinates (left, top) and size (width, height)
    left = 0
    top = 160
    width = 76
    height = 600

    screenshot = capture_screen_area(left, top, width, height)

    # Convert the screenshot to RGB mode if it's in RGBA mode
    if screenshot.mode == 'RGBA':
        screenshot = screenshot.convert('RGB')

    # Replace green and red colors with black
    processed_image = replace_green_and_red_with_black(screenshot)

    # Invert the colors of the image
    inverted_image = ImageOps.invert(processed_image)

    # Convert the PIL Image to a NumPy array
    screenshot_np = np.array(inverted_image)

    # Define the new size for upscaling
    img_h, img_w = inverted_image.size
    new_size = (img_h * 3, img_w * 3)

    # Resize the image using OpenCV
    upscaled_img_np = cv2.resize(screenshot_np, new_size, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(upscaled_img_np, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 3)

    # Apply adaptive thresholding
    gray = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Define Tesseract configuration options
    custom_config = r'--oem 3 --psm 6'

    # Perform OCR on the processed image
    text = pytesseract.image_to_string(gray, config=custom_config)

    # Print the extracted text
    print(text)

    # Convert the processed NumPy array back to a PIL Image
    upscaled_img = Image.fromarray(gray)

    # Display the upscaled image

if __name__ == "__main__":
    index = 0
    main(index)
