class Grafo
  def initialize
    @adjacency_list = {}
  end

  def agregar_nodo(nodo)
    @adjacency_list[nodo] = []
  end

  def agregar_arista(nodo1, nodo2)
    @adjacency_list[nodo1] << nodo2
    @adjacency_list[nodo2] << nodo1
  end

  def remover_nodo(nodo)
    @adjacency_list.each do |k, v|
      v.delete(nodo)
    end
    @adjacency_list.delete(nodo)
  end

  def remover_arista(nodo1, nodo2)
    @adjacency_list[nodo1].delete(nodo2)
    @adjacency_list[nodo2].delete(nodo1)
  end

  def vacio?
    @adjacency_list.empty?
  end
end

class Busqueda
  def buscar(d, h)
    raise NotImplementedError, 'Este es un metodo abstracto. Debe ser implementado por una subclase'
  end

  protected

  def explorar_nodos(inicial, objetivo)
    raise NotImplementedError, 'Este es un metodo abstracto. Debe ser implementado por una subclase'
  end
end

class DFS < Busqueda
  def buscar(d, h)
    explorar_nodos(d, h) { |stack| stack.pop }
  end

  protected

  def explorar_nodos(inicial, objetivo)
    stack = [inicial]
    visitados = {}
    explorados = 0

    until stack.empty?
      nodo = yield(stack)
      next if visitados[nodo]

      visitados[nodo] = true
      explorados += 1
      return explorados if nodo == objetivo

      @adjacency_list[nodo].each { |vecino| stack.push(vecino) }
    end

    -1
  end
end

class BFS < Busqueda
  def buscar(d, h)
    explorar_nodos(d, h) { |queue| queue.shift }
  end

  protected

  def explorar_nodos(inicial, objetivo)
    queue = [inicial]
    visitados = {}
    explorados = 0

    until queue.empty?
      nodo = yield(queue)
      next if visitados[nodo]

      visitados[nodo] = true
      explorados += 1
      return explorados if nodo == objetivo

      @adjacency_list[nodo].each { |vecino| queue.push(vecino) }
    end

    -1
  end
end

grafo = Grafo.new
grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)
grafo.agregar_nodo(4)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(3, 4)

# Prueba de BFS
bfs = BFS.new
bfs.instance_variable_set(:@adjacency_list, grafo.instance_variable_get(:@adjacency_list))
nodos_explorados_bfs = bfs.buscar(1, 4)
puts "Nodos explorados con BFS: #{nodos_explorados_bfs}" # 4

# Prueba de DFS
dfs = DFS.new
dfs.instance_variable_set(:@adjacency_list, grafo.instance_variable_get(:@adjacency_list))
nodos_explorados_dfs = dfs.buscar(1, 4)
puts "Nodos explorados con DFS: #{nodos_explorados_dfs}" # 3