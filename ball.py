import pygame
from random import choice
WINDOW_SIZE = (800, 500)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/ball/ball.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.15)
        self.rect = self.image.get_rect(center = (WINDOW_SIZE[0]/2, 450))
        self.moveX = -1
        self.moveY = -1
        self.collision_with_plate = False
    def move_x(self):
        self.rect.x *= -1
    def move_y(self):
        self.rect.y *= -1
    def move(self):
        self.rect.y += self.moveY
        self.rect.x += self.moveX

    def cheak_move(self):
        for brick_group in brick_groups:
            if pygame.sprite.spritecollide(self, brick_group, True):
                self.moveY *= -1
                self.moveX *= -1
            else:
                self.move()
        # collision between the ball and the plate
        if pygame.sprite.spritecollide(self, plate_group, False):
            if self.rect.y >=420 and self.collision_with_plate == False:
                self.collision_with_plate = True
                self.moveY *= -1
        else:
            self.collision_with_plate = False


        # collision between ball and the window
        if self.rect.top <= 0:
            self.moveY *= -1
        if self.rect.left <=0 or self.rect.right >= WINDOW_SIZE[0]:
            self.moveX *= -1


    def update(self):
        self.cheak_move()



# Plate class
class Plate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/plate/plate.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center=(WINDOW_SIZE[0] / 2, 470))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 7
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 7

    def update(self):
        self.move()

class Bricks(pygame.sprite.Sprite):
    def __init__(self, x , y, brick):
        super().__init__()
        self.image = pygame.image.load(brick)
        self.image = pygame.transform.rotozoom(self.image, 0 , 0.17)
        self.rect = self.image.get_rect(topleft = (x,y))


# plate group and object
plate_group = pygame.sprite.GroupSingle()
plate_group.add(Plate())


# array of bricks, brick group and brick object
bricks = [f"graphics/bricks/breakout_brick{i}.png" for i in range(1,11)]

brick_groups = [pygame.sprite.Group() for i in range(5)]
amount_of_bricks = 12
margin = 10
for j in range(5):
    for i in range(amount_of_bricks):
        new_brick = Bricks(65 * i + margin, j * 22, choice(bricks))
        brick_groups[j].add(new_brick)
    amount_of_bricks -= 2
    margin += 65


# ball groups and object
ball_group = pygame.sprite.GroupSingle()
ball_group.add(Ball())
