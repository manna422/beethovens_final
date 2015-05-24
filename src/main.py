import pygame
from time import sleep
import beethoven as bto
import math
from pleb import Pleb

class Game(object):
    FRAMES_PER_SECOND = 60
    clock = pygame.time.Clock()
    def __init__(self, width, height, fullscreen):
        self.running = True

        pygame.init()
        pygame.display.set_caption('Beethoven\'s Final')
        
        self.width = width
        self.height = height
        self.charSize = 120
        if (fullscreen):
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))
            # self.screen = pygame.display.set_mode((self.width, self.height))

        self.colors = {}
        self.colors['GREEN'] = (0, 255, 0)
        self.colors['RED'] = (255, 0, 0)
        self.colors['GREY'] = (127, 127, 127)

        self.screen.fill(self.colors['GREEN'])

        self.keyDelay = 0.03

        self.beethoven = bto.Beethoven(self)

        pygame.display.flip()

        print "init done"

    def run(self):
        while self.running:
            self.screen.fill(self.colors['GREEN'])
            # clock
            self.clock.tick(self.FRAMES_PER_SECOND)
            # input handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.beethoven.attackDirection(bto.Direction.Left)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.beethoven.attackDirection(bto.Direction.Right)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.beethoven.attackDirection(bto.Direction.Up)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.beethoven.attackDirection(bto.Direction.Down)
                else:
                    self.beethoven.attackDirection(bto.Direction.Rest)

def main():

    WIDTH = 640
    HEIGHT = 640
    FULLSCREEN = False

    game = Game(WIDTH, HEIGHT, FULLSCREEN)
    game.run()

if __name__ == '__main__':
    main()
