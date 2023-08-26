from settings import *

class Ministro(pygame.sprite.Sprite):
    def __init__(self): 								
        pygame.sprite.Sprite.__init__(self)				
        self.image = pygame.image.load('images/flavio-dino.png') 
        self.image = pygame.transform.scale(self.image, (76, 110))
        self.rect = self.image.get_rect()			
        self.rect.centerx = WIDTH/2					
        self.rect.centery = HEIGHT-35

    def moverMinistro(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.rect.left > 0: 
                self.rect.move_ip([-PLAYER_SPEED,0])
                
        if keys[pygame.K_RIGHT]:
            if self.rect.right < WIDTH:
                self.rect.move_ip([PLAYER_SPEED,0])