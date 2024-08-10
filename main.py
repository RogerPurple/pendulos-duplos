import pygame
from objets import Simple_Pendulum
from utils import Vector

pygame.init()

screen_width = 1280 
screen_heith = 720
screen_center = Vector(screen_width/2, screen_heith/2)
screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

# 1 = simple; 2 extended
mode = 2

# inicializando classe
frodo = Simple_Pendulum(screen_center, 300, True)



def logical_update():
    frodo.update()

def render_graphics():
    frodo.render_graphs(screen)


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    logical_update()
    # ...

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    render_graphics()
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)