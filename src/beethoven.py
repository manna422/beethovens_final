import pygame

class Direction:
    Rest = 0
    Up = 2
    Down = 1
    Right = 4
    Left = 3

class Beethoven(pygame.sprite.GroupSingle):
    def __init__(self, game):
        pygame.sprite.GroupSingle.__init__(self)
        self.game = game
        self.rest = True
        self.beethovenSprites = [BeethovenSprite(self, dir) for dir in range(5)]
        self.attackDirection(Direction.Rest)

    def attackDirection(self, direction):
        if direction == 0:
            self.rest = True
        else:
            self.rest = False
        beethovenSprite = self.beethovenSprites[direction]
        self.add(beethovenSprite)
        sprite = pygame.sprite.spritecollideany(self.beethovenSprites[0], self.game.pleb_group)
        if (sprite):
            if sprite.direction == (direction - 1):
                #sprite.kill()
                self.game.score += 1
                sprite.flyAway()
        self.update()
        # TODO: kill the pleb in this direction

    def update(self): # flicker issue
        self.draw(self.game.screen)
        pygame.display.flip()


class BeethovenSprite(pygame.sprite.Sprite):
    def __init__(self, beethoven, direction):
    	pygame.sprite.Sprite.__init__(self)
        self.beethoven = beethoven
        self.direction = direction
        self.charSize = beethoven.game.charSize
        lungeDist = 10

        self.rect = pygame.Rect((beethoven.game.width - self.charSize)/2, (beethoven.game.height- self.charSize)/2, self.charSize, self.charSize);
        
        if direction == Direction.Rest:
            self.image = pygame.transform.scale(pygame.image.load("../resources/BeethovenRest.png"), (self.charSize, self.charSize))
        elif direction == Direction.Up:
            self.rect.move_ip(0, -lungeDist)
            self.image = pygame.transform.scale(pygame.image.load("../resources/BeethovenBack.png"), (self.charSize, self.charSize))
        elif direction == Direction.Down:
            self.rect.move_ip(0, lungeDist)
            self.image = pygame.transform.scale(pygame.image.load("../resources/BeethovenFront.png"), (self.charSize, self.charSize))
        elif direction == Direction.Left:
            self.rect.move_ip(-lungeDist, 0)
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("../resources/BeethovenSide.png"), (self.charSize, self.charSize)), True, False)
        elif direction == Direction.Right:
            self.rect.move_ip(lungeDist, 0)
            self.image = pygame.transform.scale(pygame.image.load("../resources/BeethovenSide.png"), (self.charSize, self.charSize))
        
