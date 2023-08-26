import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = (800,600)		
PLAYER_SPEED = 5
BULLET_SPEED = 5		
screen = pygame.display.set_mode(SIZE)
pygame.mouse.set_visible(False)			
font1 = pygame.font.Font(None, 40)					
black = 0, 0, 0	
pygame.display.set_caption('Atentado!') 
