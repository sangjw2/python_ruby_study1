class Cs
  def Cs.class_method() #앞에 Class명을 붙여 클래스 메소드임을 명시
    p "Class method"
  end
  def instance_method() # 아무것도 없으면 인스턴스 메소드
    p "instance method"
  end
end
i = Cs.new()
Cs.class_method()
i.instance_method()