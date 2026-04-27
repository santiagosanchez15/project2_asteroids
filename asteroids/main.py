import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group() # create the groups
    drawable = pygame.sprite.Group()
    # player.containers(updatable, drawable) # another way to add gorups

    # addtion of groups to player object
    updatable.add(player) 
    drawable.add(player)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        #inclusing of movement with groups
        updatable.update(dt)
        for line in drawable:
            line.draw(screen)

        #previous inclusion of movement without groups
        # player.draw(screen)
        # player.update(dt)  # dt is passed to update which is the time taken


        pygame.display.flip()
        dt = clock.tick(60) / 1000 # dt acquaires the value of the time the the clock ticks (screen refreshes)
        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()
