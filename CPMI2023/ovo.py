from settings import *

class Ovo(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/ovo.png')
		self.image = pygame.transform.scale(self.image, (65, 45))	
		self.rect = self.image.get_rect()
		self.rect.centerx = pos.x
		self.rect.centery = pos.y
		self.speed = [0,1]
	
	def update(self, ovos):
		self.rect.move_ip(self.speed)
		if self.rect.top > HEIGHT: 									
			ovos.remove(self) 	
