import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_ascii(ascii_img: [str]) -> None:
    for row in ascii_img:
        print(row)
