import pygame
import numpy as np
import shapes_siy as ss

pygame.init()

resolution = (1280,720)
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()
for (v_1, v_2, v_3) in ss.sierpinski_triangles(np.array([0, 0]), resolution[1], resolution[0], 10):
    pygame.draw.line(screen, (255, 255, 255), v_1, v_2, 1)
    pygame.draw.line(screen, (255, 255, 255), v_2, v_3, 1)
    pygame.draw.line(screen, (255, 255, 255), v_3, v_1, 1)

# ss.sierpinski_triangles_draw(screen, np.array([0, 0]), resolution[1], resolution[0], 13)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
