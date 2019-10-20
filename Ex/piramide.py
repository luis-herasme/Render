import pygame
import math


width = 400
aspc = 2
resolucion = 50 * aspc
tamanoPantalla = 6  / aspc

screen = pygame.display.set_mode((width, width))
pygame.display.flip()

# Vector
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def punto(self, otro):
        return otro.x * self.x + otro.y * self.y + otro.z * self.z
    def cruz(self, otro):
        return Vector(self.y*otro.z - self.z*otro.y, self.z*otro.x - self.x*otro.z, self.x*otro.y - self.y*otro.x)
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def sub(self, otro):
        return Vector(self.x-otro.x, self.y-otro.y, self.z-otro.z)
    def add(self, otro):
        return Vector(self.x+otro.x, self.y+otro.y, self.z+otro.z)
    def normalizar(self):
        mag = self.mag()
        self.x /= mag
        self.y /= mag
        self.z /= mag

# Matriz pantalla
size = width / resolucion
pantalla = []

for x in range(resolucion):
    for y in range(resolucion):
        pantalla.append(Vector(0, x * tamanoPantalla, y * tamanoPantalla))

#Objetos

'''
    Cuadro
    a = 50, 25, 50
    b = 50, 25, 25
    c = 50, 50, 50
    d = 50, 50, 25
'''

'''
    Piramide
    a = 50, 100, 100
    b = 50, 200, 150
    c = 50, 100, 200
    d = 100, 100, 150
'''

objetos = [
    [   #       a                      b                    c           d: Vector(200,75,50)
        Vector(50, 100, 100), Vector(50, 200, 150), Vector(50, 100, 200)
    ],
    [
        Vector(50, 100, 100), Vector(50, 200, 150), Vector(100, 100, 150)
    ],
    [
        Vector(50, 100, 100), Vector(100, 100, 150), Vector(50, 100, 200)
    ],
    [
        Vector(50, 200, 150), Vector(100, 100, 150), Vector(50, 100, 200)
    ]
]

colores = [
    [255, 0, 0],
    [0, 255, 0],
    [255, 0, 255],
    [0, 255, 255]
]

def rotarx(objeto, angulo, pivote):
    v1 = objeto[0].sub(pivote)
    v2 = objeto[1].sub(pivote)
    v3 = objeto[2].sub(pivote)
    
    rotx(v1, angulo)
    rotx(v2, angulo)
    rotx(v3, angulo)

    objeto[0] = pivote.add(v1)
    objeto[1] = pivote.add(v2)
    objeto[2] = pivote.add(v3)

def rotary(objeto, angulo, pivote):
    v1 = objeto[0].sub(pivote)
    v2 = objeto[1].sub(pivote)
    v3 = objeto[2].sub(pivote)
    
    roty(v1, angulo)
    roty(v2, angulo)
    roty(v3, angulo)

    objeto[0] = pivote.add(v1)
    objeto[1] = pivote.add(v2)
    objeto[2] = pivote.add(v3)

def rotarz(objeto, angulo, pivote):
    v1 = objeto[0].sub(pivote)
    v2 = objeto[1].sub(pivote)
    v3 = objeto[2].sub(pivote)
    
    rotz(v1, angulo)
    rotz(v2, angulo)
    rotz(v3, angulo)

    objeto[0] = pivote.add(v1)
    objeto[1] = pivote.add(v2)
    objeto[2] = pivote.add(v3)

def rotx(vec, angulo):
    vy = vec.y
    vz = vec.z
    vec.y = vy * math.cos(angulo) - vz * math.sin(angulo)
    vec.z = vy * math.sin(angulo) + vz * math.cos(angulo)

def roty(vec, angulo):
    vx = vec.x
    vz = vec.z
    vec.x = vx * math.cos(angulo) + vz * math.sin(angulo)
    vec.z = vz * math.cos(angulo) - vx * math.sin(angulo) 

def rotz(vec, angulo):
    vx = vec.x
    vy = vec.y
    vec.x = vx * math.cos(angulo) - vy * math.sin(angulo)
    vec.y = vx * math.sin(angulo) + vy * math.cos(angulo)

#Renderizado
tx = Vector(1, 0, 0)

def render(pantalla, objetos):
    renderizado = [0] * len(pantalla)
    profundidad = [0] * len(pantalla)

    for objeto in range(len(objetos)):
        normal = objetos[objeto][1].sub(objetos[objeto][0]).cruz(objetos[objeto][2].sub(objetos[objeto][0]))

        for i in range(len(pantalla)):
            oa = objetos[objeto][0].sub(pantalla[i])
            ob = objetos[objeto][1].sub(pantalla[i])
            oc = objetos[objeto][2].sub(pantalla[i])

            if (normal.x != 0):
                t = normal.punto(oa) / normal.x
                tx.x = t
                s1 = ob.sub(tx).cruz(oc.sub(tx))
                s2 = ob.sub(tx).cruz(oa.sub(tx))
                s3 = oc.sub(tx).cruz(oa.sub(tx))
                s = normal.mag()

                if (abs(s1.mag() + s2.mag() + s3.mag() - s) < 0.01):
                    if (profundidad[i] == 0 or t < profundidad[i]):
                        profundidad[i] = t
                        renderizado[i] = colores[objeto]

    return renderizado

ang = 0.1
alante = Vector(10, 0, 0)
lado = Vector(0, 10, 0)

screens = []
def getGrab():
    for i in range(100):
        for b in range(len(objetos)):
            rotary(objetos[b], ang,  Vector(50, 200, 150)) 
            rotarz(objetos[b], 0.05,  Vector(50, 200, 150))         
        screens.append(render(pantalla, objetos))

def draw(mtrx):
    p = 0
    k = 0
    for pixel in mtrx:
        if pixel:
            pygame.draw.rect(screen, pixel, (p * size, k * size, size, size))
        p += 1
        if (p == resolucion):
            p = 0
            k += 1    

def main():
    running = True
    while running:
        #rotary(objetos[0], ang * 2, Vector(50, 100, 100))    
        
        for b in range(len(objetos)):
            #rotarz(objetos[b], ang,  Vector(50, 300, 150))
            #rotarx(objetos[b], ang,  Vector(50, 300, 150))  
            rotary(objetos[b], ang,  Vector(50, 200, 150)) 
            rotarz(objetos[b], 0.05,  Vector(50, 200, 150)) 
        
        pygame.draw.rect(screen,(0,0,0),(0, 0, width, width))


        '''
        p = 0
        k = 0
        for pixel in render(pantalla, objetos):
        #for pixel in render(pantalla, [objetos[0], objetos[1]]):
            if pixel:
                #print("PIXEL: ", pixel[0], " ", pixel[1], " ", pixel[2])
                pygame.draw.rect(screen, pixel, (p * size, k * size, size, size))
            p += 1
            if (p == resolucion):
                p = 0
                k += 1
        '''
        draw(render(pantalla, objetos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    for f in range(len(pantalla)):
                        pantalla[f] = pantalla[f].sub(alante)
                if event.key == pygame.K_s:
                    for f in range(len(pantalla)):
                        pantalla[f] = pantalla[f].add(alante)
                if event.key == pygame.K_d:
                    for f in range(len(pantalla)):
                        pantalla[f] = pantalla[f].add(lado)
                        
                if event.key == pygame.K_a:
                    for f in range(len(pantalla)):
                        pantalla[f] = pantalla[f].sub(lado)
                if event.key == pygame.K_e:
                    for b in range(len(objetos)):
                        rotarx(objetos[b], ang,  Vector(50, 300, 150)) 
                    

        pygame.display.update()
main()