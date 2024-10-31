from tileObj import *
import numpy as np

class Piece:
  
  def __init__(self, numTiles, pos):
    self.numTiles = numTiles
    self.pos = list(pos)
    self.tile = self.createTiles()
  
  def createTiles(self):
    tiles = []
    
    tilePos = []
    tilePos.extend(self.pos)
    
    tilePos[1] += self.pos[1] * .5
    if self.pos[1] == 1:
      tiles.append(Tile('top', (205/255, 205/255, 205/255), tilePos))
    elif self.pos[1] == -1:
      tiles.append(Tile('bottom', (225/255, 225/255, 50/255), tilePos))
    tilePos[1] -= self.pos[1] * .5
    
    tilePos[0] += self.pos[0] * .5
    if self.pos[0] == 1:
      tiles.append(Tile('right', (225/255, 40/255, 40/255), tilePos))
    elif self.pos[0] == -1:
      tiles.append(Tile('left', (245/255, 160/255, 40/255), tilePos))
    tilePos[0] -= self.pos[0] * .5
    
    tilePos[2] += self.pos[2] * .5
    if self.pos[2] == 1:
      tiles.append(Tile('front', (20/255, 225/255, 60/255), tilePos))
    elif self.pos[2] == -1:
      tiles.append(Tile('back', (10/255, 80/255, 205/255), tilePos))
    tilePos[2] -= self.pos[2] * .5
    
    return tiles
  
  def yTurn(self, theta):
    xOrig = self.pos[0]
    zOrig = self.pos[2]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    x = xOrig * cosVal + zOrig * sinVal
    z = xOrig * -sinVal + zOrig * cosVal
    
    self.pos[0] = x
    self.pos[2] = z
    
    for t in self.tile:
      t.yTurn(theta)
  
  def xTurn(self, theta):
    yOrig = self.pos[1]
    zOrig = self.pos[2]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    y = yOrig * cosVal + zOrig * -sinVal
    z = yOrig * sinVal + zOrig * cosVal
    
    self.pos[1] = y
    self.pos[2] = z
    
    for t in self.tile:
      t.xTurn(theta)
  
  def zTurn(self, theta):
    xOrig = self.pos[0]
    yOrig = self.pos[1]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    x = xOrig * cosVal + yOrig * -sinVal
    y = xOrig * sinVal + yOrig * cosVal
    
    self.pos[0] = x
    self.pos[1] = y
    
    for t in self.tile:
      t.zTurn(theta)
  