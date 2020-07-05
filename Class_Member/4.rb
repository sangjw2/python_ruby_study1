class Cal
  attr_accessor :v1 # reader, writer
  attr_accessor :v2
  @@_history = []
  def initialize(v1,v2)
    @v1,@v2 = v1,v2
  end
  def Cal.history()
    for item in @@_history
      p item
    end
  end
  def add()
    result = @v1+@v2
    @@_history.push("#{@v1}+#{@v2}=#{result}")
    return result
  end
  def subtract()
    result = @v1-@v2
    @@_history.push("#{@v1}-#{@v2}=#{result}")
    return result
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
    result = @v1*@v2
    @@_history.push("#{@v1}*#{@v2}=#{result}")
    return result
  end
end

class Caldivide < Calmultiply
  def divide()
    result = @v1/@v2
    @@_history.push("#{@v1}/#{@v2}=#{result}")
    return result
  end
end
c1 = Calmultiply.new(10,10)
p c1.add()
p c1.multiply()
c2 = Caldivide.new(20,10)
p c2.add
p c2.multiply
p c2.divide
Cal.history()