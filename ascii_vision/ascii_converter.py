import numpy as np

SYMBOLS = " .-,=+#@$"
BLOCK_WIDTH: int = 5
BLOCK_HEIGHT: int = 10


def _aggregate_image(img: np.ndarray) -> np.ndarray:
    height, width = img.shape
    new_width = width // BLOCK_WIDTH
    new_height = height // BLOCK_HEIGHT
    aggregated_img = np.zeros((new_height, new_width), dtype=int)
    for i in range(new_height):
        for j in range(new_width):
            block = img[i*BLOCK_HEIGHT:(i+1)*BLOCK_HEIGHT, j * BLOCK_WIDTH:(j + 1) * BLOCK_WIDTH]
            aggregated_img[i, j] = np.mean(block)
    return aggregated_img


def convert2ascii(img: np.ndarray) -> str:
    aggregated_img = _aggregate_image(img)
    text = ""
    for i in range(aggregated_img.shape[0]):
        for j in range(aggregated_img.shape[1]):
            intensity = aggregated_img[i, j]
            symbol_index = intensity * (len(SYMBOLS) - 1) // 255
            text += SYMBOLS[symbol_index]
        text += "\n"
    return text
