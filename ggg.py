import pygame
import random
import pyautogui
from tkinter import *
root = Tk()
Button(root, text="start", command=root.destroy).pack() #button to close the window
root.mainloop()



# Initialize pygame
pygame.init()

money = 0
population = 1000000

display = WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CONQUER THE GALAXY")

player_pos = [WIDTH // 2, HEIGHT // 2]  # Center position
player_radius = 100  # Reduced radius for better visuals

# Load background image
try:
    BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
except pygame.error:
    BG = pygame.Surface((WIDTH, HEIGHT))
    BG.fill((0, 0, 0))

player = pygame.draw.circle(WIN, (255, 0, 0), player_pos, player_radius)

clock = pygame.time.Clock()
if pyautogui.click and pyautogui.position() == player:
    print('hi')
if clock == 60000:
    print('Explore the galaxy?')
    root1 = Tk()
    root1.title("Explore?")
    root1.geometry("300x100")
    def y():
        root1.destroy()
        money -= 10000
    def n():
        root1.destroy()
        money += 10000
    Button(root1, text="Yes", command=y).pack(side='left', padx=20)
    Button(root1, text="No", command=n).pack(side='right', padx=20)

def main():
    
    last_money_increment = pygame.time.get_ticks()
    increment_interval = 5000  # milliseconds
    run = True
    
    # Choose a random economy type
    

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        print (population)
        print (money)
        print (clock)
        WIN.blit(BG, (0, 0))
        player = pygame.draw.circle(WIN, (255, 0, 0), player_pos, player_radius)

        current_time = pygame.time.get_ticks()
        if current_time - last_money_increment >= increment_interval:
            money += 1000
            population += 1000
            last_money_increment = current_time

        # Display economy and money (simple text)
        font = pygame.font.SysFont(None, 36)
        text = font.render("timesnewroman", True, (255, 255, 255))
        WIN.blit(text, (20, 20))

        pygame.display.update()
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
