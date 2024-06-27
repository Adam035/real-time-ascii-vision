import cv2


class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()

    def capture_gray_image(self) -> [[int]]:
        success, img = self.cap.read()
        img = cv2.flip(img, 1)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img
