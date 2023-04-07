#!/usr/bin/env python3
try:
    import pygame
    from pygame.locals import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    from os import system as sys
    print('\x1b[31m [!!!] VOCE NAO POSSUI ALGUMA DAS BIBLIOTECAS NECESSARIAS!')
    sys('pip3 install pygame && pip3 install pyOpenGL')
    exit(1)

#   CUBO EM SI
# Here, we've defined the location (x,y,z) of each vertex.

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)


edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,7),
    (6,4),
    (5,1),
    (5,4),
    (5,7)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,1),
    (0,0,0),
    (1,0,1),
    (0,1,1),
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

# ----------------------------------------------------------->
def Cube():
    glBegin(GL_QUADS)
    # for surface in surfaces:
    #     glColor3fv((0.4,0.7,0.9))
    #     x = 1
    #     for vertex in surface:
    #         x += 1
    #         glColor3fv(colors[x])
    #         glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv((0, 1, 0))  # 7C FC 00
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
# ----------------------------------------------------------->\

from time import sleep

def main():
    pygame.init()
    display = (1000,900)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(42, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, -2, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

#   FIGURAS MORES DAHORAS
# verticies = (
#     (-1, -1, -1),
#     (1, -1, -1),
#     (-1, 1, -1),
#     (1, -1, 1),
#     (1, 1, 1),
#     (-1, 1, 1),
#     (1, 1, -1),
#     (-1, -1, 1)
# )

# verticies = (
#     (1, -1, -1),
#     (1, -1, 1),
#     (-1, 1, -1),
#     (-1, 1, 1),
#     (1, 1, 1),
#     (-1, -1, -1),
#     (-1, -1, -1),
#     (-1, 1, 1),
#     (-1, 1, 1),
#     (-1, -1, 1),
#     (1, 1, -1),
#     (1, 1, -1)
# )