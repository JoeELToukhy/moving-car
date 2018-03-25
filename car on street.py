from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,
              0,0,0,
              0,1,0)
    glClearColor(0,0,0,1)

def street():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glScale(2,0.3,0.3)
    glutSolidCube(1.5)
    glPopAttrib()
    glPopMatrix()
def sides(a,b,c):
    glLoadIdentity()
    glColor(1,1,c)
    glTranslate(a,0,b)
    street()

    glLoadIdentity()
    glColor(1,1,c)
    glTranslate(a,0,b)
    street()

def strips(a1):
    glLoadIdentity()
    glColor(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(a1+3,0,1)
    glVertex3d(a1,0,1)
    glVertex3d(a1,0,.1)
    glVertex3d(a1+3,0,.1)
    glEnd()
x1 = 0
x = 0
angle = 0
y = 0.15
y1 = 0.1

def draw():
    global x , y1 , x1
    global angle,y
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)

    a2 = -40
    for i in range(-50,100):
        strips(a2+x1)
        a2 += 5

    glColor3f(1,0,0)
    glLoadIdentity()
    glTranslate(x,0,0)
    glScale(1,0.2,0.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x,5*0.2,0)
    glScale(0.5,0.2,0.5)
    glutWireCube(5)

    glColor3f(0,0,1)
    glLoadIdentity()

    glTranslate(x+2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glLoadIdentity()
    glTranslate(x+2.5,-2.5*0.25,-2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glLoadIdentity()
    glTranslate(x-2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glLoadIdentity()
    glTranslate(x-2.5,-2.5*0.25,-2.5*0.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glColor3f(1,1,0)
    glLoadIdentity()
    glutWireSphere(5,1,1)



    color = 0
    for i in range(-50,100):
        sides(i+x1,-5,color)
        i += 3
        if color == 0:
            color = 1
        else:
            color = 0
    for i in range(-50,100):
        sides(i+x1,5,color)
        i += 3
        if color == 0:
            color = 1
        else:
            color = 0



    x += y
    x1 += y1
    angle -= y * 100

    if x > 8 or x < -30:
        y *= -1
    if x1 > 5.5 or x1 < -20:
        y1 *= -1

    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"moving car")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()
