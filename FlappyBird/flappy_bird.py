import pygame
import random
import webbrowser

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
pygame.display.set_caption('Flappy Bird')

# Load assets
bird_img = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_img.fill((255, 255, 0))  # Bird color is yellow for simplicity
bg_color = (0, 0, 255)  # Background color (sky blue)
pipe_color = (0, 255, 0)  # Pipe color (green)

# Fonts
font_large = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)

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
        title_text = font_large.render("Flappy Bird", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Buttons
        start_button = pygame.Rect(WIDTH // 2 - 75, 200, 150, 50)
        settings_button = pygame.Rect(WIDTH // 2 - 75, 300, 150, 50)
        donate_button = pygame.Rect(WIDTH // 2 - 75, 400, 150, 50)

        pygame.draw.rect(screen, (255, 0, 0), start_button)
        pygame.draw.rect(screen, (0, 255, 0), settings_button)
        pygame.draw.rect(screen, (0, 0, 255), donate_button)

        screen.blit(font_small.render("Start", True, (255, 255, 255)), (WIDTH // 2 - 35, 215))
        screen.blit(font_small.render("Settings", True, (255, 255, 255)), (WIDTH // 2 - 50, 315))
        screen.blit(font_small.render("Donate", True, (255, 255, 255)), (WIDTH // 2 - 40, 415))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    menu_screen()
                if settings_button.collidepoint(event.pos):
                    settings_screen()
                if donate_button.collidepoint(event.pos):
                    webbrowser.open("https://www.patreon.com")

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
                exit()
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
        pygame.draw.rect(screen, (255, 0, 0), level1_button)
        screen.blit(font_small.render("Level 1", True, (255, 255, 255)), (WIDTH // 2 - 40, 215))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level1_button.collidepoint(event.pos):
                    game_loop()

# Main game loop
def game_loop():
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
                running = False
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
                score += 1  # Increase score when pipe moves off screen

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

    # Game over
    pygame.quit()

if __name__ == '__main__':
    home_screen()




# import pygame
# import random

# # Initializing pygame
# pygame.init()

# # Define constants
# WIDTH, HEIGHT = 400, 600
# FPS = 60
# GRAVITY = 0.25
# FLAP_STRENGTH = -6
# PIPE_WIDTH = 60
# PIPE_GAP = 150
# BIRD_WIDTH = 40
# BIRD_HEIGHT = 40

# # Set up screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Flappy Bird')

# # Load assets
# bird_img = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
# bird_img.fill((255, 255, 0))  # Bird color is yellow for simplicity
# bg_color = (0, 0, 255)  # Background color (sky blue)
# pipe_color = (0, 255, 0)  # Pipe color (green)

# # Define classes for Bird and Pipe
# class Bird:
#     def __init__(self):
#         self.x = WIDTH // 4
#         self.y = HEIGHT // 2
#         self.velocity = 0

#     def update(self):
#         self.velocity += GRAVITY
#         self.y += self.velocity

#     def flap(self):
#         self.velocity = FLAP_STRENGTH

#     def draw(self):
#         screen.blit(bird_img, (self.x, self.y))

# class Pipe:
#     def __init__(self):
#         self.x = WIDTH
#         self.height = random.randint(150, HEIGHT - 150)
#         self.top = self.height - HEIGHT
#         self.bottom = self.height + PIPE_GAP
#         self.width = PIPE_WIDTH

#     def update(self):
#         self.x -= 3

#     def draw(self):
#         pygame.draw.rect(screen, pipe_color, (self.x, 0, self.width, self.height))
#         pygame.draw.rect(screen, pipe_color, (self.x, self.bottom, self.width, HEIGHT - self.bottom))

# # Main game loop
# def main():
#     bird = Bird()
#     pipes = [Pipe()]
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     while running:
#         screen.fill(bg_color)
        
#         # Event handling
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     bird.flap()

#         # Bird update
#         bird.update()

#         # Pipe update
#         for pipe in pipes:
#             pipe.update()
#             if pipe.x + PIPE_WIDTH < 0:
#                 pipes.remove(pipe)
#                 pipes.append(Pipe())
#                 score += 1  # Increase score when pipe moves off screen

#         # Drawing
#         bird.draw()
#         for pipe in pipes:
#             pipe.draw()

#         # Display the score
#         font = pygame.font.Font(None, 36)
#         score_text = font.render(str(score), True, (255, 255, 255))
#         screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

#         # Check for collision
#         if bird.y <= 0 or bird.y >= HEIGHT - BIRD_HEIGHT:
#             running = False

#         for pipe in pipes:
#             if bird.x + BIRD_WIDTH > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
#                 if bird.y < pipe.height or bird.y + BIRD_HEIGHT > pipe.bottom:
#                     running = False

#         # Update the display
#         pygame.display.update()
#         clock.tick(FPS)

#     # Game over
#     pygame.quit()

# if __name__ == '__main__':
#     main()

