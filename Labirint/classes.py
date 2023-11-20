import pygame as pg

class Sprite():
    def __init__(self,x,y,weight,height,image):
        self.rect = pg.Rect(x,y,weight,height)
        self.imge = pg.transform.scale(pg.image.load(image),(weight,height))

    def draw_picture(self,window):
        window.blit(self.imge,(self.rect.x,self.rect.y))


class Player(Sprite):
    def __init__(self,x,y,weight,height,image,x_speed,y_speed):
        super().__init__(x,y,weight,height,image)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rect = pg.Rect(x,y,weight,height)
        self.imge = pg.transform.scale(pg.image.load(image),(weight,height))

    def update(self,speed_number,move):
        if move == 'horizontal':
            self.rect.x += self.x_speed * speed_number
        elif move == 'up':
            self.rect.y += self.y_speed * speed_number

    def collide(self,somebody):
        return pg.sprite.collide_rect(self,somebody)

    def shot(self,w,h,image_b,look_bul,list_name):
        bullet = Bullet(self.rect.x+50,self.rect.centery,w,h,image_b,3,3,look_bul)
        list_name.append(bullet)   

class Enemy(Sprite):
    def __init__(self,x,y,weight,height,image,x_speed,y_speed):
        super().__init__(x,y,weight,height,image)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rect = pg.Rect(x,y,weight,height)
        self.imge = pg.transform.scale(pg.image.load(image),(weight,height))

    def update(self):
        self.rect.y += self.y_speed
        if self.rect.y == 200:
            self.y_speed *= -1
        elif self.rect.y == 0:
            self.y_speed *= -1                    


class Bullet(Player):
    def __init__(self,x,y,weight,height,image,x_speed,y_speed,direction):
        super().__init__(x,y,weight,height,image,x_speed,y_speed)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rect = pg.Rect(x,y,weight,height)
        self.imge = pg.transform.scale(pg.image.load(image),(weight,height))
        self.direction = direction
       
    def update(self):
        if self.direction == 'up':
            self.rect.y -= 3
        elif self.direction == 'down':
            self.rect.y += 3
        elif self.direction == 'right':
            self.rect.x += 3
        elif self.direction == 'left':
            self.rect.x -= 3

    def kill(self,enemy,list_name):
        if self.collide(enemy):
            enemy.rect.x = 800
            list_name.remove(self)
        