from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Screen width: {SCREEN_WIDTH}")

if __name__ == "__main__":
    main()
