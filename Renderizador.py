from Vector import Vector

tx = Vector(1, 0, 0)
colores = [
    [255, 0, 0],
    [0, 255, 0],
    [255, 0, 255],
    [0, 255, 255]
]

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

def draw(mtrx, screen, resolucion, size, pygame):
    for y in range(resolucion):
        for x in range(resolucion):
            if (mtrx[x + y * resolucion]):
                pygame.draw.rect(screen, mtrx[x + y * resolucion], (x * size, y * size, size, size))

#old sin threads
'''

empty = [0] * 10000
renderizado = []
profundidad = []


normales = []
oa=0
ob=0
oc=0
def inicializar(pantalla, objetos):
    for objeto in range(len(objetos)):
            normal = objetos[objeto][1].sub(objetos[objeto][0]).cruz(objetos[objeto][2].sub(objetos[objeto][0]))
            normales.append(normal.mag())

def render(pantalla, objetos):
    renderizado = empty.copy()
    profundidad = empty.copy()

    for objeto in range(len(objetos)):
        normal = objetos[objeto][1].sub(objetos[objeto][0]).cruz(objetos[objeto][2].sub(objetos[objeto][0]))

        for i in range(len(pantalla)):
            oa = objetos[objeto][0].sub(pantalla[i])
            ob = objetos[objeto][1].sub(pantalla[i])
            oc = objetos[objeto][2].sub(pantalla[i])

            if (normal.x != 0):
                t = normal.punto(oa) / normal.x
                tx.x = t
                if ((ob.sub(tx).cruzMag(oc.sub(tx)) + ob.sub(tx).cruzMag(oa.sub(tx)) + oc.sub(tx).cruzMag(oa.sub(tx)) - normales[objeto]) < 0.01):
                    if (profundidad[i] == 0 or t < profundidad[i]):
                        profundidad[i] = t
                        renderizado[i] = colores[objeto]
    return renderizado
'''