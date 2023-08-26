from settings import *

class Fundo(pygame.sprite.Sprite):
	def __init__(self,img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img)
		self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/2
		self.rect.centery = HEIGHT/2
