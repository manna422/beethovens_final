import pygame
import math
from pleb import PlebSprite

class Game(object):
    FRAMES_PER_SECOND = 60
    clock = pygame.time.Clock()
    def __init__(self, width, height, fullscreen):
        self.running = True

        pygame.init()
        pygame.display.set_caption('Beethoven\'s Final')
        
        self.width = width
        self.height = height
        if (fullscreen):
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))

        self.colors = {}
        self.colors['GREEN'] = (0, 255, 0)
        self.colors['RED'] = (255, 0, 0)
        self.colors['GREY'] = (127, 127, 127)

        self.alive = True # Beethoven

        self.pleb_group = pygame.sprite.Group()

        self.screen.fill(self.colors['GREEN'])
        self.spawnPleb("UP")
    def run(self):
        while self.running:
            self.screen.fill(self.colors['GREEN'])
            # clock
            deltat = self.clock.tick(self.FRAMES_PER_SECOND)
            # input handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            # Rendering
            self.pleb_group.update(deltat)
            self.pleb_group.draw(self.screen)
            pygame.display.flip()
            
    def spawnPleb(self, direction_string):
        pleb = PlebSprite(self, "../resources/orange_square.png", direction_string)
        self.pleb_group.add(pleb)

def main():

    WIDTH = 800
    HEIGHT = 800
    FULLSCREEN = False

    game = Game(WIDTH, HEIGHT, FULLSCREEN)
    game.run()

if __name__ == '__main__':
    main()
