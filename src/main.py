import pygame
from time import sleep

class Game(object):
    def __init__(self):
        self.running = True

        pygame.init()
        pygame.display.set_caption('Beethoven\'s Final')
        
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.colors = {}
        self.colors['GREEN'] = (0, 255, 0)
        self.colors['RED'] = (255, 0, 0)
        self.colors['GREY'] = (127, 127, 127)

        self.screen.fill(self.colors['GREEN'])

        self.beethovenRect = pygame.Rect(390, 390, 20, 20);
        pygame.draw.rect(self.screen, self.colors['GREY'], self.beethovenRect);
        
        self.keyDelay = 0.03;

        pygame.display.flip()

    def run(self):
        print self.running
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.drawAttack(-20, 0);
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.drawAttack(20, 0);
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.drawAttack(0, -20);
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.drawAttack(0, 20);

    def drawAttack(self, x, y):
        leftRect = self.beethovenRect.move(x, y);
        pygame.draw.rect(self.screen, self.colors['RED'], leftRect);
        pygame.display.flip();
        sleep(self.keyDelay);
        pygame.draw.rect(self.screen, self.colors['GREEN'], leftRect);
        pygame.display.flip();



def main():
     game = Game()
     game.run()

if __name__ == '__main__':
    main()
