# Разработай свою игру в этом файле!

from pygame import *
import classes as cl
import os
from pathlib import Path

# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути

move_right = False
move_left = False
move_up = False
move_down = False
look_bul = 'right'
finish = False
lose = False
bullets = []
speed_number = 1
run = True
walls = []
x_wall = 150
BLUE = ((0,0,255))
WIN_HIGHT = 700
WIN_WIGHT = 500
picture = transform.scale(image.load(DIR/'img/Bg.jpeg'),(WIN_HIGHT,WIN_WIGHT))
player = cl.Player(400,400,100,100,DIR/'img/Happy_Alien.png',3,2)
enemy = cl.Enemy(200,50,50,50,DIR/'img/enemy.png',2,2)
final = cl.Sprite(400,50,100,100,DIR/'img/ball.png')
win_screen = cl.Sprite(0,0,700,500,DIR/'img/win.png')
lose_screen = cl.Sprite(0,0,700,500,DIR/'img/lose.png')
for i in range(4):
    wall = cl.Sprite(x_wall,250,125,75,DIR/'img/Wall.png')
    walls.append(wall)
    x_wall += 150

window = display.set_mode((WIN_HIGHT,WIN_WIGHT))
display.set_caption('Лабиринт')

while run:
    time.delay(50)
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            if look_bul == 'right':
                player.shot(20,10,DIR/'img/Bullet_Hor.png',look_bul,bullets)
            elif look_bul == 'up':
                player.shot(10,20,DIR/'img/Bullet.png',look_bul,bullets)
            elif look_bul == 'down':
                player.shot(10,20,DIR/'img/Bullet.png',look_bul,bullets)
            elif look_bul == 'left':
                player.shot(20,10,DIR/'img/Bullet_Hor.png',look_bul,bullets)
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_a:
                move_left = True
                look_bul = 'left'
            if e.key == K_d:
                move_right = True
                look_bul = 'right'
            if e.key == K_w:
                move_up = True
                look_bul = 'up'
            if e.key == K_s:
                move_down = True
                look_bul = 'down'
        if e.type == KEYUP:
            if e.key == K_a:
                move_left = False
            if e.key == K_d:
                move_right = False 
            if e.key == K_w:
                move_up = False
            if e.key == K_s:
                move_down = False

    window.blit(picture,(0,0))
    if finish == False:
        player.draw_picture(window)
        enemy.draw_picture(window)
        final.draw_picture(window)
        enemy.update()
        for i in walls:
            i.draw_picture(window)
        
        for bulle in bullets:
            bulle.draw_picture(window)
            bulle.update()
            bulle.kill(enemy,bullets)
    else:
        if lose:
            lose_screen.draw_picture(window)
        else:
            win_screen.draw_picture(window)
        
    for i in walls:
        for b in bullets:
            if b.collide(i):
                bullets.remove(b)

    if move_right:
        speed_number = 1
        player.update(speed_number,'horizontal')
    if move_down:
        speed_number = 1
        player.update(speed_number,'up')
    if move_left:
        speed_number = -1
        player.update(speed_number,'horizontal')
    if move_up:
        speed_number = -1
        player.update(speed_number,'up')

    if player.collide(enemy):
        finish = True
        lose = True

    if player.collide(final):
        finish = True

    if player.rect.y > 400:
        player.rect.y -= 2
    if player.rect.y < 0:
        player.rect.y += 2
    if move_right and player.rect.x > 600:
        player.rect.x -= 3
    if player.rect.x < 0:
        player.rect.x += 3
    
    for wall in walls:
        if player.collide(wall):
            if move_right:
                player.rect.x -= 4
            if move_down:
                player.rect.y -= 3
            if move_left:
                player.rect.x +=3
            if move_up:
                player.rect.y += 4
            move_right = False
            move_down = False
            move_left = False
            move_up = False
    
    display.update()