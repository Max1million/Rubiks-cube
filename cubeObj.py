from pieceObj import *

class Cube:
  
  def __init__(self):
    self.centerPiece = []
    self.edgePiece = []
    self.cornerPiece = []
    
    centerPos = [(0, 1, 0), (0, 0, -1), (1, 0, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0)]
    for pos in centerPos:
      self.centerPiece.append(Piece(1, pos))
    
    edgePos = [(0, 1, -1), (1, 1, 0), (0, 1, 1), (-1, 1, 0),
    (-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1),
    (0, -1, -1), (1, -1, 0), (0, -1, 1), (-1, -1, 0)]
    for pos in edgePos:
      self.edgePiece.append(Piece(2, pos))
    
    cornerPos = [(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1),
                 (-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)]
    for pos in cornerPos:
      self.cornerPiece.append(Piece(3, pos))
    
    self.piece = self.centerPiece + self.edgePiece + self.cornerPiece
  
  def roundPos(self):
    for p in self.piece:
      for i in range(3):
        p.pos[i] = round(p.pos[i])
  
  def rotY(self, theta):
    for p in self.piece:
      p.yTurn(theta)
  
  def rotX(self, theta):
    for p in self.piece:
      p.xTurn(theta)
  
  def turnT(self, theta):
    for p in self.piece:
      if p.pos[1] == 1:
        p.yTurn(theta)
  
  def turnR(self, theta):
    for p in self.piece:
      if p.pos[0] == 1:
        p.xTurn(theta)
  
  def turnL(self, theta):
    for p in self.piece:
      if p.pos[0] == -1:
        p.xTurn(theta)
  
  def turnF(self, theta):
    for p in self.piece:
      if p.pos[2] == 1:
        p.zTurn(theta)
  
  def turnD(self, theta):
    for p in self.piece:
      if p.pos[1] == -1:
        p.yTurn(theta)
  
  def turnB(self, theta):
    for p in self.piece:
      if p.pos[2] == -1:
        p.zTurn(theta)
  
  def turnM(self, theta):
    for p in self.piece:
      if p.pos[0] == 0:
        p.xTurn(theta)
  
  def turnWR(self, theta):
    for p in self.piece:
      if p.pos[0] == 1 or p.pos[0] == 0:
        p.xTurn(theta)
  
  def turnWL(self, theta):
    for p in self.piece:
      if p.pos[0] == -1 or p.pos[0] == 0:
        p.xTurn(theta)
