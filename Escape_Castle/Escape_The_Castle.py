import pygame
from pygame.locals import *
import os
import random

#I think this was written in python2, there are a few changes to python3 when using classes
#you have 4 classes - player, sword, ghost, armour
#they all share some attributes (x, y, width, height)
#you've sort of recognised this as spike and ghost are child classes from armour - they inherit from armour class
#however, I think if you make a single parent class - game_object then everything can inherit from that and it becomes a little clearer

class GameObject(): #note you don't need to specify that this is an object in python3
    #its also convention to put a capital letter on your class
    def __init__(self, x, y, width, height): #all your sub-classes have these attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height

#player class
class Player(GameObject): #our Player is now a sub-class of GameObject
    # shouldn't really have variables ouside the __init__
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height) #this allows us to use the game_object variables
        self.run = [pygame.image.load(os.path.join('.images', str(x) + '.png')) for x in range(8,16)]
        self.jump = [pygame.image.load(os.path.join('.images', str(x) + '.png')) for x in range(1,8)]
        self.slide = [pygame.image.load(os.path.join('.images', 'S1.png')),
                        pygame.image.load(os.path.join('.images', 'S2.png')),
                        pygame.image.load(os.path.join('.images', 'S2.png')),  
                        pygame.image.load(os.path.join('.images', 'S2.png')), 
                        pygame.image.load(os.path.join('.images', 'S2.png')),
                        pygame.image.load(os.path.join('.images', 'S2.png')), 
                        pygame.image.load(os.path.join('.images', 'S2.png')), 
                        pygame.image.load(os.path.join('.images', 'S2.png')), 
                        pygame.image.load(os.path.join('.images', 'S3.png')), 
                        pygame.image.load(os.path.join('.images', 'S4.png')), 
                        pygame.image.load(os.path.join('.images', 'S5.png'))]
        self.fall = pygame.image.load(os.path.join('.images','0.png'))
        self.jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
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
            elif self.slideCount > 20 and self.slideCount < 80: #reorded to be a little more logical
                self.hitbox = (self.x,self.y+3,self.width-8,self.height-35)      
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            if self.slideCount >= 110: #what happens if slideCount is between 80 and 110?
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

#obsacles classes includes(armor,spike)
class Armor(GameObject): #now a sub-class of GameObject
    def __init__(self,x,y,width,height):
        super().__init__(x, y, width, height) #and inherits attributes from GameObject
        self.img = [pygame.image.load(os.path.join('.images', 'Knight1.png')),pygame.image.load(os.path.join('.images', 'Knight2.png')),pygame.image.load(os.path.join('.images', 'Knight3.png'))]
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

class Spike(GameObject): #now a sub-class of GameObject
    def __init__(self,x,y,width,height):
        super().__init__(x, y, width, height) #and inherits attributed from GameObject
        #I think you had your images named wrong, I've renamed them in the order they get bigger
        self.img = [pygame.image.load(os.path.join('.images', 'Spike.png')), 
                pygame.image.load(os.path.join('.images', 'Spike1.png')), 
                pygame.image.load(os.path.join('.images', 'Spike2.png'))]
        self.costume = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]
        self.number = 0
        #self.img_count = self.move[no] this isn't needed

    def draw(self,screen):
        if self.costume[self.number] == 0:
            self.hitbox = (self.x, self.y, 80,500)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        elif self.costume[self.number] == 1:
            self.hitbox = (self.x, self.y, 80,520)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        elif self.costume[self.number] == 2: #you don't have a fourth costume
            self.hitbox = (self.x, self.y, 80,530)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        screen.blit(self.img[self.costume[self.number]], (self.x,self.y))
        self.number += 1
        if self.number == len(self.costume):
            self.number = 0

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False

#reward/punishments classes(gohst,sword)
#I would make a reward class, and then ghosts & swords as sub-classes
class Reward(GameObject):
    def __init__(self,x,y,width,height):
        super().__init__(x, y, width, height)
    #our collide function for rewards is the same for ghosts and swords
    #so we can put it here and only write it out once
    def collide(self, rect):
                if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
                    if rect[1] < self.hitbox[1]:
                        return True
                return False
    #and so is your draw for rewards
    def draw(self,screen):
        self.hitbox = (self.x, self.y, 50,50)  # defines the hitbox
        #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        screen.blit(pygame.transform.scale(self.img, (50,50)), (self.x,self.y))

class Ghost(Reward): #Ghosts are sub-classes of Reward, which is a sub-class of GameObject
    def __init__(self,x,y,width,height):
        super().__init__(x, y, width, height) #everything inherits back to GameObject
        self.img = pygame.image.load(os.path.join('.images', 'ghost.png'))

class Sword(Reward):
    def __init__(self,x,y,width,height):
        super().__init__(x, y, width, height)
        self. img = pygame.image.load(os.path.join('.images', 'sword.png'))

#writing score to a file
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


#screens(wining and end)
def winScreen():
    global pause, score, swords, speed, obstacles #oooh, bad globals - should pass arguments to function and return if needed
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
        currentScore = largeFont.render('Your_Score: '+ str(score),1,(56,7,12))
        screen.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
        screen.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0
    swords = 0

        
#where the blitting the classes to the screee happen

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

#maiin game loop
def run_main_game():
    
    #setting the window
    pygame.init()
    W, H = 580, 570
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Escape the castle!')
    bg = pygame.image.load(os.path.join('.images','bg.png')).convert()
    bgX = 0
    bgX2 = bg.get_width()
    clock = pygame.time.Clock()

    #making stuff happen

    pygame.time.set_timer(USEREVENT+1, 500)
    pygame.time.set_timer(USEREVENT+2, 9000)
    pygame.time.set_timer(USEREVENT+3, 900)
    
    #main varibles,lists
    speed = 30
    score = 0
    swords = 0

    run = True
    hero = Player(100,517,64,64)

    obstacles = []
    rewards = []
    pause = 0
    fallSpeed = 0

    #calling end or win screen
    while run:
        if pause > 0:
            pause += 1
            if pause > fallSpeed * 2:
                endScreen()
        if score >= 100:
            winScreen()
        
     #blitting the obsticles(knight/spike)
        for obstacle in obstacles:
            if obstacle.collide(hero.hitbox):
                if type(obstacle) == Armor:
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
        #blitting reward/punisments(sword or ghost)        
        for thing in rewards:
            if thing.collide(hero.hitbox):
                if type(thing) == Sword:
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
        
        #scrolling screen
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

         #bitting stuff to screen with events       
            if event.type == USEREVENT+1:
                speed += 1
                
            if event.type == USEREVENT+2:
                r = random.randrange(0,2)
                if r == 0:
                    obstacles.append(Armor(810,110,64,64))
                elif r == 1:
                    obstacles.append(Spike(810, 0, 48, 310))
            
            if event.type == USEREVENT+3:
                a = random.randrange(0,2)
                if a == 0:
                    rewards.append(Sword(200,400,50,50))
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
