import pygame
import random

window = pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Write your caption here!")

game_state = 1
#1 = active
#2 = end/game over

#making player
player = pygame.surface.Surface((100,100))
player = pygame.image.load("imgs/player_icon.png").convert_alpha()
player = pygame.transform.scale(player, (300,300))
player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

#making npc
falling_object = pygame.surface.Surface((50,50))
falling_object.fill((0,0,0))
falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0.3

#making game over screen
game_over = pygame.surface.Surface((400,400))
game_over = pygame.image.load("imgs/sad_player_icon.png").convert_alpha()
game_over = pygame.transform.scale(game_over, (300,300))

def collision_detection():
     return ((player_x <= (falling_object_x + int(falling_object.width))) and
            (player_x + player.width) >= falling_object_x and 
            player_y <= (falling_object_y + falling_object.height + 5) and 
            (player_y + player.height) >= falling_object_y)

while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.2
        else:
            player_vel_x = 0
            player_vel_y = 0
    #falling obeject randomizer
    if collision_detection():
        falling_object_y = 0
        falling_object_x = random.randint(0, window.width - 50)
    #falling object gone detector/ fail state
    if falling_object_y >= 600:
        player_x, player_y = 1000,1000
        player_vel_x, player_vel_y = 0,0

        falling_object_x, falling_object_y = 1000,1000
        falling_object_vel_x, falling_object_vel_y = 0,0

        game_state = 2
    #drawing everyting
    #draws window
    if game_state == 1: #if game is on, render the people and stuff
        window.fill((255,255,255))    
        #draws player
        player_x += player_vel_x
        player_y += player_vel_y
        window.blit(player,(player_x, player_y))
    
        #draws falling object
        falling_object_x += falling_object_vel_x
        falling_object_y += falling_object_vel_y
        window.blit(falling_object, (falling_object_x, falling_object_y))

    elif game_state == 2:
        window.fill((255,255,255))
        window.blit(game_over, (200,100))
    
    pygame.display.flip()