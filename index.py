import pygame
import math
import Rotar
from Renderizador import render, draw
from Vector import Vector
import Gen

width = 400
scale = 8
resolucion = 50 * scale
tamanoPixel = 6  / scale
size = width / resolucion
pantalla = []

for x in range(resolucion):
    for y in range(resolucion):
        pantalla.append(Vector(0, x * tamanoPixel, y * tamanoPixel))

#Objetos
objetos = [
    [ Vector(50, 100, 100), Vector(50, 200, 150), Vector(50, 100, 200) ],
    [ Vector(50, 100, 100), Vector(50, 200, 150), Vector(100, 100, 150) ],
    [ Vector(50, 100, 100), Vector(100, 100, 150), Vector(50, 100, 200) ],
    [ Vector(50, 200, 150), Vector(100, 100, 150), Vector(50, 100, 200) ]
]

def main():
    running = True
    screen = pygame.display.set_mode((width, width))
    pygame.display.flip()
    
    #grabacion = Gen.getGrab(objetos, pantalla, 10)
    grabacion = Gen.screensAndSave(objetos, pantalla, 50)
    #print("Pantalla size: ", len(pantalla))
    #print("Cal:", len(pantalla) * 3 * 50)
    #grabacion = Gen.read(len(pantalla))
    
    
    #Gen.reproduce(grabacion, screen, resolucion, size, pygame, 0.5)
    while running:
        Gen.reproduce(grabacion, screen, resolucion, size, pygame, 0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
   
    '''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.draw.rect(screen, (25, 25, 25), (0, 0, width, width))
        for b in range(len(objetos)):
            Rotar.rotary(objetos[b], 0.1,  Vector(50, 200, 150)) 
            Rotar.rotarz(objetos[b], 0.05,  Vector(50, 200, 150)) 
        draw(render(pantalla, objetos), screen, resolucion, size, pygame)
        pygame.display.update()
    '''
    
main()
