import pygame

class PlebSprite(pygame.sprite.Sprite):
    def __init__(self, game, image, direction_string):
        self.game = game
        self.VELOCITY = 5
        self.image = image
        if direction_string == "UP":
            self.xdirection = 0
            self.ydirection = -1
            self.position = (self.game.width/2, self.game.height)
        elif direction_string == "DOWN":
            self.xdirection = 0
            self.ydirection = 1
            self.position = (self.game.width/2, 0)
        elif direction_string == "RIGHT":
            self.xdirection = 1
            self.ydirection = 0
            self.position = (0, self.game.height/2)
        else:
            self.xdirection = -1
            self.ydirection = 0
            self.position = (self.game.width, self.game.height/2)

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.image).convert_alpha() #messed up

    def update(self, deltat):
        # SIMULATION
        x, y = self.position
        x += self.VELOCITY * self.xdirection
        y += self.VELOCITY * self.ydirection
        self.position = (x, y)
        self.rect = self.image.get_rect() #messed up
        self.rect.center = self.position

        # collision detection
        if self.xdirection and abs(self.position[0] - self.game.width/2) <= 50:
            self.kill()
        elif self.ydirection and abs(self.position[1] - self.game.height/2) <= 50:
            self.kill()