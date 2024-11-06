import pygame #the main import
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Use the screen.fill method to fill the screen w/ black
        screen.fill(color="black")
        #Use pygames display.flip() to refresh the screen
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)


#    Delete later
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()