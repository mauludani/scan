import pyautogui
from PIL import Image

def capture_screen_area(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

# Contoh pemanggilan fungsi capture_screen_area dengan koordinat (left, top) dan ukuran (width, height) yang diinginkan
left = 0
top = 100
width = 200
height = 680

screenshot = capture_screen_area(left, top, width, height)
screenshot.show()  # Tampilkan tangkapan layar dalam jendela pop-up
