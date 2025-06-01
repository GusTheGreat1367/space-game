import pygame
import time
import random
import pyautogui
from tkinter import *
root = Tk()
Button(root, text="start", command=root.destroy).pack() #button to close the window
root.mainloop()





WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CONQUER THE GALAXY")
font = pygame.font.Font('timesnewroman', 25)

player = pygame.draw.circle(display, (100, 0, 0), (0, 0), 50, 0)
x, y = pyautogui.position()
if pyautogui.click and pyautogui.position() == player:
    print('hi')
    
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

def draw(player):
    WIN.blit(BG)

def main():
    run = True

    while run:
        print (clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
pygame.quit()

if __name__ == "__main__":
    main
