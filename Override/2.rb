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
  def info
    return "Cal => v1 : #{@v1}, v2 : #{@v2}"
  end
end

class Calmultiply < Cal
  def multiply()
    result = @v1*@v2
    @@_history.push("#{@v1}*#{@v2}=#{result}")
    return result
  end
  def info
    return "Calmultiply => #{super()}"
  end
end

class Caldivide < Calmultiply
  def divide()
    result = @v1/@v2
    @@_history.push("#{@v1}/#{@v2}=#{result}")
    return result
  end
  def info
    return "Caldivide => #{super()}"
  end
end
c0 = Cal.new(30,60)
p c0.info
c1 = Calmultiply.new(10,10)
p c1.info
c2 = Caldivide.new(20,10)
p c2.info