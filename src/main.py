import pygame
from time import sleep
import beethoven as bto
import math
from pleb import PlebSprite
from menu import Menu #credit from http://czajnikmorderca.pl

class Game(object):
    FRAMES_PER_SECOND = 60
    clock = pygame.time.Clock()
    def __init__(self, width, height, fullscreen, song):
        self.running = True

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Beethoven\'s Beats')
        
        self.width = width
        self.height = height
        self.charSize = 120
        if (fullscreen):
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.width, self.height))

        self.font = pygame.font.Font(None, 100)
        self.highscoreFont = pygame.font.SysFont("monospace", 30)
        self.score = 0
        self.highscore = 0
        self.colors = {}
        self.colors['GREEN'] = (0, 255, 0)
        self.colors['RED'] = (255, 0, 0)
        self.colors['GREY'] = (127, 127, 127)
        self.colors['FONT'] = (64, 127, 64)
        self.pleb_index = 0
        self.background = pygame.image.load("../resources/NewBackground.png")
        self.backgroundRect  = self.background.get_rect()
        self.screen.blit(self.background, self.backgroundRect)
        #self.screen.fill(self.colors['GREEN'])
        self.pleb_list = []
        self.load_level(song)
        self.alive = True # Beethoven
        self.pleb_group = pygame.sprite.Group()
        self.plebImages = [
            pygame.transform.scale(pygame.image.load("../resources/PlebBack.png"), (self.charSize, self.charSize)), 
            pygame.transform.scale(pygame.image.load("../resources/PlebFront.png"), (self.charSize, self.charSize)), 
            pygame.transform.flip(pygame.transform.scale(pygame.image.load("../resources/PlebSide.png"), (self.charSize, self.charSize)), True, False), 
            pygame.transform.scale(pygame.image.load("../resources/PlebSide.png"), (self.charSize, self.charSize)), 
        ]
        #self.spawnPleb(0)
        #self.spawnPleb(1)
        #self.spawnPleb(2)
        #self.spawnPleb(3)
        self.keyDelay = 0.03

        self.beethoven = bto.Beethoven(self)

        #pygame.display.flip()

    def load_level(self, filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(1)
        mdata_file = filename + '.mdata'
        with open(mdata_file) as f:
            lines = f.readlines()
            for line in lines:
                self.pleb_list.append((line[-2], int(line[:-3])))

    def run(self):
        pygame.mixer.music.play() 
        self.startTime = pygame.time.get_ticks()
        self.pleb_index = 0
        while self.running:
            self.screen.blit(self.background,  self.backgroundRect)
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
                    # self.spawnPleb(3)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.beethoven.attackDirection(bto.Direction.Right)
                    # self.spawnPleb(2)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.beethoven.attackDirection(bto.Direction.Up)
                    # self.spawnPleb(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.beethoven.attackDirection(bto.Direction.Down)
                    # self.spawnPleb(1)
                elif self.beethoven.rest == False: # to fix flicker issue
                    self.beethoven.attackDirection(bto.Direction.Rest)

            elapsedTime = pygame.time.get_ticks() - self.startTime
            try:
                if elapsedTime >= (self.pleb_list[self.pleb_index][1] - 950*self.width/(2*3)/60):
                    item = self.pleb_list[self.pleb_index]
                    self.pleb_index = self.pleb_index + 1
                    if item[0] == 'a':
                        self.spawnPleb(0)
                    elif item[0] == 'b':
                        self.spawnPleb(1)
                    elif item[0] == 'c':
                        self.spawnPleb(2)
                    elif item[0] == 'd':
                        self.spawnPleb(3)
            except IndexError:
                pass

            if self.alive == False:
                self.restart()

            # Rendering
            self.pleb_group.update(deltat)
            self.pleb_group.draw(self.screen)
            self.beethoven.update()

            score_texture = self.font.render(str(self.score), 1, self.colors['FONT'])
            self.screen.blit(score_texture, (20, 20))
            score_texture = self.font.render(str(self.highscore), 1, self.colors['FONT'])
            self.screen.blit(score_texture, (600, 20))
            score_texture = self.highscoreFont.render("highscore",1,self.colors['FONT'])
            self.screen.blit(score_texture, (600, 100))
            pygame.display.flip()

            
    def spawnPleb(self, direction):
        pleb = PlebSprite(self, self.plebImages[direction], direction)
        self.pleb_group.add(pleb)

    def restart(self):
        self.screen.blit(self.background,  self.backgroundRect)
        if self.score > self.highscore:
            self.highscore = self.score
            score_texture = self.font.render("new highscore!",1,self.colors['RED'])
            self.screen.blit(score_texture, (150, 450))
        self.beethoven.attackDirection(bto.Direction.Dead)
        score_texture = self.font.render(str(self.score), 1, self.colors['RED'])
        self.screen.blit(score_texture, (20, 20))
        pygame.display.flip()
        pygame.mixer.music.fadeout(3000)
        pygame.time.delay(3000)
        pygame.mixer.music.rewind() 
        self.startTime = pygame.time.get_ticks()
        self.pleb_index = 0
        self.score = 0
        self.alive = True
        for sprite in self.pleb_group:
            sprite.kill()
        self.beethoven.attackDirection(bto.Direction.Rest)
        pygame.display.flip()
        pygame.mixer.music.play()

def main():

    WIDTH = 800
    HEIGHT = 800
    FULLSCREEN = True
    ode = '../resources/song.ogg'
    overture = '../resources/song1.ogg'
    moonlight = '../resources/song2.ogg'

    if (FULLSCREEN):
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((51,51,51))




    menu = Menu()
    menu.init(['Start', 'Quit'], screen)
    menu.draw(0)
    pygame.display.update()

    pygame.mixer.init()
    pygame.mixer.music.load('../resources/tuning_warmup.mp3')
    pygame.mixer.music.set_volume(2)
    pygame.mixer.music.play()

    pick = menu.run()

    while 1:
        if (pick == 1):
            menu = Menu()
            menu.init(['Start', 'Quit'], screen)
            menu.draw(0)
            pygame.display.update()
            pick = menu.run()
            if (pick == 1):
                menu = Menu()
                menu.init(['Ode To Joy','The Creatures of Prometheus','Moonlight Sonata mov 3','Quit'], screen)
                menu.draw(0)
                pygame.display.update()
                pick2 = menu.run()
                if (pick2 == 1):
                    game = Game(WIDTH, HEIGHT, FULLSCREEN, ode)
                    game.run()
                elif (pick2 == 2):
                    game = Game(WIDTH, HEIGHT, FULLSCREEN, overture)
                    game.run()
                elif (pick2 == 3):
                    game = Game(WIDTH, HEIGHT, FULLSCREEN, moonlight)
                    game.run()
            elif (pick == 2):
                break



if __name__ == '__main__':
    main()
