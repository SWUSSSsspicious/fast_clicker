import pygame
from time import *
from random import randint
pygame.init()
#cоздаем окно программы
back=(229,204,255)
mv=pygame.display.set_mode((500,500))
mv.fill(back)
clock=pygame.time.Clock()
#класс прямоугольник
class Area():
    def __init__(self, x=0, y=0, width=10, hight=10, color=None):
        self.rect=pygame.Rect(x, y, width, hight)
        self.fill_color=color
    def color(self, new_color):
        self.fill_color=new_color
    def fill(self):
        pygame.draw.rect(mv, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect( mv, frame_color, self.rect, thickness)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x, y)
#Класс надпись

class Lable(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image=pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mv.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
RED=(254,24,24)
GREEN = (0, 255, 51)
YELLOW=(250,250,0)
DARK_BLUE=(0,0,153)
BLUE=(51,51,255)
cards=list()
num_cards=4
x=70
start_time=time()
cur_time=start_time
#Создание интрефейса игры
time_text=Lable(0,0,50,50,back)
time_text.set_text('Время:', 40, DARK_BLUE)
time_text.draw(20,20)

timer=Lable(50,55,50,40, back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)

score_text=Lable(380,0,50,50,back)
score_text.set_text('Счет', 45,DARK_BLUE)
score_text.draw(20,20)

score=Lable(440,55,50,40, back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)
for i in range(4):
    new_card=Lable(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x+=100
wait=0
points=0
while True:
    #Отрисовка карточек и отображение кликов
    if wait==0:
        wait=10
        click=randint(1,num_cards)
        for i in range(num_cards):
            cards[i].color((YELLOW))
            if (i+1)==click:
                cards[i].draw(10,40)
            else:
                cards[i].fill()
    else:
        wait-=1
    pygame.display.update()
    clock.tick(40)
    #Обработка кликов по карточкам
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            x,y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if (i+1)==click:
                        cards[i].color(GREEN)
                        points-=1
                    else:
                        cards[i].color(RED)
                        points+=1
                    cards[i].fill()
                    score.set_text(str(points), 40, DARK_BLUE)
                    score.draw(0,0) 
    #Выигрыш и проигрыш
    new_time=time()
    if new_time-start_time>=11:
        win=Lable(0,0,500,500,RED)
        win.set_text('Время вышло!!!', 60, DARK_BLUE)
        win.draw(110,180)
        break
    if int(new_time)-int(cur_time)==1:
        timer.set_text(str(int(new_time-start_time)), 40, DARK_BLUE)
        timer.draw(0,0)
        cur_time=new_time
    if points>=5:
        win=Lable(0,0,500,500,GREEN)
        win.set_text('Ты победил!!!', 60, DARK_BLUE)
        win.draw(140,180)
        result_time=Lable (90,230,250,250, GREEN)
        result_time.set_text('Время прохождения: '+ str(int(new_time-start_time))+ ' сек',40, DARK_BLUE)
        result_time.draw(0,0)
        break
    pygame.display.update()
    clock.tick(40)
pygame.display.update()
