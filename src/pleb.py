import pygame
import random
class PlebSprite(pygame.sprite.Sprite):
    def __init__(self, game, image, direction):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.VELOCITY = 3
        self.image = image
        self.rect = self.image.get_rect() #messed up
        self.direction = direction
        self.alive = True
        if direction == 0:
            self.xdirection = 0
            self.ydirection = -1
            self.position = (self.game.width/2, self.game.height)
        elif direction == 1:
            self.xdirection = 0
            self.ydirection = 1
            self.position = (self.game.width/2, 0)
        elif direction == 2:
            self.xdirection = 1
            self.ydirection = 0
            self.position = (0, self.game.height/2)
        else:
            self.xdirection = -1
            self.ydirection = 0
            self.position = (self.game.width, self.game.height/2)

    def update(self, deltat):
        # SIMULATION
        x, y = self.position
        x += self.VELOCITY * self.xdirection
        y += self.VELOCITY * self.ydirection
        self.position = (x, y) 
        self.rect.center = self.position

        # collision detection
        if (self.alive):
            if self.xdirection and abs(self.position[0] - self.game.width/2) <= 50:
                self.kill()
                self.game.alive = False
            elif self.ydirection and abs(self.position[1] - self.game.height/2) <= 50:
                self.kill()
                self.game.alive = False
        else:
            x, y = self.position
            if (abs(x) > 1000 or abs(y)> 1000):
                self.kill()

    def flyAway(self):
        self.alive = False
        self.VELOCITY = random.randint(5, 40)
        if self.direction == 0:
            self.xdirection = random.randint(-5,5)
            self.ydirection = random.randint(1,5)
            x, y = self.position
            y += 50
            self.rect.center = (x, y)
        elif self.direction == 1:
            self.xdirection = random.randint(-5,5)
            self.ydirection = random.randint(-5,-1)
            x, y = self.position
            y -= 50
            self.rect.center = (x, y)
        elif self.direction == 2:
            self.xdirection = random.randint(-5,-1)
            self.ydirection = random.randint(-5,5)
            x, y = self.position
            x -= 50
            self.rect.center = (x, y)
        else:
            self.xdirection = random.randint(1,5)
            self.ydirection = random.randint(-5,5)
            x, y = self.position
            x += 50
            self.rect.center = (x, y)