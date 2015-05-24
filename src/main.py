import pygame
from time import sleep
import beethoven as bto
import math
from pleb import PlebSprite

class Game(object):
    FRAMES_PER_SECOND = 60
    clock = pygame.time.Clock()
    def __init__(self, width, height, fullscreen):
        self.running = True

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Beethoven\'s Final')
        
        self.width = width
        self.height = height
        self.charSize = 120
        if (fullscreen):
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))

        self.colors = {}
        self.colors['GREEN'] = (0, 255, 0)
        self.colors['RED'] = (255, 0, 0)
        self.colors['GREY'] = (127, 127, 127)

        self.screen.fill(self.colors['GREEN'])
        self.pleb_list = []
        #self.load_level('../resources/song.mp3')
        self.alive = True # Beethoven
        self.pleb_group = pygame.sprite.Group()
        self.plebImages = [
            pygame.transform.scale(pygame.image.load("../resources/PlebBack.png"), (self.charSize, self.charSize)), 
            pygame.transform.scale(pygame.image.load("../resources/PlebFront.png"), (self.charSize, self.charSize)), 
            pygame.transform.flip(pygame.transform.scale(pygame.image.load("../resources/PlebSide.png"), (self.charSize, self.charSize)), True, False), 
            pygame.transform.scale(pygame.image.load("../resources/PlebSide.png"), (self.charSize, self.charSize)), 
        ]
        self.spawnPleb(0)
        self.spawnPleb(1)
        self.spawnPleb(2)
        self.spawnPleb(3)
        self.keyDelay = 0.03

        self.beethoven = bto.Beethoven(self)

        #pygame.display.flip()

        print "init done"

    def load_level(self, filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(1)
        mdata_file = filename + '.mdata'
        with open(mdata_file) as f:
            lines = f.readlines()
            for line in lines:
                self.pleb_list.append((line[-2], line[:-3]))

    def run(self):
        #self.level_track.play()
        #pygame.mixer.music.play() 
        while self.running:
            self.screen.fill(self.colors['GREEN'])
            # clock
            deltat = self.clock.tick(self.FRAMES_PER_SECOND)
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
                elif self.beethoven.rest == False: # to fix flicker issue
                    self.beethoven.attackDirection(bto.Direction.Rest)

            # Rendering
            self.pleb_group.update(deltat)
            self.pleb_group.draw(self.screen)
            self.beethoven.update()
            pygame.display.flip()
            
    def spawnPleb(self, direction):
        pleb = PlebSprite(self, self.plebImages[direction], direction)
        self.pleb_group.add(pleb)

def main():

    WIDTH = 640
    HEIGHT = 640
    FULLSCREEN = False

    game = Game(WIDTH, HEIGHT, FULLSCREEN)
    game.run()

if __name__ == '__main__':
    main()