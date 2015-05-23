import pygame
from enum import Enum

class DirectionEnum(Enum):
	Rest = 0
	Up = 1
	Down = 2
	Left = 3
	Right = 4


class Beethoven(pygame.sprite.GroupSingle):
	def __init__(self, game):
		self.game = game
		self.sprites = [BeethovenSprite(self, dir) for dir in DirectionEnum]
		self.attackDirection(DirectionEnum.Rest)

	def attackDirection(direction):
		self.add(self.sprites[direction])
		self.update()
		self.draw(game.screen)
		# TODO: kill the pleb in this direction

class BeethovenSprite(pygame.sprite.Sprite):
    def __init__(self, beethoven, direction):
        self.beethoven = beethoven
        self.direction = direction
        self.rect = (300, 300, 20, 20);

        if direction == DirectionEnum.Up:
        	self.image = ""
        elif direction == DirectionEnum.Down:
        	self.image = ""
        elif direction == DirectionEnum.Left:
        	self.image = ""
        elif direction == DirectionEnum.Right:
        	self.image = ""

