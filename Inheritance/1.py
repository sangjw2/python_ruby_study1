class Class1(object):
  def method1(self):
    return 'm1'

c1 = Class1()
print(c1,c1.method1())

class Class3(Class1): #Class1을 상속
  def method2(self):
    return 'm2'

c3 = Class3()

print(c3.method1())
print(c3.method2())