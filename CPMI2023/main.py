import sys
from settings import *
from tiro import Tiro
from ministro import Ministro
from patriota import Patriota
from fundo import Fundo
from random import choice
				
class Game:
	def __init__(self):
		self.imagem_patriota1 = pygame.image.load('images/bolsonarista1.png')
		self.imagem_patriota2 = pygame.image.load('images/bolsonarista2.png')

		self.invasores = pygame.sprite.Group()
		for i in range(20):
			if i % 2 == 0:
				img = self.imagem_patriota1
			else:
				img = self.imagem_patriota2

			patriota = Patriota(img)
			self.invasores.add(patriota)

		self.m = Ministro()
		self.t = Tiro()

		self.objetos = [self.m]
		self.ovos = []
			
		self.clock = pygame.time.Clock()

		self.acertou = False
		self.perdeu = False
		self.tiros = 0
		self.tempo = 0
		self.temp = 240 
		self.flag = 23
		self.text = font1.render('Tiros Restantes: ' + str(10 - self.tiros), True, (0, 0, 0)) 
		self.background = pygame.image.load("images/background.jpg")
		self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

	def run(self):
		while self.tiros < self.flag:
			self.clock.tick(120)			
			self.tempo = (self.tempo+1)%self.temp

			if self.tempo == 0:
				if (self.temp-15) != 0:
					self.temp -= 15
					enemy = choice(self.invasores.sprites())
					self.ovos.append(enemy.tacarOvos())

			for event in pygame.event.get():							

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE and not self.t in self.objetos:
						self.t.speed = [0,-BULLET_SPEED]						
						self.t.rect.centerx = self.m.rect.centerx
						self.objetos.append(self.t) 		
					elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
						sys.exit()

				elif event.type == pygame.QUIT:
					sys.exit()

			self.m.moverMinistro()

			# Update Invasores
			for invasor in self.invasores.sprites():
				invasor.update(self.tempo)
			

			# Colisão
			for invasor in self.invasores.sprites():
				if (invasor.rect.colliderect(self.t.rect)) and self.t in self.objetos:
					pygame.mixer.music.load("audio/aiai.mp3")
					pygame.mixer.music.play(1)
					invasor.kill()
					self.tiros = self.t.update(self.objetos, self.tiros, True)

			self.tiros = self.t.update(self.objetos, self.tiros, False)

			# Aviso de Tiros Restantes
			if self.tiros <= 10: 
				text = font1.render('Tiros Restantes: ' + str(self.flag - self.tiros), True, (0, 0, 0))
			elif self.tiros <= 18: 
				text = font1.render('Tiros Restantes: ' + str(self.flag - self.tiros), True, (255, 150, 0))
			else: 
				text = font1.render('Tiros Restantes: ' + str(self.flag - self.tiros), True, (255, 0, 0))

			# Colisão de Ovos
			for ovo in self.ovos:
				if  self.m.rect.colliderect(ovo.rect): self.perdeu = True
			
			if self.perdeu or self.flag - self.tiros < len(self.invasores): break
					
			if len(self.invasores) == 0:
				self.acertou = True
				break


			# Desenhando os Objetos da Tela
			screen.fill(black)
			screen.blit(self.background, (0, 0))	
			self.invasores.draw(screen)
			
			# Desenhando Objetos na Tela
			for objeto in self.objetos: screen.blit(objeto.image, objeto.rect)
			
			for ovo in self.ovos:
				ovo.update(self.ovos)
				screen.blit(ovo.image, ovo.rect)

			screen.blit(text, (WIDTH - text.get_width(), 0))

			pygame.display.flip()

		if self.acertou: 
			self.f = Fundo('images/youwin.jpg')
			msc = "audio/youwin.mp3"
		else: 
			self.f = Fundo('images/gameover.jpg')
			msc = "audio/gameover.mp3"
			
		pygame.mixer.music.load(msc)
		pygame.mixer.music.play(-1)
		
		self.over()
		return
	
	def home(self):
		self.f = Fundo('images/home.png')
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE or event.key == pygame.K_q or event.key == pygame.K_RETURN: sys.exit()
					if event.key == pygame.K_SPACE:
						Game().run()
			
			screen.blit(self.f.image, self.f.rect)
			pygame.display.flip()

	def over(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE or event.key == pygame.K_q or event.key == pygame.K_RETURN: sys.exit()
					if event.key == pygame.K_r:
						pygame.mixer.music.pause()
						Game().run()


			screen.blit(self.f.image, self.f.rect)
			pygame.display.flip()
		

if __name__ == '__main__':
	Game().home()
