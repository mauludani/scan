import cv2
import numpy as np
import pyautogui

def capture_screen(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

def capture_screen_area(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

def find_image_in_screen(screen, template):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val, max_loc

# Contoh penggunaan:
left = 0
top = 100
width = 200
height = 680

screenshot = capture_screen_area(left, top, width, height)

# Misalnya, kita ingin mencari logo Google di tangkapan layar
template_path = 'buy2.png'
template = cv2.imread(template_path)

match_threshold = 0.9  # Threshold untuk menentukan kecocokan

result, match_location = find_image_in_screen(screenshot, template)

pyautogui.moveTo(match_location[0], match_location[1])

ss = capture_screen(match_location[0] + 40, match_location[1] + 110, 100, 100)
ss.show() 

print(result)

# if result >= match_threshold:
#     print("Logo Google ditemukan pada posisi:", match_location)
# else:
#     print("Logo Google tidak ditemukan pada tangkapan layar.")
