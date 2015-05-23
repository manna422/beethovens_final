import pygame
import math

WIDTH = 800
HEIGHT = 800
FULLSCREEN = False

class plebSprite(pygame.sprite.Sprite):
    VELOCITY = 5
    def __init__(self, image, position, xdirection, ydirection):
        pygame.sprite.Sprite.__init__(self)
        self.scr_image = pygame.image.load(image)
        self.position = position
        self.xdirection = xdirection
        self.ydirection = ydirection

    def update(self, deltat):
        # SIMULATION
        x, y = self.position
        x += self.VELOCITY * self.xdirection
        y += self.VELOCITY * self.ydirection
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class pleb(object):
    def __init__(self, direction_string):
        if direction_string == "UP":
            self.xdirection = 0
            self.ydirection = -1
            self.position = (WIDTH)
        self.direction 

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

        self.screen.fill(self.colors['GREEN'])

    def run(self):
        while self.running:
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
    game = Game(WIDTH, HEIGHT, FULLSCREEN)
    game.run()

if __name__ == '__main__':
    main()
