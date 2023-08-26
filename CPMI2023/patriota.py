from settings import *
from ovo import Ovo
from random import randint 

class Patriota(pygame.sprite.Sprite):
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.image = pygame.transform.scale(self.image, (66, 100))					
		self.rect = self.image.get_rect()
		self.rect.centerx = randint(50,WIDTH-50)
		self.rect.centery = randint(35,HEIGHT/2-5)
		self.speed = [randint(-4,4),randint(-2,2)]	

	def tacarOvos(self):
		return Ovo(self.rect)

	def update(self, tempo):
		self.rect.move_ip(self.speed)					

		if tempo==0: 
			self.speed[0] = randint(-4,4)
			self.speed[1] = randint(-2,2)

		if self.rect.centerx > WIDTH or self.rect.centerx < 0: 
			self.speed[0] = -self.speed[0] 
		if self.rect.top < 0 or self.rect.bottom > (HEIGHT/1.5):
			self.speed[1] = -self.speed[1]
	
		
