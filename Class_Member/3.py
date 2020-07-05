class Cs:
  count = 0 # 초기화
  def __init__(self):
    Cs.count += 1
  @classmethod
  def getCount(cls):
    print(cls)
    return Cs.count# = cls.count (cls = Cs)

i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
print(Cs.getCount())