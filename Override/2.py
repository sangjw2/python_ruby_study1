class Cal(object):
  _history = []
  def __init__(self, v1, v2): #self는 변수 이름. 다른 것도 가능
    if isinstance(v1, int):
      self.v1 = v1
    if isinstance(v2, int):
      self.v2 = v2
  def add(self):
    result = self.v1+self.v2
    Cal._history.append(f"{self.v1}+{self.v2}={result}")
    return result
  def subtract(self):
    result = self.v1-self.v2
    Cal._history.append(f"{self.v1}-{self.v2}={result}")
    return result
  def setV1(self, v):
    if isinstance(v, int):
      self.v1 = v
  def getV1(self):
    return self.v1
  @classmethod
  def history(cls):
    for i in Cal._history:
      print(i)
  def info(self):
    return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)
class Calmultiply(Cal): #Cal의 모든 메소드 상속받음
  def multiply(self):
    result = self.v1*self.v2
    Cal._history.append(f"{self.v1}*{self.v2}={result}")
    return result
  def info(self):
    return f"CalMultiply => {super().info()}"
class Caldivide(Calmultiply):
  def divide(self):
    result = self.v1/self.v2
    Cal._history.append(f"{self.v1}/{self.v2}={result}")
    return result
  def info(self):
    return f"Caldivide => {super().info()}"
c0 = Cal(30,60)
print(c0.info())
c1 = Calmultiply(10,10)
print(c1.info())
c2 = Caldivide(20,10)
print(c2.info())