import math

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
