import Rotar
from Vector import Vector
from Renderizador import render, draw
import time

def read(pantallaSize):
    f = open("data.txt", "r")
    content = f.read()
    print(content)
    content = content.split(',')
    del content[0]
    print("content: ", len(content))
    fotogramas = round((len(content) / 3) / pantallaSize)
    print("fotogramas: ", fotogramas)
    screens = []
    for e in range(fotogramas):
        screen = []
        foto = e * pantallaSize
        for i in range(pantallaSize):
            screen.append([int(content[ foto + (i*3)]), int(content[foto + (i*3) + 1]), int(content[foto + (i*3) + 2])])
        screens.append(screen)
    return screens
        
def screensAndSave(objetos, pantalla, fotogramas):
    screens = []
    screens = getGrab(objetos, pantalla, fotogramas)

    f = open("data.txt", "w")
    for screen in screens:
        for pixel in screen:
            if (pixel == 0):
                f.write(", 0, 0, 0")
            else:
                f.write(f", {pixel[0]}, {pixel[1]}, {pixel[2]}")
    f.close()
    return screens

def getGrab(objetos, pantalla, fotogramas):
    screens = []
    for i in range(fotogramas):
        for ojb in objetos:
            Rotar.rotary(ojb, 0.1,  Vector(50, 200, 150)) 
            Rotar.rotarz(ojb, 0.05,  Vector(50, 200, 150))         
        screens.append(render(pantalla, objetos))
        print((i/fotogramas)*100,"%")
    return screens

def reproduce(screens, screen, resolucion, size, pygame, speed):
    for i in screens:
        pygame.draw.rect(screen, (25, 25, 25), (0, 0, 400, 400)) # Limpia (ERROR: 400 es de la pantalla)
        time.sleep(speed)
        draw(i, screen, resolucion, size, pygame)
        pygame.display.update()