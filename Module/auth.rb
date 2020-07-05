module Auth
  module_function()
  def login(id)
    members = ['egoing', 'k8805']
    for member in members do
      if member == id
        return true
      end
    end
    return false
  end
end