import pygame
from ball import *
from sys import exit


pygame.init()
clock = pygame.time.Clock()
WINDOW_SIZE = (800, 500)
window = pygame.display.set_mode(WINDOW_SIZE)
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# background
background = pygame.image.load("graphics/background/moon.png").convert()
background = pygame.transform.scale(background, (WINDOW_SIZE))
background_rect = background.get_rect( topleft = (0,0))

#backgrounds
front_mountain = pygame.image.load("graphics/background/mountain.png").convert_alpha()
front_mountain = pygame.transform.rotozoom(front_mountain, 0, 2)
front_mountain_rect = front_mountain.get_rect(midtop = (300, 110))

back_mountain = pygame.image.load("graphics/background/mountains.png").convert_alpha()
back_mountain = pygame.transform.rotozoom(back_mountain, 0, 2)
back_mountain_rect = back_mountain.get_rect(bottomleft = (0, 450))

mountain_tree = pygame.image.load("graphics/background/mountain_tree.png").convert_alpha()
mountain_tree = pygame.transform.rotozoom(mountain_tree, 0 , 3)
mountain_tree_rect = mountain_tree.get_rect(bottomleft = (0, 500))

tree = pygame.image.load("graphics/background/tree.png").convert_alpha()
tree = pygame.transform.rotozoom(tree, 0, 2)
tree_rect = tree.get_rect(bottomleft = (0,500))

game_on = False

while True:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
                game_on = True


    # draw backgrounds
    window.blit(background, background_rect)
    window.blit(front_mountain, front_mountain_rect)
    window.blit(back_mountain, back_mountain_rect)
    window.blit(mountain_tree, mountain_tree_rect)
    window.blit(tree, tree_rect)
    if game_on:
        # draw and update the bricks
        brick_amount = 0
        for brick_group in brick_groups:
            brick_amount+= len(brick_group)
            brick_group.draw(window)
            brick_group.update()
        if brick_amount <= 0:
            game_on = False
            message = font.render("you win", False, "#4E3636")
            message_rect = message.get_rect(center = (WINDOW_SIZE[0]/2, 110))
            window.blit(message, message_rect)
            ball_group.sprite.rect = ball_group.sprite.image.get_rect(center = (WINDOW_SIZE[0]/2, 450))
        if ball_group.sprite.rect.bottom >= 490:
            game_on = False

        # draw and update the ball
        ball_group.draw(window)
        ball_group.update()
        plate_group.draw(window)
        plate_group.update()
    else:
        text = font.render(f"press space to start", False, "#4E3636")
        text_rect = text.get_rect(center = (WINDOW_SIZE[0]/2, 150))
        window.blit(text, text_rect)
    pygame.display.update()
    clock.tick(60)



"""
The `get_rect()` method in Pygame returns a `pygame.Rect` object that represents the rectangular area of the surface 
it's called on. The `pygame.Rect` object has various attributes including `center`, `midbottom`, `midleft`, `midright`,
 `midtop`, `bottomleft`, `bottomright`, `topleft`, `topright`, `width`, and `height`.
"""