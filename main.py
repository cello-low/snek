import pygame
import random

window = pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Write your caption here!")

#floor
floor = pygame.surface.Surface((800,100))
floor.fill((0,0,0))

game_state = 1
#1 = active
#2 = end/game over

#making player
player = pygame.surface.Surface((100,100))
player = pygame.image.load("imgs/Player_icon (2).png").convert_alpha()
player = pygame.transform.scale(player, (100,100))
player_x = 0
player_y = 400
player_vel_x = 0
player_vel_y = 0

#making npc
falling_object = pygame.surface.Surface((40,40))
falling_object = pygame.image.load("imgs/Apple_icon.png").convert_alpha()
falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0.2

#making falling special apple
fall_special = pygame.surface.Surface((40,40))
fall_special = pygame.image.load("imgs/Golden_apple_icon.png").convert_alpha()
fall_special_x = 1000
fall_special_y = 1000
fall_special_vel_x = 0
fall_special_vel_y = 0

special_is_falling = False

#making game over screen
game_over = pygame.surface.Surface((400,400))
game_over = pygame.image.load("imgs/Sad_player_icon.png").convert_alpha()
game_over = pygame.transform.scale(game_over, (300,300))

#making score display
score = 0
pygame.font.init()
font = pygame.font.Font(None, 36)
score_text = font.render(f"Score: {score}", True, (0,0,0))

#making "you lose" text
you_lose_text = font.render("You Lose! Press r to restart.", True, (0,0,0))

def collision_detection():
     return ((player_x <= (falling_object_x + int(falling_object.width))) and
            (player_x + player.width) >= falling_object_x and 
            player_y <= (falling_object_y + falling_object.height + 5) and 
            (player_y + player.height) >= falling_object_y)
def collision_detection_special():
    return ((player_x <= (fall_special_x + int(fall_special.width))) and
            (player_x + player.width) >= fall_special_x and 
            player_y <= (fall_special_y + fall_special.height + 5) and 
            (player_y + player.height) >= fall_special_y)

def make_special():
    random_number = random.randint(0, 300)
    if random_number == 1:
        return True

while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.4
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.4
            if event.key == pygame.K_r:
                game_state = 1
                # Reset game objects
                score = 0
                player_x = 0
                player_y = 400
                falling_object_x = random.randint(0, window.width - 50)
                falling_object_y = 0
                falling_object_vel_y = 0.2
                score_text = font.render(f"Score: {score}", True, (0,0,0))
        else:
            player_vel_x = 0
            player_vel_y = 0
    #falling object gone detector/ fail state
    if falling_object_y >= 600:
        player_x, player_y = 1000,1000
        player_vel_x, player_vel_y = 0,0

        falling_object_x, falling_object_y = 1000,1000
        falling_object_vel_x, falling_object_vel_y = 0,0

        game_state = 2
    #falling obeject collision detector
    elif collision_detection():
        score += 1
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        falling_object_y = 0
        falling_object_x = random.randint(0, window.width - 50)

    #if it goes out of bounds, reset it
    if make_special() and not special_is_falling:
        special_is_falling = True
        fall_special_x = random.randint(0, window.width - 50)
        fall_special_y = 0
        fall_special_vel_x = 0
        fall_special_vel_y = 0.1
        window.blit(fall_special, (fall_special_x, fall_special_y))
    if fall_special_y >= 600:
        special_is_falling = False
        fall_special_x, fall_special_y = 1000,1000
        fall_special_vel_x, fall_special_vel_y = 0,0
    #if you touch it, get 5 points
    elif collision_detection_special():
        score += 5
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        fall_special_x, fall_special_y = 1000,1000
        fall_special_vel_x, fall_special_vel_y = 0,0
    
    #drawing everyting
    #draws window
    if game_state == 1: #if game is on, render the people and stuff
        window.fill((255,255,255))    
        window.blit(floor, (0,500))
        #draws player
        player_x += player_vel_x
        player_y += player_vel_y
        window.blit(player,(player_x, player_y))
    
        #draws falling object
        falling_object_x += falling_object_vel_x
        falling_object_y += falling_object_vel_y
        window.blit(falling_object, (falling_object_x, falling_object_y))

        #randomizer for falling object
        fall_special_x += fall_special_vel_x
        fall_special_y += fall_special_vel_y
        window.blit(fall_special, (fall_special_x, fall_special_y))
            
        #draws score
        window.blit(score_text, (10, 10))

    elif game_state == 2:
        window.fill((255,255,255))
        window.blit(game_over, (200,100))
        window.blit(you_lose_text, (200, 400))
        window.blit(score_text, (10, 10))
    
    pygame.display.flip()