import numpy as np

class Tile:
  
  def __init__(self, face, color, pos):
    self.face = face
    self.pos = pos
    self.color = color
    self.corner = []
    
    if face == 'top' or face == 'bottom':
      cornerPos = [(-.4, -.4), (.4, -.4), (.4, .4), (-.4, .4)]
      for i in cornerPos:
        self.corner.append((self.pos[0] + i[0], self.pos[1], self.pos[2] + i[1]))
    
    if face == 'right' or face == 'left':
      cornerPos = [(-.4, -.4), (.4, -.4), (.4, .4), (-.4, .4)]
      for i in cornerPos:
        self.corner.append((self.pos[0], self.pos[1] + i[0], self.pos[2] + i[1]))
    
    if face == 'front' or face == 'back':
      cornerPos = [(-.4, -.4), (.4, -.4), (.4, .4), (-.4, .4)]
      for i in cornerPos:
        self.corner.append((self.pos[0] + i[0], self.pos[1] + i[1], self.pos[2]))
    
    self.xRot = 0
    self.yRot = 0
    self.zRot = 0
  
  def yTurn(self, theta):
    self.yRot = self.yRot + theta
    #print(self.yRot)
    
    xOrig = self.pos[0]
    zOrig = self.pos[2]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    x = xOrig * cosVal + zOrig * sinVal
    z = xOrig * -sinVal + zOrig * cosVal
    
    self.pos[0] = x
    self.pos[2] = z
    
    for i in range(4):
      self.corner[i] = self.yRotCorner(self.corner[i], theta)
    
    if self.yRot < -np.pi/4:
      self.changeFaceY()
      self.yRot = np.pi/2 + self.yRot
    
    if self.yRot > np.pi/4:
      self.changeFaceY()
      self.yRot = -np.pi/2 + self.yRot
  
  def yRotCorner(self, pos, theta):
    xOrig = pos[0]
    zOrig = pos[2]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    x = xOrig * cosVal + zOrig * sinVal
    z = xOrig * -sinVal + zOrig * cosVal
    
    return (x, pos[1], z)
  
  def changeFaceY(self):
    if self.face == 'front':
      if self.yRot > 0:
        self.face = 'right'
      else:
        self.face = 'left'
    
    elif self.face == 'left':
      if self.yRot > 0:
        self.face = 'front'
      else:
        self.face = 'back'
    
    elif self.face == 'back':
      if self.yRot > 0:
        self.face = 'left'
      else:
        self.face = 'right'
    
    elif self.face == 'right':
      if self.yRot > 0:
        self.face = 'back'
      else:
        self.face = 'front'
  
  def xTurn(self, theta):
    self.xRot = self.xRot + theta
    
    yOrig = self.pos[1]
    zOrig = self.pos[2]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    y = yOrig * cosVal + zOrig * -sinVal
    z = yOrig * sinVal + zOrig * cosVal
    
    self.pos[1] = y
    self.pos[2] = z
    
    for i in range(4):
      self.corner[i] = self.xRotCorner(self.corner[i], theta)
    
    if self.xRot < -np.pi/4:
      self.changeFaceX()
      self.xRot = np.pi/2 + self.xRot
    
    if self.xRot > np.pi/4:
      self.changeFaceX()
      self.xRot = -np.pi/2 + self.xRot
  
  def xRotCorner(self, pos, theta):
    yOrig = pos[1]
    zOrig = pos[2]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    y = yOrig * cosVal + zOrig * -sinVal
    z = yOrig * sinVal + zOrig * cosVal
    
    return (pos[0], y, z)

  def changeFaceX(self):
    if self.face == 'top':
      if self.xRot > 0:
        self.face = 'front'
      else:
        self.face = 'back'
    
    elif self.face == 'back':
      if self.xRot > 0:
        self.face = 'top'
      else:
        self.face = 'bottom'
    
    elif self.face == 'bottom':
      if self.xRot > 0:
        self.face = 'back'
      else:
        self.face = 'front'
    
    elif self.face == 'front':
      if self.xRot > 0:
        self.face = 'bottom'
      else:
        self.face = 'top'
  
  def zTurn(self, theta):
    self.zRot = self.zRot + theta
    
    xOrig = self.pos[0]
    yOrig = self.pos[1]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    x = xOrig * cosVal + yOrig * -sinVal
    y = xOrig * sinVal + yOrig * cosVal
    
    self.pos[0] = x
    self.pos[1] = y
    
    for i in range(4):
      self.corner[i] = self.zRotCorner(self.corner[i], theta)
    
    if self.zRot < -np.pi/4:
      self.changeFaceZ()
      self.zRot = np.pi/2 + self.zRot
    
    if self.zRot > np.pi/4:
      self.changeFaceZ()
      self.zRot = -np.pi/2 + self.zRot
  
  def zRotCorner(self, pos, theta):
    xOrig = pos[0]
    yOrig = pos[1]
    
    cosVal = np.cos(theta)
    sinVal = np.sin(theta)
    
    x = xOrig * cosVal + yOrig * -sinVal
    y = xOrig * sinVal + yOrig * cosVal
    
    return (x, y, pos[2])

  def changeFaceZ(self):
    if self.face == 'top':
      if self.zRot > 0:
        self.face = 'left'
      else:
        self.face = 'right'
    
    elif self.face == 'left':
      if self.zRot > 0:
        self.face = 'bottom'
      else:
        self.face = 'top'
    
    elif self.face == 'bottom':
      if self.zRot > 0:
        self.face = 'right'
      else:
        self.face = 'left'
    
    elif self.face == 'right':
      if self.zRot > 0:
        self.face = 'top'
      else:
        self.face = 'bottom'
