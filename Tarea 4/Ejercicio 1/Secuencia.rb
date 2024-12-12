class Secuencia
  def agregar(elemento)
    raise NotImplementedError, 'Este es un metodo abstracto. Debe ser implementado por una subclase'
  end

  def remover
    raise NotImplementedError, 'Este es un metodo abstracto. Debe ser implementado por una subclase'
  end

  def vacio?
    raise NotImplementedError, 'Este es un metodo abstracto. Debe ser implementado por una subclase'
  end
end

class Pila < Secuencia
  def initialize
    @elementos = []
  end

  def agregar(elemento)
    @elementos.push(elemento)
  end

  def remover
    raise 'La pila está vaciaa' if vacio?
    @elementos.pop
  end

  def vacio?
    @elementos.empty?
  end
end

class Cola < Secuencia
  def initialize
    @elementos = []
  end

  def agregar(elemento)
    @elementos.push(elemento)
  end

  def remover
    raise 'La cola está vacia' if vacio?
    @elementos.shift
  end

  def vacio?
    @elementos.empty?
  end
end