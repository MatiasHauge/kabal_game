import pygame
import sys

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 600, 450
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(" The Kabal Game")

FPS = 60

# COLORS
WHITE_COL = (255, 255, 255)

def main_loop():

    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(FPS)
        WIN.fill(WHITE_COL)
        pygame.display.update()

if __name__ == '__main__':

    main_loop()