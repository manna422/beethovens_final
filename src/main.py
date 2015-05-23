import pygame

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
        pygame.display.flip()

    def run(self):
        print self.running
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False


def main():
     game = Game()
     game.run()

if __name__ == '__main__':
    main()
