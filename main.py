from ascii_vision.camera import Camera
from ascii_vision.ascii_converter import convert2ascii
from ascii_vision.display import display_ascii, clear_terminal
from time import sleep

if __name__ == '__main__':
    camera = Camera()
    while True:
        img = camera.capture_gray_image()
        if img is not None:
            ascii_img = convert2ascii(img)
            display_ascii(ascii_img)
            sleep(0.01)
            clear_terminal()
