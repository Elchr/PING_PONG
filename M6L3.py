from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height): #THIS CHANGES
       super().__init__()  #THIS CHANGES
       self.image = transform.scale(image.load(player_image), (wight, height))   #THIS CHANGES #e.g. 55,55 - parameters
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:   #THIS CHANGES
           self.rect.y -= self.speed   #THIS CHANGES
       if keys[K_DOWN] and self.rect.y < win_height - 80:   #THIS CHANGES
           self.rect.y += self.speed   #THIS CHANGES
   def update_l(self): #THIS IS EXTRA INSTEAD OF FIRE
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
back = (200, 255, 255) #background colour
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back) #fill background with colour of line 29


#flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60
 
#creating ball and paddles   
racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
 

 
while game:    
   for e in event.get():
       if e.type == QUIT:
           game = False
  

 
       racket1.reset()
       racket2.reset()
       ball.reset()
 
   display.update()
   clock.tick(FPS)
 