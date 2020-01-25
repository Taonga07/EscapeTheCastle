import pygame
import Main_account
import time

def run():
    size = 600
    pygame.display.init()
    screen = pygame.display.set_mode((size, size))

    for i in range(0 , size , 25):
        pygame.draw.line (screen, (0, 250, 0), (0, i), (i, size), 1)
        pygame.draw.line (screen, (0, 250, 0), (i, 0), (size, i), 1)
        pygame.draw.line (screen, (0, 250, 0), (size - i, 0), (0,i), 1)
        pygame.draw.line (screen, (0, 250, 0), (i, size), (size ,size - i), 1)
        
        time.sleep(0.5)
        pygame.display.flip()
        

    pygame.quit()
    Main_account.Open()

if __name__ =="__main__":
    run()
