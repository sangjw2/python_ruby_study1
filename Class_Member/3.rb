class Cs
  @@count = 0 # 변수 초기화 
  def initialize() 
    @@count += 1   # @ = instance변수, @@ = Class변수
  end
  def Cs.getCount()
    return @@count
  end
end

i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()
i4 = Cs.new()
p Cs.getCount() # Output = 4