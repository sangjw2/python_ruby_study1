class Cal
  attr_accessor :v1 # reader, writer
  attr_accessor :v2
  def initialize(v1,v2)
    @v1,@v2 = v1,v2
  end

  def add()
    return @v1+@v2
  end
  
  def subtract()
    return @v1-@v2
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def getV1()
    return @v1
  end
end

class Calmultiply < Cal
  def multiply()
    return @v1*@v2
  end
end

class Caldivide < Calmultiply
  def divide()
    return @v1/@v2
  end
end
c1 = Calmultiply.new(10,10)
p c1.v1
p c1.add()
p c1.subtract()
c1.setV1('one')
p c1.add()
p c1.getV1()
p c1.multiply()
c2 = Caldivide.new(20,10)
p c2.add
p c2.divide