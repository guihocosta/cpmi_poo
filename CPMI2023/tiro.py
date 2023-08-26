from settings import *

class Tiro(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/algema.png')
		self.image = pygame.transform.scale(self.image, (58, 58))	
		self.rect = self.image.get_rect()
		self.rect.centery = HEIGHT-70
		self.speed = [0,0]

	def update(self,objetos,tiros, colisao):
		self.rect.move_ip(self.speed)

		if self.rect.bottom < 0: 
			self.rect.centery = HEIGHT-70				
			self.speed = [0,0]							
			if self in objetos: objetos.remove(self) 						
			return tiros+1

		elif colisao:
			self.rect.centery = HEIGHT-70				
			self.speed = [0,0]
			objetos.remove(self)		
			return tiros + 1
		
		return tiros
