class Calmultiply(): #Cal의 모든 메소드 상속받음
  def multiply(self):
    return self.v1*self.v2

class Caldivide():
  def divide(self):
    return self.v1/self.v2

class Cal(Calmultiply,Caldivide):
  def __init__(self, v1, v2): #self는 변수 이름. 다른 것도 가능
    if isinstance(v1, int):
      self.v1 = v1
    if isinstance(v2, int):
      self.v2 = v2
  def add(self):
    return self.v1+self.v2
  def subtract(self):
    return self.v1-self.v2
  def setV1(self, v):
    if isinstance(v, int):
      self.v1 = v
  def getV1(self):
    return self.v1

c = Cal(100,10)
print(c.add())
print(c.multiply())
print(c.divide())

