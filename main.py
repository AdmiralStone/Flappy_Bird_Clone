import pygame
import sys, random  


def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,650))
    screen.blit(floor_surface,(floor_x_pos+576,650))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos-850))

    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 500:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    
    if bird_rect.top <= -200 or bird_rect.bottom >= 650:
        return False
    
    return True


clock = pygame.time.Clock()
#PyGame Variables
pygame.init()
screen = pygame.display.set_mode((576,800))
runGame = True
game_active = True

#background image
bg_surface = pygame.image.load('assets/background-day.png').convert()

#Scale surface 2 times
bg_surface = pygame.transform.scale2x(bg_surface)

#Floor surface
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

#bird asset
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
#Put rect on bird asset
bird_rect = bird_surface.get_rect(center = (100,312))

#Pipe asset
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
#pygame timer
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [200,250,300,350,400,450,500,550]



#Physics vars
gravity = 0.5
bird_movement = 0

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center=(100,312)
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
    
    screen.blit(bg_surface,(0,-200))
    
    if game_active:
        #Blit is the method to display imagages on screen
        

        bird_movement += gravity
        bird_rect.centery += bird_movement

        screen.blit(bird_surface,bird_rect)

        game_active = check_collision(pipe_list)
        
        #Move the pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

    #Floor
    floor_x_pos-=2
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    #Cap fram rate at 120hz
    clock.tick(120)