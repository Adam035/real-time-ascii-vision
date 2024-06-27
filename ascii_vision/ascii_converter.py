import numpy as np

symbols = ".,-+*=#@$"


def _aggregate_image(img: np.ndarray, block_width: int = 8, block_height: int = 16) -> np.ndarray:
    height, width = img.shape
    new_width = width // block_width
    new_height = height // block_height
    aggregated_img = np.zeros((new_height, new_width), dtype=int)
    for i in range(new_height):
        for j in range(new_width):
            block = img[i*block_height:(i+1)*block_height, j*block_width:(j+1)*block_width]
            aggregated_img[i, j] = np.mean(block)
    return aggregated_img


def convert2ascii(img: np.ndarray) -> [str]:
    aggregated_img = _aggregate_image(img)
    ascii_img = []
    for i in range(aggregated_img.shape[0]):
        row = ""
        for j in range(aggregated_img.shape[1]):
            intensity = aggregated_img[i, j]
            symbol_index = intensity * (len(symbols) - 1) // 255
            row += symbols[symbol_index]
        ascii_img.append(row)
    return ascii_img
