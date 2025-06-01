import pygame
import random
import pyautogui
from tkinter import *

# --- Tkinter intro window ---
def start_game():
    start_root.quit()  # Use quit instead of destroy for mainloop

start_root = Tk()
start_root.title("Start Game")
Button(start_root, text="Start", command=start_game).pack()
start_root.mainloop()
start_root.destroy()  # Properly destroy the window after mainloop ends

# --- Initialize pygame ---
pygame.init()

money = 0
population = 1000000

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CONQUER THE GALAXY")

player_pos = [WIDTH // 2, HEIGHT // 2]
player_radius = 100

# Load background image with fallback
try:
    BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))
except pygame.error:
    BG = pygame.Surface((WIDTH, HEIGHT))
    BG.fill((0, 0, 0))  # fallback color

# Random economy assignment
economy_types = ["Agriculture", "Mining", "Trade", "Science"]
economy = random.choice(economy_types)
print("Economy type:", economy)
money += 10000

# --- Explore popup using tkinter ---
def explore_prompt():
    prompt = Toplevel()  # Use Toplevel instead of Tk for additional windows
    prompt.title("Explore the galaxy?")
    prompt.geometry("300x100")

    def on_yes():
        global money
        money -= 10000
        prompt.destroy()

    def on_no():
        global money
        money += 10000
        prompt.destroy()

    Label(prompt, text="Explore a new galaxy?").pack(pady=10)
    Button(prompt, text="Yes", command=on_yes).pack(side="left", padx=20)
    Button(prompt, text="No", command=on_no).pack(side="right", padx=20)

    # Make the popup modal
    prompt.grab_set()
    prompt.wait_window()

# --- Game Loop ---
def main():
    global money, population

    clock = pygame.time.Clock()
    last_money_increment = pygame.time.get_ticks()
    increment_interval = 5000  # every 5 seconds
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dist = ((mouse_x - player_pos[0]) ** 2 + (mouse_y - player_pos[1]) ** 2) ** 0.5
                if dist <= player_radius:
                    # Show popup using pyautogui
                    pyautogui.alert(
                        text=f"Money: {money}\nPopulation: {population}\nTime: {pygame.time.get_ticks() // 1000}s",
                        title="Player Info"
                    )

        # Draw background and player
        WIN.blit(BG, (0, 0))
        pygame.draw.circle(WIN, (255, 0, 0), player_pos, player_radius)

        # Economy-based income
        current_time = pygame.time.get_ticks()
        if current_time - last_money_increment >= increment_interval:
            money += 1000
            population += 1000
            last_money_increment = current_time
            print(f"Money: {money}, Population: {population}")

            if (current_time // 60000) % 2 == 1:
                explore_prompt()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# --- Run the game ---
if __name__ == "__main__":
    main()
