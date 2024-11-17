import pygame #the main import
import constants as const
import player as p
import asteroids as aster
import asteroidfield as asfield
import shots as sh
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    #sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # update containers
    p.Player.containers = (updateable, drawable)
    aster.Asteroid.containers = (asteroids, updateable, drawable)
    asfield.AsteroidField.containers = (updateable)
    sh.Shot.containers = (shots, updateable, drawable)

    player = p.Player((const.SCREEN_WIDTH / 2), (const.SCREEN_HEIGHT / 2))



    screen = pygame.display.set_mode(size=(const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    print("Starting asteroids!")
    while True:
        #Quit the game if instructed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for object in updateable:
            object.update(dt)

        #Check for collisionsa
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()

        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        #Use the screen.fill method to fill the screen w/ black
        screen.fill(color="black")

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