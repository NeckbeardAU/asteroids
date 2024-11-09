import pygame #the main import
import constants as const
import player as p

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    p.Player.containers = (updateable, drawable)
    player = p.Player((const.SCREEN_WIDTH / 2), (const.SCREEN_HEIGHT / 2))




    screen = pygame.display.set_mode(size=(const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    print("Starting asteroids!")
    while True:
        #Quit the game if instructed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Use the screen.fill method to fill the screen w/ black
        screen.fill(color="black")
            
        #Draw and update objects as required.  
        for object in updateable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)


        #Use pygames display.flip() to refresh the screen
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)


#    Delete later
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()