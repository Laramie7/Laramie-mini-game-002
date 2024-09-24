import pygame
import sys
import random
from pygame import mixer


pygame.init()
mixer.init()

mixer.music.load('rb.mp3')  # Replace with your file path
mixer.music.set_volume(2.0)  # Set volume (0.0 to 1.0)
mixer.music.play(-1)  # -1 means the music will loop indefinitely

width, height = 700, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Average game!!! USE ARROWS TO MOVE ARROUND")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

dot_size = 15
dot_x, dot_y = width // 2, height // 2
dot_speed = 10
# Modify this to change difficulty as you want 
cube_size = 100
cube_speed = 5
num_cubes = 30

cube_colors = [blue, red, green]  

cubes = []
for _ in range(num_cubes):
    cube_x = random.randint(0, width - cube_size)
    cube_y = random.randint(0, height - cube_size)
    cube_speed_x = random.choice([-cube_speed, cube_speed])
    cube_speed_y = random.choice([-cube_speed, cube_speed])
    cube_color = random.choice(cube_colors)
    cubes.append([cube_x, cube_y, cube_speed_x, cube_speed_y, cube_color])

font = pygame.font.Font(None, 36)

start_ticks = pygame.time.get_ticks()

running = True
game_over = False
extreme_mode = False

def draw_restart_menu():
    screen.fill(white)
    restart_text = font.render("Press R to Restart, E for Dim mode, or Q to Quit", True, red)
    screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 - restart_text.get_height() // 2))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dot_x -= dot_speed
        if keys[pygame.K_RIGHT]:
            dot_x += dot_speed
        if keys[pygame.K_UP]:
            dot_y -= dot_speed
        if keys[pygame.K_DOWN]:
            dot_y += dot_speed

        dot_x = max(0, min(dot_x, width - dot_size))
        dot_y = max(0, min(dot_y, height - dot_size))

        for cube in cubes:
            cube[0] += cube[2]
            cube[1] += cube[3]

            if cube[0] <= 0 or cube[0] >= width - cube_size:
                cube[2] = -cube[2]
            if cube[1] <= 0 or cube[1] >= height - cube_size:
                cube[3] = -cube[3]

            if (dot_x < cube[0] + cube_size and
                dot_x + dot_size > cube[0] and
                dot_y < cube[1] + cube_size and
                dot_y + dot_size > cube[1]):
                game_over = True
                death_time = pygame.time.get_ticks()

        seconds = (pygame.time.get_ticks() - start_ticks) // 1000

        screen.fill(white)

        pygame.draw.rect(screen, black, (dot_x, dot_y, dot_size, dot_size))

        for cube in cubes:
            pygame.draw.rect(screen, cube[4], (cube[0], cube[1], cube_size, cube_size))

        timer_text = font.render(f"Time: {seconds} s", True, black)
        screen.blit(timer_text, (10, 10))
    else:
        draw_restart_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            dot_x, dot_y = width // 2, height // 2
            start_ticks = pygame.time.get_ticks()
            game_over = False
            extreme_mode = False
            cubes = []
            for _ in range(num_cubes):
                cube_x = random.randint(0, width - cube_size)
                cube_y = random.randint(0, height - cube_size)
                cube_speed_x = random.choice([-cube_speed, cube_speed])
                cube_speed_y = random.choice([-cube_speed, cube_speed])
                cube_color = random.choice(cube_colors)
                cubes.append([cube_x, cube_y, cube_speed_x, cube_speed_y, cube_color])
        elif keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
        elif keys[pygame.K_e]:  # Extreme mode
            dot_x, dot_y = width // 2, height // 2
            start_ticks = pygame.time.get_ticks()
            game_over = False
            extreme_mode = True
            cubes = []
            for _ in range(num_cubes):
                cube_x = random.randint(0, width - cube_size)
                cube_y = random.randint(0, height - cube_size)
                cube_speed_x = random.choice([-cube_speed, cube_speed])
                cube_speed_y = random.choice([-cube_speed, cube_speed])
                cube_color = black
                cubes.append([cube_x, cube_y, cube_speed_x, cube_speed_y, cube_color])

    pygame.display.flip()

    pygame.time.Clock().tick(30)









