class Cal(object):
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

class Calmultiply(Cal): #Cal의 모든 메소드 상속받음
  def multiply(self):
    return self.v1*self.v2

class Caldivide(Calmultiply):
  def divide(self):
    return self.v1/self.v2

c1 = Calmultiply(10,10)
# print(c1.add())
# print(c1.subtract())
# c1.setV1('one')
# print(c1.getV1())
# print(c1.add())
# c2 = Cal(30,20)
# print(c2.add())
# print(c2.subtract())
# print('c1 value:',c1.v1)
print(c1.add())
print(c1.multiply())

c2 = Caldivide(20,10)
print(c2.multiply())
print(c2.divide())