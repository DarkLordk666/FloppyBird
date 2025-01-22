ขั้นตอนที่ 1
pip install pygame

ขั้นตอนที่ 2

rmdir /s /q dist
rmdir /s /q build
del flappy_bird.

rmdir /s /q dist
rmdir /s /q build
del floppy_chicken.

pyinstaller --onefile --noconsole --distpath ./output floppy_chicken.py

Backup Code

import pygame
import random
import webbrowser
import sys  # เพิ่มการนำเข้า sys

# Initializing pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.25
FLAP_STRENGTH = -6
PIPE_WIDTH = 60
PIPE_GAP = 150
BIRD_WIDTH = 40
BIRD_HEIGHT = 40

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Floppy Chicken')

# Load assets
bird_img = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_img.fill((255, 255, 0))  # Bird color is yellow for simplicity
bg_color = (0, 0, 255)  # Background color (sky blue)
pipe_color = (0, 255, 0)  # Pipe color (green)

# Fonts
font_large = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)

# Global variable for high score
high_score = 0

# Define classes for Bird and Pipe
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(150, HEIGHT - 150)
        self.top = self.height - HEIGHT
        self.bottom = self.height + PIPE_GAP
        self.width = PIPE_WIDTH

    def update(self):
        self.x -= 3

    def draw(self):
        pygame.draw.rect(screen, pipe_color, (self.x, 0, self.width, self.height))
        pygame.draw.rect(screen, pipe_color, (self.x, self.bottom, self.width, HEIGHT - self.bottom))

# Home Screen
def home_screen():
    running = True
    while running:
        screen.fill(bg_color)
        title_text = font_large.render("Floppy Chicken", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Buttons
        start_button = pygame.Rect(WIDTH // 2 - 75, 200, 150, 50)
        settings_button = pygame.Rect(WIDTH // 2 - 75, 300, 150, 50)
        donate_button = pygame.Rect(WIDTH // 2 - 75, 400, 150, 50)
        exit_button = pygame.Rect(WIDTH // 2 - 75, 500, 150, 50)

        pygame.draw.rect(screen, (255, 0, 0), start_button)
        pygame.draw.rect(screen, (0, 255, 0), settings_button)
        pygame.draw.rect(screen, (0, 0, 255), donate_button)
        pygame.draw.rect(screen, (128, 128, 128), exit_button)

        screen.blit(font_small.render("Start", True, (255, 255, 255)), (WIDTH // 2 - 35, 215))
        screen.blit(font_small.render("Settings", True, (255, 255, 255)), (WIDTH // 2 - 50, 315))
        screen.blit(font_small.render("Donate", True, (255, 255, 255)), (WIDTH // 2 - 40, 415))
        screen.blit(font_small.render("Exit", True, (255, 255, 255)), (WIDTH // 2 - 25, 515))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    menu_screen()
                if settings_button.collidepoint(event.pos):
                    settings_screen()
                if donate_button.collidepoint(event.pos):
                    webbrowser.open("https://www.patreon.com")
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Settings Screen
def settings_screen():
    running = True
    while running:
        screen.fill(bg_color)
        title_text = font_large.render("Settings", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Back button
        back_button = pygame.Rect(WIDTH // 2 - 50, 400, 100, 50)
        pygame.draw.rect(screen, (255, 0, 0), back_button)
        screen.blit(font_small.render("Back", True, (255, 255, 255)), (WIDTH // 2 - 25, 415))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return

# Menu Screen
def menu_screen():
    running = True
    while running:
        screen.fill(bg_color)
        title_text = font_large.render("Game Levels", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Level 1 button
        level1_button = pygame.Rect(WIDTH // 2 - 75, 200, 150, 50)
        home_button = pygame.Rect(WIDTH // 2 - 75, 400, 150, 50)

        pygame.draw.rect(screen, (255, 0, 0), level1_button)
        pygame.draw.rect(screen, (128, 128, 128), home_button)

        screen.blit(font_small.render("Level 1", True, (255, 255, 255)), (WIDTH // 2 - 40, 215))
        screen.blit(font_small.render("Home", True, (255, 255, 255)), (WIDTH // 2 - 30, 415))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1_button.collidepoint(event.pos):
                    game_loop()
                if home_button.collidepoint(event.pos):
                    home_screen()

# Game Over Screen
def game_over_screen(score, high_score):
    running = True
    while running:
        screen.fill(bg_color)
        title_text = font_large.render("Game Over", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Display current score and high score
        score_text = font_small.render(f"Score: {score}", True, (255, 255, 255))
        high_score_text = font_small.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))
        screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, 250))

        # Buttons
        retry_button = pygame.Rect(WIDTH // 2 - 75, 350, 150, 50)
        menu_button = pygame.Rect(WIDTH // 2 - 75, 450, 150, 50)

        pygame.draw.rect(screen, (255, 0, 0), retry_button)
        pygame.draw.rect(screen, (0, 255, 0), menu_button)

        screen.blit(font_small.render("Retry", True, (255, 255, 255)), (WIDTH // 2 - 35, 365))
        screen.blit(font_small.render("Back to Menu", True, (255, 255, 255)), (WIDTH // 2 - 60, 465))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    game_loop()
                if menu_button.collidepoint(event.pos):
                    menu_screen()

# Main game loop
def game_loop():
    global high_score  # ใช้ตัวแปร global
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()
    running = True
    score = 0

    while running:
        screen.fill(bg_color)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # Bird update
        bird.update()

        # Pipe update
        for pipe in pipes:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                pipes.append(Pipe())
                score += 1  # เพิ่มคะแนนเมื่อท่อเลื่อนออกจากหน้าจอ
                if score > high_score:  # อัปเดต high_score ถ้าคะแนนมากกว่า
                    high_score = score

        # Drawing
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        # Display the score
        score_text = font_small.render(str(score), True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        # Check for collision
        if bird.y <= 0 or bird.y >= HEIGHT - BIRD_HEIGHT:
            running = False

        for pipe in pipes:
            if bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + BIRD_HEIGHT > pipe.bottom:
                    running = False

        # Update the display
        pygame.display.update()
        clock.tick(FPS)

    # Show game over screen
    game_over_screen(score, high_score)

if __name__ == '__main__':
    home_screen()
