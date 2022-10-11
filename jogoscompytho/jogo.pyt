import pygame
from pygame.locals import *
from OpenGL.GL import *

branco = (250,250,250)
altura = 480
largura = 640

xDaBola = 0
yDaBola = 0
tamanhoBola = 20
velocidadeBolaX = 0.2
velocidadeBolaY = 0.2

yjogador1 = 0
yjogador2 = 0

def xjogador1():
    return -largura /2 + largurajogadores() / 2 


def xjogador2():
    return largura /2 - largurajogadores() / 2


def largurajogadores():
    return tamanhoBola


def alturajogadores():
    return 3 * tamanhoBola


def atualizar():
    global xDaBola, yDaBola, velocidadeBolaX, velocidadeBolaY, yjogador1, yjogador2

    xDaBola = xDaBola + velocidadeBolaX
    yDaBola = yDaBola + velocidadeBolaY

    if (xDaBola + tamanhoBola / 2 > xjogador2() - largurajogadores() / 2
    and yDaBola - tamanhoBola / 2 < yjogador2 + alturajogadores() / 2
    and yDaBola + tamanhoBola / 2 > yjogador2 - alturajogadores() / 2):
        velocidadeBolaX = -velocidadeBolaX

    if (xDaBola - tamanhoBola / 2 < xjogador1() + largurajogadores() / 2
    and yDaBola - tamanhoBola / 2 < yjogador1 + alturajogadores() / 2
    and yDaBola + tamanhoBola / 2 > yjogador1 - alturajogadores() / 2):
        velocidadeBolaX = -velocidadeBolaX

    if yDaBola + tamanhoBola / 2 > altura/ 2:
        velocidadeBolaY = -velocidadeBolaY

    if yDaBola - tamanhoBola / 2 < -largura / 2:
        velocidadeBolaY = -velocidadeBolaY

    if xDaBola < -largura / 2 or xDaBola > largura/ 2:
        xDaBola = 0
        yDaBola = 0

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        yjogador1 = yjogador1 + 2

    if keys[K_s]:
        yjogador1 = yjogador1 - 2

    if keys[K_UP]:
        yjogador2 = yjogador2 + 2

    if keys[K_DOWN]:
        yjogador2 = yjogador2 - 2
    
def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor(r, g,b)
    
    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():
    glViewport(0, 0, largura, altura)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-largura / 2, largura /2, -altura / 2, altura / 2, 0, 1)
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    desenharRetangulo(xDaBola, yDaBola, tamanhoBola, tamanhoBola, 1, 1, 0)
    desenharRetangulo(xjogador1(), yjogador1, largurajogadores(), alturajogadores(), 1, 0, 0)
    desenharRetangulo(xjogador2(), yjogador2, largurajogadores(), alturajogadores(), 0, 0, 1)
    
    pygame.display.flip()
    
    

pygame.init()
janela = pygame.display.set_mode((largura,altura), DOUBLEBUF | OPENGL)
pygame.display.set_caption("ping pong")

fim = False
while not fim:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True
    atualizar()
    desenhar()
    pygame.event.pump()
