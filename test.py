import pyautogui
import requests
import time
import sys
from pytesseract import pytesseract
from PIL import Image, ImageOps
from io import BytesIO

def capture_screen_area(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

def main(index, coin: str):
    # Contoh pemanggilan fungsi capture_screen_area dengan koordinat (left, top) dan ukuran (width, height) yang diinginkan
    left = 0
    top = 160
    width = 76
    height = 600

    screenshot = capture_screen_area(left, top, width, height)
    # screenshot.show()  # Tampilkan tangkapan layar dalam jendela pop-up

    # Convert screenshot to bytes
    buffer = BytesIO()
    if screenshot.mode != 'RGB':
        screenshot = screenshot.convert('RGB')

    # screenshot = ImageOps.invert(screenshot)
    screenshot.save(buffer, format="PNG")
    buffer.seek(0)

    # Define your backend URL to upload the screenshot
    backend_url = "http://127.0.0.1:8000/api/upload"

    # Set up the files parameter with the screenshot
    files = {'file': buffer}
    textt = pytesseract.image_to_string(screenshot)

    data = {
        'text': textt,
        'coin': coin,
    }
    # print(text)
    # Make a POST request to upload the screenshot
    response = requests.post(backend_url, data=data)

    print('--start--')
    print(' ')
    print(textt)
    # Check the response
    if response.status_code == 200:
        print(index)
        # print(coin)
    else:
        print("Error : ", response.content)

    print(' ')
    print('--end--')
    print(' ')
if __name__ == "__main__":
    index = 0
    while True:
        index = index + 1
        main(index, coin= sys.argv[1])
        time.sleep(1)