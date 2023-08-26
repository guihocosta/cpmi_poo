import sys
import pygame
import os

size = width, height = 400, 500

class Plataforma(pygame.sprite.Sprite):
	"""Classe para a plataforma"""
	def __init__(self, startpos, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img)
		self.rect = self.image.get_rect()
		self.rect.center = startpos

class Bola(pygame.sprite.Sprite):
	"""Classe para a bola"""
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/wilson.gif')
		self.rect = self.image.get_rect()
		self.rect.center = startpos
		self.speed = [2,2]

	def update(self):
		self.rect.move_ip(self.speed)

		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = -self.speed[0]

		if self.rect.bottom > height:
			self.rect.center = (width/2, 50)
			self.speed[0] = abs(self.speed[0]) + 1
			self.speed[1] = self.speed[1] + 1

		if self.rect.top < 0:
			self.rect.center = (width/2, height - 50)
			self.speed[0] = abs(self.speed[0]) + 1
			self.speed[1] = - (abs(self.speed[1]) + 1)

def moverPlataformas(key, p1, p2):
	if key == pygame.K_LEFT:
		if p1.rect.left > 0: 
			p1.rect.move_ip([-1,0])
	if key == pygame.K_RIGHT:
		if p1.rect.right < width:
			p1.rect.move_ip([1,0])

	if key == pygame.K_a:
		if p2.rect.left > 0: 
			p2.rect.move_ip([-1,0])
	if key == pygame.K_d:
		if p2.rect.right < width:
			p2.rect.move_ip([1,0])

def main():
	pygame.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	screen = pygame.display.set_mode(size)
	pygame.key.set_repeat(1,1)
	pygame.display.set_caption('Ping!')
	clock = pygame.time.Clock()

	# Carregando a imagem de fundo
	background = pygame.image.load("images/campo.gif")

	# Criando um objeto para a bola
	b = Bola((width/2, 50))

	# Criando um objeto para a plataforma
	p1 = Plataforma((width/2, height-5), 'images/red.gif')
	p2 = Plataforma((width/2, 5), 'images/blue.gif')

	plataformas = pygame.sprite.Group()
	plataformas.add(p1)
	plataformas.add(p2)

	# Selecionando a musica de fundo
	pygame.mixer.music.load("music/mario.mp3")
	pygame.mixer.music.play(-1)

	while abs(b.speed[0]) < 10:
		clock.tick(120) # Jogo nao vai rodar a mais de 120 frames por segundo

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# Se fechar usuario a janela
				print ('Bye')
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# Se pressionar alguma tecla
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
					# Tecla pressionada eh ESC ou Q
					print ('Bye')
					sys.exit()
				moverPlataformas(event.key, p1, p2)

		# Atualizando os objetos
		b.update()
		#plataformas.update() # Nao eh necessario (movimentam atraves do teclado)
		
		colisoes = pygame.sprite. spritecollide (b, plataformas , False)
		if len(colisoes) > 0:
			b.speed[1] = -b.speed[1]

		# Desenhando os objetos
		screen.blit(background, (0, 0))
		screen.blit(b.image, b.rect)
		plataformas.draw(screen)
		pygame.display.update()

main()

