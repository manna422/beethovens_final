class PlebSprite(pygame.sprite.Sprite):
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

class Pleb(object):
    def __init__(self, game, direction_string):
        self.game = game
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
        else
            self.xdirection = -1
            self.ydirection = 0
            self.position = (self.game.width, self.game.height/2)