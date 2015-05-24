import pygame
import math
from pleb import Pleb

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

        self.load_level('../resources/song.mp3')


    def load_level(self, filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(1)
        mdata_file = filename + '.mdata'
        with open(mdata_file) as f:
            lines = f.readlines()
            for line in lines:
                self.pleb_list.append((line[-2], line[:-3]))

    def run(self):
        # self.level_track.play()
        pygame.mixer.music.play()
        while self.running:
            # clock
            self.clock.tick(self.FRAMES_PER_SECOND)
            # input handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False


            # Rendering
            self.screen.fill(self.colors['GREEN'])
            pygame.display.flip()

def main():

    WIDTH = 800
    HEIGHT = 800
    FULLSCREEN = False

    game = Game(WIDTH, HEIGHT, FULLSCREEN)
    game.run()

if __name__ == '__main__':
    main()
