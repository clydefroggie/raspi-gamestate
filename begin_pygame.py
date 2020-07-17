import pygame

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 500, 300

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("First game")
bkg = pygame.image.load('sprites/bkg_1.png')

clock = pygame.time.Clock()

class Pusher (pygame.sprite.Sprite):
    def __init__(self, width, height, bot=False):
        super().__init__()
        
        self.width, self.height = width, height
        
        self.vel = 5  
        
        self.image = pygame.Surface([self.width, self.height])
        BLACK = (0,0,0)
        self.image.fill(BLACK)
        
        pygame.draw.rect(self.image, BLACK,[0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
        
        self.x_pos = self.rect[0]
        self.y_pos = self.rect[1]
#    def get_x_pos(self):
#        return self.rect[0]
#    
#    def get_y_pos(self):
#        return self.rect[1]
#    def draw(self, win):
#        pass
#        pygame.draw.rect(self.img, (255,255,0),[self.x, self.y, self.width, self.height])
#        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))                

class Puck (object):
    #todo: check how to do inheritence
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width, self.height = width, height        
        
        self.vel = 6
        self.x_dir, self.y_dir = 1, 1
        
    def update_x_dir(self):
        self.x_dir *= -1
    
    def update_y_dir(self):
        self.y_dir *= -1
    
    def update_movement(self):
        self.x_pos += (self.vel * self.x_dir)
        self.y_pos += (self.vel * self.y_dir)
        
    def draw(self, win):
        self.update_movement()
        pygame.draw.rect(win, (0, 255, 255), (self.x_pos, self.y_pos, self.width, self.height))
        
        
def redrawGameWindow():   
    win.blit(bkg, (0, 0))
#    player_one.draw(win)
#    puck.draw(win)
    pygame.display.flip()
    list_all_sprites.draw(win)
    pygame.display.update()

#mainloop

player_one = Pusher(20, 64)
player_one.rect = (100, 100)

puck = Puck(150, 150, 5, 5)

list_all_sprites = pygame.sprite.Group()
list_all_sprites.add(player_one)

run = True
while run:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
#    x_pos, y_pos = player_one.rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if (player_one.y_pos - player_one.vel) < 0:
            player_one.y_pos = 0 
        else:
            player_one.y_pos -= player_one.vel
#    if keys[pygame.K_DOWN]:
#        if (player_one.rect.y + player_one.height + player_one.vel) > WIN_HEIGHT:
#            player_one.rect.y = WIN_HEIGHT - player_one.height
#        else:
#            player_one.rect.y += player_one.vel
#
#    if (puck.x_pos + puck.width) > WIN_WIDTH:
#        puck.update_x_dir()
#    if puck.y_pos < 0 or (puck.y_pos + puck.height) > WIN_HEIGHT:
#        puck.update_y_dir()
# 
#    if puck.x_pos <= (player_one.x + player_one.width):
#        puck.update_x_dir()
#        if not (puck.y_pos >= (player_one.y - puck.height) and puck.y_pos <= (player_one.y + player_one.height + puck.height)):
#            print("NOK")
#    
    redrawGameWindow()
    
pygame.quit()