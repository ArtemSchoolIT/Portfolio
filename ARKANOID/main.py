import pygame as pg
import sys
import os
from pathlib import Path

# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути

pg.init()
window = pg.display.set_mode((500,500))
window.fill((128, 128, 255))
clock = pg.time.Clock()
amount_monster = 24
monsters = []
x = 25
run = True
move_right = False
move_left = False
speed_y = 3
speed_x = 3
collide_x = 0
lvl0 = True
lvl1 = False
lvl2 = False
lvl3 = False
lvl3_break = False
outline = (0, 207, 108)
color_c = (128, 128, 255)
alliens = []
bullet_speed = 3
bullets = []
rockets = []
drons = []
speed_boss = 2
coldown = 0
coldown_r = 0
r_work = 0
reverse = False
win = False
lose = False
summon = 0

class Area():
    def __init__(self,x,y,weight,height,color):
        self.rect = pg.Rect(x,y,weight,height)
        self.color = color

    def draw(self):
        pg.draw.rect(window,self.color,self.rect)

    def outline(self,color_outline,wight_outline):
        pg.draw.rect(window,color_outline,self.rect,wight_outline)

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

    def collide(self,rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self,x,y,weight,height,color,image,hp,no_attack):
        super().__init__(x,y,weight,height,color)
        self.imge = pg.image.load(image)
        self.hp = hp
        self.no_attack = no_attack  

    def set_picture(self,image):
        self.imge = pg.image.load(image)

    def draw_picture(self):
        window.blit(self.imge,(self.rect.x,self.rect.y)) 

    def shot(self,hp,list_name):
        bullet = Picture(self.rect.x+65,self.rect.y,10,20,color_c,'Bullet.png',hp,0)
        list_name.append(bullet)   

    def launch(self,hp,list_name): 
        rocket = Picture(self.rect.x+65,self.rect.y + self.rect.y,50,60,color_c,'Blue_Rocket.png',hp,0)
        list_name.append(rocket)   


class Label(Area):
    def set_text(self,text,ime):
        self.text = text
        self.ime = pg.font.Font(None,40).render(self.text,True,(0,0,0))

    def fill(self):
        self.draw()

    def fill_text(self,shift_x,shift_y):
        self.draw()
        window.blit(self.ime,(self.rect.x+shift_x,self.rect.y+shift_y))

class End_Screen(Area):
    def set_end_text(self,text,image):
        self.text = text
        self.image = pg.font.Font(None,50).render(self.text,True,(0,0,0))

ball = Picture(75,300,50,50,color_c,DIR/'img/ball.png',1,0)

plat = Picture(100,360,100,23,color_c,DIR/'img/platform.png',1,0)

plat_weap = Picture(100,450,130,20,color_c,DIR/'img/Plat_Weapon_C.png',3,0)
plat_weap.imge = pg.transform.scale(plat_weap.imge,(600,600))

play_button = Picture(200,250,80,40,color_c,DIR/'img/Play_b.png',1,0)
play_button.imge = pg.transform.scale(play_button.imge,(700,700))

exit_button = Picture(200,350,80,40,color_c,DIR/'img/Exit_b.png',1,0)
exit_button.imge = pg.transform.scale(exit_button.imge,(700,700))

headline = Picture(150,50,200,100,color_c,DIR/'img/Title.png',1,0)
headline.imge = pg.transform.scale(headline.imge,(900,900))

lose_text = Label(200,300,100,50,color_c)
lose_text.set_text('You Lose',100)

win_text = Label(200,300,100,50,color_c)
win_text.set_text('You Win',100)

menu_button = Picture(50,300,75,50,color_c,DIR/'img/Menu_b.png',1,0)
menu_button.imge = pg.transform.scale(menu_button.imge,(700,700))

restart = Picture(350,300,75,50,color_c,DIR/'img/Restart_b.png',1,0)
restart.imge = pg.transform.scale(restart.imge,(700,700))

continue_button = Picture(350,300,75,50,color_c,DIR/'img/Continue_b.png',1,0)
continue_button.imge = pg.transform.scale(continue_button.imge,(700,700))

new_screen = Label(0,0,500,600,color_c)

while run:
    while lvl0 == True:
        new_screen.fill()
        play_button.draw_picture()
        exit_button.draw_picture()
        headline.draw_picture()
        pg.display.update()
        clock.tick(40)

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x_event,y_event= event.pos
                if play_button.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl1 = True
                    lvl0 = False
                    monsters = []
                    x = 25
                    speed_y = 3
                    speed_x = 3
                    ball.rect.x = 75
                    ball.rect.y = 300
                    plat.rect.x =100
                    for mon in range(9):
                        monster = Picture(x,50,50,45,color_c,'img/enemy.png',1,0)
                        monster.draw_picture()
                        monsters.append(monster)
                        x += 50

                    x = 50
                    for mons in range(8):
                        monster = Picture(x,100,50,45,color_c,'enemy.png',1,0)
                        monster.draw_picture()
                        monsters.append(monster)
                        x += 50

                    x= 75
                    for monst in range(7):
                        monster = Picture(x,150,50,45,color_c,'enemy.png',1,0)
                        monster.draw_picture()
                        monsters.append(monster)
                        x += 50

                if exit_button.collidepoint(x_event,y_event):
                    sys.exit()
            if event.type == pg.QUIT:
                run = False 
                lvl0 = False 
                                              
        pg.display.update()
        clock.tick(40)

    while lvl1 == True:
        new_screen.fill()

        for monste in range(len(monsters)):
            monsters[monste].draw_picture()
                
        if move_right == True or plat.rect.x < 0:
            plat.rect.x +=3
        if move_left == True or plat.rect.x > 400:
            plat.rect.x -= 3
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        for monster_2 in monsters:
            if ball.collide(monster_2.rect):
                if ball.rect.x > monster_2.rect.x:
                    collide_x = ball.rect.x - monster_2.rect.x
                    if collide_x < 50:
                        speed_y *= -1
                    else:
                        speed_x *= -1
                elif ball.rect.x < monster_2.rect.x:
                    collide_x = monster_2.rect.x - ball.rect.x 
                    if collide_x < 50:
                        speed_y *= -1
                    else:
                        speed_x *= -1
                monsters.remove(monster_2) 


        if ball.collide(plat.rect) or ball.rect.y < -5:
            speed_y *= - 1
        elif ball.rect.x < 0 or ball.rect.x > 450:
            speed_x *= -1
        elif ball.rect.y > 450:
            speed_x = 0
            speed_y= 0
            continue_button.rect.x = 600
            restart.rect.x = 350
            menu_button.rect.x = 50
            lose_text.fill_text(0,0)
            menu_button.draw_picture()
            restart.draw_picture()
        if len(monsters) <= 23:
            speed_x = 0
            speed_y= 0
            restart.rect.x = 600
            continue_button.rect.x = 350
            menu_button.rect.x = 50
            win_text.fill_text(5,10)
            menu_button.draw_picture()
            continue_button.draw_picture()


        ball.draw_picture()
        plat.draw_picture()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x_event,y_event= event.pos
                if menu_button.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl0 = True
                    lvl1 = False
                    new_screen.fill()
                if restart.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    monsters = []
                    x = 25
                    speed_y = 3
                    speed_x = 3
                    ball.rect.x = 75
                    ball.rect.y = 300
                    plat.rect.x =100
                    for mon in range(9):
                        monster = Picture(x,50,50,45,color_c,'enemy.png',1,0)
                        monster.draw_picture()
                        monsters.append(monster)
                        x += 50

                    x = 50
                    for mons in range(8):
                        monster = Picture(x,100,50,45,color_c,'enemy.png',1,0)
                        monster.draw_picture()
                        monsters.append(monster)
                        x += 50

                    x= 75
                    for monst in range(7):
                        monster = Picture(x,150,50,45,color_c,'enemy.png',1,0)
                        monster.draw_picture()
                        monsters.append(monster)
                        x += 50
                    new_screen.fill()
                if continue_button.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl2 = True
                    lvl1 = False
                    alliens = []
                    speed_y = 3
                    speed_x = 3
                    ball.rect.x = 75
                    ball.rect.y = 300
                    plat_weap.rect.x = 100
                    plat_weap.rect.y = 400
                    plat.rect.x = 600
                    y = 0

                    for i in range(3):
                        allien = Picture(50,y,100,100,color_c,'Happy_Alien.png',2,0)
                        allien.imge = pg.transform.scale(allien.imge,(500,500))
                        allien.draw_picture()
                        alliens.append(allien)
                        y += 100

                    y = 0
                    for i in range(3):
                        allien = Picture(200,y,100,100,color_c,'Happy_Alien.png',2,0)
                        allien.imge = pg.transform.scale(allien.imge,(500,500))
                        allien.draw_picture()
                        alliens.append(allien)
                        y += 100
                    
                    y = 0 
                    for i in range(3):
                        allien = Picture(350,y,100,100,color_c,'Happy_Alien.png',2,0)
                        allien.imge = pg.transform.scale(allien.imge,(500,500))
                        allien.draw_picture()
                        alliens.append(allien)
                        y += 100
                    new_screen.fill()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    move_left = True
                elif event.key == pg.K_d:
                    move_right = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    move_left = False
                elif event.key == pg.K_d:
                    move_right = False
        pg.display.update()
        clock.tick(40)


    while lvl2 == True:
        new_screen.fill()

        for al in range(len(alliens)):
            alliens[al].draw_picture()

        if move_right == True or plat_weap.rect.x < 0:
            plat_weap.rect.x +=3
        if move_left == True or plat_weap.rect.x > 370:
            plat_weap.rect.x -= 3
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        

        if ball.collide(plat_weap.rect) or ball.rect.y < -5:
            speed_y *= - 1
        elif ball.rect.x < 0 or ball.rect.x > 450:
            speed_x *= -1
        elif ball.rect.y > 450:
            speed_x = 0
            speed_y= 0
            continue_button.rect.x = 600
            restart.rect.x = 350
            menu_button.rect.x = 50
            lose_text.fill_text(0,0)
            menu_button.draw_picture()
            restart.draw_picture()
        for allien_2 in alliens:
            if ball.collide(allien_2.rect):
                if ball.rect.x > allien_2.rect.x:
                    collide_x = ball.rect.x - allien_2.rect.x
                    if collide_x < 50:
                        speed_y *= -1
                    else:
                        speed_x *= -1
                elif ball.rect.x < allien_2.rect.x:
                    collide_x = allien_2.rect.x - ball.rect.x 
                    if collide_x < 50:
                        speed_y *= -1
                    else:
                        speed_x *= -1
                allien_2.draw()
                if allien_2.hp == 2:
                    allien_2.hp -= 1
                    allien_2.set_picture('Sad_Alien.png')
                    allien.imge = pg.transform.scale(allien_2.imge,(500,500))
                else:
                    alliens.remove(allien_2) 

        if len(alliens) <= 8:
            speed_x = 0
            speed_y= 0
            restart.rect.x = 600
            continue_button.rect.x = 350
            menu_button.rect.x = 50
            win_text.fill_text(5,10)
            menu_button.draw_picture()
            continue_button.draw_picture()


        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x_event,y_event= event.pos
                if menu_button.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl0 = True
                    lvl2 = False
                    new_screen.fill()
                if restart.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl2 = True
                    lvl1 = False
                    alliens = []
                    speed_y = 3
                    speed_x = 3
                    ball.rect.x = 75
                    ball.rect.y = 300
                    plat_weap.rect.x = 100
                    plat_weap.rect.y = 400
                    plat.rect.x = 600
                    y = 0

                    for i in range(3):
                        allien = Picture(50,y,100,100,color_c,'Happy_Alien.png',2,0)
                        allien.imge = pg.transform.scale(allien.imge,(500,500))
                        allien.draw_picture()
                        alliens.append(allien)
                        y += 100

                    y = 0
                    for i in range(3):
                        allien = Picture(200,y,100,100,color_c,'Happy_Alien.png',2,0)
                        allien.imge = pg.transform.scale(allien.imge,(500,500))
                        allien.draw_picture()
                        alliens.append(allien)
                        y += 100
                    
                    y = 0 
                    for i in range(3):
                        allien = Picture(350,y,100,100,color_c,'Happy_Alien.png',2,0)
                        allien.imge = pg.transform.scale(allien.imge,(500,500))
                        allien.draw_picture()
                        alliens.append(allien)
                        y += 100
                    new_screen.fill()
                if continue_button.collidepoint(x_event,y_event):
                    reload_plat = 0
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl3 = True
                    lvl2 = False
                    des_walls = []
                    walls  = []
                    speed_y = 2
                    speed_x = 2
                    ball.rect.x = 75
                    ball.rect.y = 300
                    plat_weap.rect.x = 100
                    plat_weap.rect.y = 400
                    plat.rect.x = 600
                    coldown = 0 
                    bullets = []
                    rockets = []
                    drons = []
                    x = 0

                    for i in range(3):
                        wall = Picture(x,200,150,80,color_c,'Wall.png',4,0)
                        wall.imge = pg.transform.scale(wall.imge,(700,500))
                        wall.draw_picture()
                        walls.append(wall)
                        x += 175

                    boss = Picture(100,0,150,150,color_c,'3hp_Boss.png',3,0)
                    boss.imge = pg.transform.scale(boss.imge,(700,700))
                    boss.draw_picture()
                    new_screen.fill()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    move_left = True
                elif event.key == pg.K_d:
                    move_right = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    move_left = False
                elif event.key == pg.K_d:
                    move_right = False

        ball.draw_picture()
        plat_weap.draw_picture()

        pg.display.update()
        clock.tick(40)
    while lvl3 == True:
        new_screen.fill()

        for wal in range(len(walls)):
            walls[wal].draw_picture()

        for dwal in range(len(des_walls)):
            des_walls[dwal].draw_picture()


        if len(bullets) != 0:
            for bullet2 in range(len(bullets)):
                bullets[bullet2].rect.y -= bullet_speed
                bullets[bullet2].draw_picture()


        if move_right == True or plat_weap.rect.x < 0:
            plat_weap.rect.x +=3
        if move_left == True or plat_weap.rect.x > 370:
            plat_weap.rect.x -= 3
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        boss.rect.x += speed_boss
        if len(rockets) != 0:
            for ro in range(len(rockets)):
                rockets[ro].draw_picture()
                rockets[ro].rect.y += 2


        if boss.rect.x == 0:
            speed_boss *= -1
        if boss.rect.x == 350:
            speed_boss *= -1

        for rocke in rockets:
            if rocke.collide(plat_weap.rect):
                if plat_weap.hp > 1:
                    plat_weap.hp -= 1
                else:
                    lose = True
                rockets.remove(rocke)

        
        if ball.collide(plat_weap.rect) or ball.rect.y < -5:
            speed_y *= - 1
        elif ball.rect.x < 0 or ball.rect.x > 450:
            speed_x *= -1
        elif ball.collide(boss.rect):
            if boss.hp != 1:
                if boss.hp == 3:
                    boss.set_picture('2hp_Boss_block.png')
                    boss.imge = pg.transform.scale(boss.imge,(700,700))
                elif boss.hp == 2:
                    boss.set_picture('1hp_Boss_block.png')
                    boss.imge = pg.transform.scale(boss.imge,(700,700))
                boss.hp -= 1
                restart.rect.x = 600
                continue_button.rect.x = 600
                menu_button.rect.x = 600
                lvl3 = False
                lvl3_break = True
                des_walls = []
                walls  = []
                speed_y = 2
                speed_x = 2
                ball.rect.x = 600
                ball.rect.y = 600
                plat_weap.rect.x = 100
                plat_weap.rect.y = 400
                plat.rect.x = 600
                boss.rect.x = 150
                boss.rect.y = 0
                coldown = 0
                coldown_r = 0 
                r_work = 0
                bullets = []
                rockets = []
                drons = []
                x = 50

                for i in range(2):
                    dron = Picture(x,50,70,50,color_c,'Dron.png',10,0)
                    dron.draw_picture()
                    drons.append(dron)
                    x += 350

            else:
                win = True

        if win:
            speed_x = 0
            speed_y= 0
            restart.rect.x = 600
            menu_button.rect.x = 50
            win_text.fill_text(5,10)
            menu_button.draw_picture()

        elif ball.rect.y > 450 or lose:
            speed_x = 0
            speed_y= 0
            menu_button.rect.x = 50
            restart.rect.x = 350
            continue_button.rect.x = 600
            lose_text.fill_text(0,0)
            menu_button.draw_picture()
            restart.draw_picture()
        for wall2 in walls:
            if ball.collide(wall2.rect):
                speed_y *= -1
                if wall2.hp != 1:
                    wall2.hp -= 1
                else:
                    des_walls.append(wall2)
                    wall2.set_picture('Wal_Dl.png')
                    wall2.rect.y -= 25
                    wall2.imge = pg.transform.scale(wall2.imge,(700,500))
                    walls.remove(wall2) 

        for dwall2 in des_walls:
            if ball.collide(dwall2.rect):
                speed_y *= -1


        for r in rockets:
            for bu in bullets:
                if bu.collide(r.rect):
                    if r.hp != 1:
                        r.hp -= 1
                    else:
                        rockets.remove(r)
                    bullets.remove(bu)

        ball.draw_picture()
        plat_weap.draw_picture()
        boss.draw_picture()

        if len(walls) == 0:
            for dewall in des_walls:
                des_walls.remove(dewall)


        coldown += 1
        if coldown == 120:
            boss.launch(2,rockets)
            coldown = 0

        coldown_r += 1
        if coldown_r == 600:
            r_work = 80
            coldown = 121
            reverse = True
            if boss.hp == 3:
                boss.set_picture('3hp_Boss_Red.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))
            elif boss.hp == 2:
                boss.set_picture('2hp_Boss_Red.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))
            elif boss.hp == 1:
                boss.set_picture('1hp_Boss_Red.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))
        r_work -= 1
        if r_work == 0: 
            coldown_r = 0
            coldown = 0
            reverse = False
            move_left = False
            move_right = False
            if boss.hp == 3:
                boss.set_picture('3hp_Boss.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))
            elif boss.hp == 2:
                boss.set_picture('2hp_Boss.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))
            elif boss.hp == 1:
                boss.set_picture('1hp_Boss.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))      

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x_event,y_event= event.pos
                if menu_button.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl0 = True
                    lvl3 = False
                    win = False
                    new_screen.fill()
                if restart.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl3 = True
                    lvl2 = False
                    des_walls = []
                    walls  = []
                    speed_y = 2
                    speed_x = 2
                    ball.rect.x = 75
                    ball.rect.y = 300
                    plat_weap.rect.x = 100
                    plat_weap.rect.y = 400
                    plat_weap.hp = 5
                    plat.rect.x = 600
                    coldown = 0
                    coldown_r = 0
                    r_work = 0  
                    bullets = []
                    rockets = []
                    drons = []
                    x = 0

                    for i in range(3):
                        wall = Picture(x,200,150,80,color_c,'Wall.png',4,0)
                        wall.imge = pg.transform.scale(wall.imge,(700,500))
                        wall.draw_picture()
                        walls.append(wall)
                        x += 175

                    boss = Picture(100,0,150,150,color_c,'3hp_Boss.png',3,0)
                    boss.imge = pg.transform.scale(boss.imge,(700,700))
                    boss.draw_picture()
            if event.type == pg.KEYDOWN:
                if reverse:
                    if event.key == pg.K_a:
                        move_right = True
                    elif event.key == pg.K_d:
                        move_left = True
                    elif event.key == pg.K_SPACE:
                        plat_weap.shot(1,bullets)
                else:
                    if event.key == pg.K_a:
                        move_left = True
                    elif event.key == pg.K_d:
                        move_right = True
                    elif event.key == pg.K_SPACE:
                        plat_weap.shot(1,bullets)
            if event.type == pg.KEYUP:
                if reverse:
                    if event.key == pg.K_a:
                        move_right = False
                    elif event.key == pg.K_d:
                        move_left = False
                else:
                    if event.key == pg.K_a:
                        move_left = False
                    elif event.key == pg.K_d:
                        move_right = False

            

        pg.display.update()
        clock.tick(40)
    
    while lvl3_break:
        new_screen.fill()

        if len(bullets) != 0:
            for bullet2 in range(len(bullets)):
                bullets[bullet2].rect.y -= bullet_speed
                bullets[bullet2].draw_picture()


        if move_right == True or plat_weap.rect.x < 0:
            plat_weap.rect.x +=3
        if move_left == True or plat_weap.rect.x > 370:
            plat_weap.rect.x -= 3


        for rocke2 in rockets:
            if rocke.collide(plat_weap.rect):
                if plat_weap.hp > 1:
                    plat_weap.hp -= 1
                else:
                    lose = True
                rockets.remove(rocke)
        
        if len(rockets) != 0:
            for ro in range(len(rockets)):
                rockets[ro].draw_picture()
                rockets[ro].rect.y += 2
                rockets[ro].no_attack -= 1

        for d in range(len(drons)):
            drons[d].draw_picture()

        for rocket2 in rockets:
            for bu in bullets:
                if bu.collide(rocket2.rect) and rocket2.no_attack <= 0:
                    if rocket2.hp != 1:
                        rocket2.hp -= 1
                    else:
                        rockets.remove(rocket2)
                    bullets.remove(bu)

        if lose:
            menu_button.rect.x = 50
            restart.rect.x = 350
            continue_button.rect.x = 600
            lose_text.fill_text(0,0)
            menu_button.draw_picture()
            restart.draw_picture()


        plat_weap.draw_picture()
        boss.draw_picture()

        summon += 1
        if summon == 140:
            x = 40 
            for i in range(6):
                rocket = Picture(x,0,50,60,color_c,'Blue_Rocket.png',2,20)
                rockets.append(rocket)
                x += 75
            summon = 0


        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x_event,y_event= event.pos
                if restart.collidepoint(x_event,y_event):
                    restart.rect.x = 600
                    continue_button.rect.x = 600
                    menu_button.rect.x = 600
                    lvl3 = True
                    lvl2 = False
                    des_walls = []
                    walls  = []
                    speed_y = 2
                    speed_x = 2
                    ball.rect.x = 75
                    ball.rect.y = 300
                    plat_weap.rect.x = 100
                    plat_weap.rect.y = 400
                    plat_weap.hp = 5
                    plat.rect.x = 600
                    coldown = 0
                    coldown_r = 0
                    r_work = 0 
                    bullets = []
                    rockets = []
                    drons = []
                    x = 0

                    for i in range(3):
                        wall = Picture(x,200,150,80,color_c,'Wall.png',4)
                        wall.imge = pg.transform.scale(wall.imge,(700,500))
                        wall.draw_picture()
                        walls.append(wall)
                        x += 175

                    boss = Picture(100,0,150,150,color_c,'3hp_Boss.png',3)
                    boss.imge = pg.transform.scale(boss.imge,(700,700))
                    boss.draw_picture()
                    new_screen.fill()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    move_left = True
                elif event.key == pg.K_d:
                    move_right = True
                elif event.key == pg.K_SPACE:
                    plat_weap.shot(1,bullets)
            if event.type == pg.KEYUP:
                if event.key == pg.K_a:
                    move_left = False
                elif event.key == pg.K_d:
                    move_right = False


        for dron2 in drons:
            for bul in bullets:
                if bul.collide(dron2.rect):
                    if dron2.hp != 1:
                        dron2.hp -= 1
                    else:
                        drons.remove(dron2)
                    bullets.remove(bul)

        if len(drons) == 0:
            restart.rect.x = 600
            continue_button.rect.x = 600
            menu_button.rect.x = 600
            lvl3 = True
            lvl3_break = False
            des_walls = []
            walls  = []
            speed_y = 2
            speed_x = 2
            ball.rect.x = 75
            ball.rect.y = 300
            plat_weap.rect.x = 100
            plat_weap.rect.y = 400
            plat.rect.x = 600
            boss.rect.x = 100
            boss.rect.y = 0
            coldown = 0 
            bullets = []
            rockets = []
            drons = []
            x = 0

            for i in range(3):
                wall = Picture(x,200,150,80,color_c,'Wall.png',4,0)
                wall.imge = pg.transform.scale(wall.imge,(700,500))
                wall.draw_picture()
                walls.append(wall)
                x += 175
            
            if boss.hp == 2:
                boss.set_picture('2hp_Boss.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))
                speed_boss = 3
            elif boss.hp == 1:
                boss.set_picture('1hp_Boss.png')
                boss.imge = pg.transform.scale(boss.imge,(700,700))
                speed_boss = 4

            new_screen.fill()

        plat_weap.draw_picture()
        boss.draw_picture()

        pg.display.update()
        clock.tick(40) 



        

