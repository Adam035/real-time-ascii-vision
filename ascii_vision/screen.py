import pygame
from ascii_vision import Camera
from ascii_vision import convert2ascii

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Screen:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        pygame.init()
        pygame.display.set_caption("Real Time ASCII Vision")
        self.display = pygame.display.set_mode((self.width, self.height))
        self.camera = Camera()
        self.clock = pygame.time.Clock()

    def _draw_text(self, text: str, font_size: int) -> None:
        font = pygame.font.Font("assets/consola.ttf", font_size)
        lines = text.splitlines()
        y = 0
        for line in lines:
            text_surface = font.render(line, True, WHITE)
            text_rect = text_surface.get_rect(topleft=(0, y))
            self.display.blit(text_surface, text_rect)
            y += font_size

    def paint(self, font_size: int, fps: int = 60) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.display.fill(BLACK)
            text = convert2ascii(self.camera.capture_gray_image())
            self._draw_text(text, font_size)
            pygame.display.flip()
            self.clock.tick(fps)
        pygame.quit()
