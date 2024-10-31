import turtle as t
import random as r
import time
import numpy as np
from cubeObj import *
from pieceObj import *
from tileObj import *

turnSpeed = 20
theta = (np.pi/2) / (160//turnSpeed)

wn = t.Screen()
wn.setup(500,500)
wn.bgcolor(0, 0, 0)
wn.tracer(0,0)

draw = t.Turtle()
draw.ht()
draw.pu()
draw.speed(0)
draw.color(1, 1, 1)
#draw.pensize(3)
draw.pd()

def proj(pos):
  x3d = pos[0]
  y3d = pos[1]
  z3d = pos[2]
  
  y3d = y3d/(2**.5) - z3d/(2**.5)
  z3d = y3d/(2**.5) + z3d/(2**.5)
  
  x = (x3d*2.5)/(-z3d+5)
  y = (y3d*2.5)/(-z3d+5)
  return((x*170, y*170 - 18))

cube = Cube()

def drawCube():
  draw.clear()
  
  for face in ['back', 'bottom', 'left', 'right', 'top', 'front']:
    for piece in cube.piece:
      for tile in piece.tile:
        if tile.face != face:
          continue
        
        draw.color(tile.color)
        draw.pencolor(0, 0, 0)
        
        draw.goto(proj(tile.corner[3]))
        draw.begin_fill()
        draw.pd()
        for corner in tile.corner:
          draw.goto(proj(corner))
        draw.end_fill()
        draw.pu()
      
  wn.update()

drawCube()

que = []
  
def topC():
  que.append(-1)
def topCC():
  que.append(1)

def rightC():
  que.append(-2)
def rightCC():
  que.append(2)

def leftC():
  que.append(3)
def leftCC():
  que.append(-3)

def frontC():
  que.append(-4)
def frontCC():
  que.append(4)

def bottomC():
  que.append(5)
def bottomCC():
  que.append(-5)

def backC():
  que.append(6)
def backCC():
  que.append(-6)

def mC():
  que.append(-7)
def mCC():
  que.append(7)

def wideRC():
  que.append(-8)
def wideRCC():
  que.append(8)

def wideLC():
  que.append(9)
def wideLCC():
  que.append(-9)
  
def rotC():
  que.append(-10)
def rotCC():
  que.append(10)

def rotF():
  que.append(11)
def rotB():
  que.append(-11)


wn.listen()
wn.onkey(rotC, 'p')
wn.onkey(backC, 'w')
wn.onkey(bottomC, 's')
wn.onkey(leftCC, 'e')
wn.onkey(leftC, 'd')
wn.onkey(topCC, 'f')
wn.onkey(frontCC, 'g')

wn.onkey(rotB, 't')
wn.onkey(rotB, 'y')
wn.onkey(rotF, 'b')

wn.onkey(frontC, 'h')

wn.onkey(topC, 'j')

wn.onkey(rightC, 'i')
wn.onkey(rightCC, 'k')
wn.onkey(bottomCC, 'l')
wn.onkey(backCC, 'o')

wn.onkey(rotCC, 'a')
wn.onkey(rotCC, 'q')

wn.onkey(mC, 'x')
wn.onkey(mCC, '6')

wn.onkey(wideRC, 'u')
wn.onkey(wideRCC, 'm')
wn.onkey(wideLCC, 'r')
wn.onkey(wideLC, 'v')

def makeMove(move):
  if abs(move) == 1:
    turnT(abs(move)//move)
  elif abs(move) == 2:
    turnR(abs(move)//move)
  elif abs(move) == 3:
    turnL(abs(move)//move)
  elif abs(move) == 4:
    turnF(abs(move)//move)
  elif abs(move) == 5:
    turnD(abs(move)//move)
  elif abs(move) == 6:
    turnB(abs(move)//move)
  elif abs(move) == 7:
    turnM(abs(move)//move)
  elif abs(move) == 8:
    turnWR(abs(move)//move)
  elif abs(move) == 9:
    turnWL(abs(move)//move)
  elif abs(move) == 10:
    rotY(abs(move)//move)
  elif abs(move) == 11:
    rotX(abs(move)//move)
  elif abs(move) == 12:
    drawCube()

def turnT(direc):
  for i in range(160//turnSpeed):
    cube.turnT(direc * theta)
    drawCube()
  cube.roundPos()

def turnR(direc):
  for i in range(160//turnSpeed):
    cube.turnR(direc * theta)
    drawCube()
  cube.roundPos()

def turnL(direc):
  for i in range(160//turnSpeed):
    cube.turnL(direc * theta)
    drawCube()
  cube.roundPos()

def turnF(direc):
  for i in range(160//turnSpeed):
    cube.turnF(direc * theta)
    drawCube()
  cube.roundPos()

def turnD(direc):
  for i in range(160//turnSpeed):
    cube.turnD(direc * theta)
    drawCube()
  cube.roundPos()

def turnB(direc):
  for i in range(160//turnSpeed):
    cube.turnB(direc * theta)
    drawCube()
  cube.roundPos()

def turnM(direc):
  for i in range(160//turnSpeed):
    cube.turnM(direc * theta)
    drawCube()
  cube.roundPos()

def turnWR(direc):
  for i in range(160//turnSpeed):
    cube.turnWR(direc * theta)
    drawCube()
  cube.roundPos()

def turnWL(direc):
  for i in range(160//turnSpeed):
    cube.turnWL(direc * theta)
    drawCube()
  cube.roundPos()

def rotY(direc):
  for i in range(160//turnSpeed):
    cube.rotY(direc * theta)
    drawCube()
  cube.roundPos()

def rotX(direc):
  for i in range(160//turnSpeed):
    cube.rotX(direc * theta)
    drawCube()
  cube.roundPos()

def scramble():
  global turnSpeed
  global theta
  
  theta = (np.pi/2) / (160//turnSpeed)
  
  for i in range(30):
    que.append(r.randint(0, 11) * r.choice([-1, 1]))

wn.onkey(scramble, 'space')

def exit():
  t.bye()

wn.onkey(exit, '0')

while True:
  if len(que) != 0:

    makeMove(que[0])
    que.pop(0)

  else:
    drawCube()