import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
COOKIE_SIZE = 100
COOKIE_COLOR = (255, 215, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Initialize variables
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (
                x >= WIDTH / 2 - COOKIE_SIZE / 2
                and x <= WIDTH / 2 + COOKIE_SIZE / 2
                and y >= HEIGHT / 2 - COOKIE_SIZE / 2
                and y <= HEIGHT / 2 + COOKIE_SIZE / 2
            ):
                score += 1

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the cookie
    pygame.draw.circle(
        screen,
        COOKIE_COLOR,
        (WIDTH // 2, HEIGHT // 2),
        COOKIE_SIZE // 2,
    )

    # Display the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
