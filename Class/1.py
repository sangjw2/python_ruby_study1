class Cal(object):
  def __init__(self, v1, v2): #self는 변수 이름. 다른 것도 가능
    self.v1 = v1
    self.v2 = v2
  def add(self):
    return self.v1+self.v2
  def subtract(self):
    return self.v1-self.v2

c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())