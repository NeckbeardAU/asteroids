import pygame #the main import
import constants as const
import player as p

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = p.Player((const.SCREEN_WIDTH / 2), (const.SCREEN_HEIGHT / 2))

    screen = pygame.display.set_mode(size=(const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        #Use the screen.fill method to fill the screen w/ black
        screen.fill(color="black")
        player.draw(screen)
        #Use pygames display.flip() to refresh the screen
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)


#    Delete later
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()