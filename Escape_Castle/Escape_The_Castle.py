import pygame
from pygame.locals import *
import os
import random




class player(object):
    run = [pygame.image.load(os.path.join('.images', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('.images', str(x) + '.png')) for x in range(1,8)]
    slide = [pygame.image.load(os.path.join('.images', 'S1.png')),pygame.image.load(os.path.join('.images', 'S2.png')),pygame.image.load(os.path.join('.images', 'S2.png')),pygame.image.load(os.path.join('.images', 'S2.png')), pygame.image.load(os.path.join('.images', 'S2.png')),pygame.image.load(os.path.join('.images', 'S2.png')), pygame.image.load(os.path.join('.images', 'S2.png')), pygame.image.load(os.path.join('.images', 'S2.png')), pygame.image.load(os.path.join('.images', 'S3.png')), pygame.image.load(os.path.join('.images', 'S4.png')), pygame.image.load(os.path.join('.images', 'S5.png'))]
    fall = pygame.image.load(os.path.join('.images','0.png'))
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
    def draw(self, screen):
        if self.falling:
            screen.blit(self.fall, (self.x, self.y + 30))        
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            screen.blit(self.jump[self.jumpCount//18], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x+ 4,self.y,self.width-24,self.height-10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                self.hitbox = (self.x+ 4,self.y,self.width-24,self.height-10)
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x,self.y+3,self.width-8,self.height-35)      
            if self.slideCount >= 110:
                self.slideCount = 0
                self.runCount = 0
                self.slideUp = False
                self.hitbox = (self.x+ 4,self.y,self.width-24,self.height-10)
            screen.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1       
        else:
            if self.runCount > 42:
                self.runCount = 0
            screen.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (self.x+ 4,self.y,self.width-24,self.height-13)
        #pygame.draw.rect(screen, (255,0,0),self.hitbox, 2)

class armor(object):
    img = [pygame.image.load(os.path.join('.images', 'Knight1.png')),pygame.image.load(os.path.join('.images', 'Knight2.png')),pygame.image.load(os.path.join('.images', 'Knight3.png'))]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.costume = random.randint(0, 2)
    def draw(self,screen):
        self.hitbox = (self.x, self.y, 150,460)
        #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        screen.blit(pygame.transform.scale(self.img[self.costume], (150,460)), (self.x,self.y))
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
class spike(armor):
    img = [pygame.image.load(os.path.join('.images', 'Spike.png')), pygame.image.load(os.path.join('.images', 'Spike1.png')), pygame.image.load(os.path.join('.images', 'Spike2.png'))]
    move = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]
    no = 0
    img_count = move[no]
    def draw(self,screen):
        if self.img_count == 0:
            self.hitbox = (self.x, self.y, 80,500)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        elif self.img_count == 2:
            self.hitbox = (self.x, self.y, 80,520)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        elif self.img_count == 3:
            self.hitbox = (self.x, self.y, 80,530)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        elif self.img_count == self.move[29]:
            self.no = 0
        screen.blit(self.img[self.img_count], (self.x,self.y))
        self.no += 1
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False

class Ghost(armor):
    img = pygame.image.load(os.path.join('.images', 'ghost.png'))
    def draw(self,screen):
        self.hitbox = (self.x, self.y, 50,50)  # defines the hitbox
        #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        screen.blit(pygame.transform.scale(self.img, (50,50)), (self.x,self.y))
    def collide(self, rect):
                if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
                    if rect[1] < self.hitbox[1]:
                        return True
                return False            
class sword(armor):
    img = pygame.image.load(os.path.join('.images', 'sword.png'))
    def draw(self,screen):
        self.hitbox = (self.x, self.y, 50,50)  # defines the hitbox
        #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        screen.blit(pygame.transform.scale(self.img, (50,50)), (self.x,self.y))
    def collide(self, rect):
                if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
                    if rect[1] < self.hitbox[1]:
                        return True
                return False
def updateFile():
    f = open('.scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('.scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score
               
    return last



def winScreen():
    global pause, score, swords, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []
                   
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                hero.falling = False
                hero.sliding = False
                hero.jumpin = False
                
        screen.blit(bg, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(56,7,12))
        currentScore = largeFont.render('Your_Score: '+ str(score),1,(56,7,12))
        #screen.blit(largeFont.render('well done you won'))
        screen.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
        screen.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0
    swords = 0
    
def endScreen():
    global pause, score, swords, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []
                   
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                hero.falling = False
                hero.sliding = False
                hero.jumpin = False
                
        screen.blit(bg, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(56,7,12))
        currdef redrawscreen(screen, bg, bgX, bgX2, score, swords, hero, obstacles, rewards):
entScore = largeFont.render('Your_Score: '+ str(score),1,(56,7,12))
        screen.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
        screen.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0
    swords = 0

        


def redrawscreen(screen, bg, bgX, bgX2, score, swords, hero, obstacles, rewards):
    largeFont = pygame.font.SysFont('comicsans', 30)
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2,0))
    text = largeFont.render('Score: ' + str(score), 1, (255,255,255))
    text1 = largeFont.render('Swords: ' + str(swords), 1, (255,255,255))
    screen.blit(text, (2,30))
    screen.blit(text1, (2, 10))
    hero.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)
    for thing in rewards:
        thing.draw(screen)
    screen.blit(text, (700, 10))
    pygame.display.update()

def run_main_game():
    
    pygame.init()
    W, H = 580, 570
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Escape the castle!')
    bg = pygame.image.load(os.path.join('.images','bg.png')).convert()
    bgX = 0
    bgX2 = bg.get_width()
    clock = pygame.time.Clock()

    pygame.time.set_timer(USEREVENT+1, 500)
    pygame.time.set_timer(USEREVENT+2, 9000)
    pygame.time.set_timer(USEREVENT+3, 900)
    speed = 30

    score = 0
    swords = 0

    run = True
    hero = player(100,517,64,64)

    obstacles = []
    rewards = []
    pause = 0
    fallSpeed = 0

    while run:
        if pause > 0:
            pause += 1
            if pause > fallSpeed * 2:
                endScreen()
        if score >= 100:
            winScreen()
        
        for obstacle in obstacles:
            if obstacle.collide(hero.hitbox):
                if type(obstacle) == armor:
                    if swords >= 3:
                        obstacles.pop(obstacles.index(obstacle))
                        swords -= 5
                        score += 1
                    else:
                        hero.falling = True
                        if pause == 0:
                            pause = 1
                            fallSpeed = speed
                            score -= 1
                else:
                    hero.falling = True
                    if pause == 0:
                        pause = 1
                        fallSpeed = speed
                        score -= 1
            if obstacle.x < obstacle.width * -1:
                obstacles.pop(obstacles.index(obstacle))
                score += 1
            else:
                obstacle.x -= 1.4
                
        for thing in rewards:
            if thing.collide(hero.hitbox):
                if type(thing) == sword:
                    swords += 1
                    rewards.pop(rewards.index(thing))
                if type(thing) == Ghost:
                    if swords >= 1:
                        swords -= 1
                        rewards.pop(rewards.index(thing))
                    else:
                        swords = 0
                        rewards.pop(rewards.index(thing))
            if thing.x < thing.width * -1:
                rewards.pop(rewards.index(thing))
            else:
                thing.x -= 1.4
        
        bgX -= 1.4
        bgX2 -= 1.4

        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width() 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False 
                raise SystemExit
                
            if event.type == USEREVENT+1:
                speed += 1
                
            if event.type == USEREVENT+2:
                r = random.randrange(0,2)
                if r == 0:
                    obstacles.append(armor(810,110,64,64))
                elif r == 1:
                    obstacles.append(spike(810, 0, 48, 310))
            
            if event.type == USEREVENT+3:
                a = random.randrange(0,2)
                if a == 0:
                    rewards.append(sword(200,400,50,50))
                elif a == 1:
                    rewards.append(Ghost(200,400,50,50))
                    
        if hero.falling == False:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                if not(hero.jumping):
                    hero.jumping = True

            if keys[pygame.K_DOWN]:
                if not(hero.sliding):
                    hero.sliding = True

        clock.tick(speed)
        redrawscreen(screen, bg, bgX, bgX2, score, swords, hero, obstacles, rewards)


if __name__ == '__main__':
    run_main_game()
