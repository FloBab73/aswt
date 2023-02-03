import pygame
from src.core.BlockType import BlockType

class GameBlock (pygame.Rect):
	NON    = BlockType.NON
	WALL   = BlockType.WALL
	SECRET = BlockType.SECRET
	ITEM   = BlockType.ITEM

	def __init__(self, left, top, width, height, blockType=BlockType.NON):
		super().__init__(left, top, width, height)
		self._blockType = blockType

	@property
	def blockType(self):
		return self._blockType