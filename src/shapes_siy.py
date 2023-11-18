import pygame
import numpy as np
from itertools import chain

def sierpinski_triangles_arr(origin: np.ndarray, height, width, depth):
    if depth < 2:
        return [(origin + np.array([width / 2, 0]), origin + np.array([0, height]), origin + np.array([width, height]))]
    else:
        
        return sierpinski_triangles_arr(origin + np.array([width / 4, 0]), height / 2, width / 2, depth - 1) + sierpinski_triangles_arr(origin + np.array([0, height / 2]), height / 2, width / 2, depth - 1) + sierpinski_triangles_arr(origin + np.array([width / 2, height /2]), height / 2, width / 2, depth - 1)

        
def sierpinski_triangles_draw(SCREEN, origin: np.ndarray, height, width, depth):
    def st(origin: np.ndarray, height, width, depth):
        if depth < 2:
            v_1, v_2, v_3 = (origin + np.array([width / 2, 0]), origin + np.array([0, height]), origin + np.array([width, height]))
            pygame.draw.line(SCREEN, (255, 255, 255), v_1, v_2, 1)
            pygame.draw.line(SCREEN, (255, 255, 255), v_2, v_3, 1)
            pygame.draw.line(SCREEN, (255, 255, 255), v_3, v_1, 1)
        else:
            st(origin + np.array([width / 4, 0]), height / 2, width / 2, depth - 1)
            st(origin + np.array([0, height / 2]), height / 2, width / 2, depth - 1)
            st(origin + np.array([width / 2, height /2]), height / 2, width / 2, depth - 1)
            
    st(origin, height, width, depth)
def sierpinski_triangles(origin: np.ndarray, height, width, depth):
    if depth < 2:
        return [(origin + np.array([width / 2, 0]), origin + np.array([0, height]), origin + np.array([width, height]))]
    else:
        return chain(sierpinski_triangles(origin + np.array([width / 4, 0]), height / 2, width / 2, depth - 1),
                     sierpinski_triangles(origin + np.array([0, height / 2]), height / 2, width / 2, depth - 1),
                     sierpinski_triangles(origin + np.array([width / 2, height /2]), height / 2, width / 2, depth - 1))

# WIP
def sierpinski_triangles_iter(origin: np.ndarray, height, width, depth):
    while False:
        pass
    
    
