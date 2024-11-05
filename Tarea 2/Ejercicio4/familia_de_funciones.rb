# CI-3641 Lenguajes de Programación
# Alumno: Jesus Gutierrez
# Carnet: 20-10332
# Pregunta 4
# X = 3, Y = 3, Z = 2

require 'gruff'
require 'benchmark'

# Recursiva
def fun_rec(n)
    if n >= 0 && n < 12
        return n
    else
        return fun_rec(n - 3) + fun_rec(n - 6) + fun_rec(n - 9) + fun_rec(n - 12)
    end
end


# Iterativa
def fun_iter(n)

    return n if n < 12 && n >= 0
    
    results = [0] * (n + 1)
    (0...12).each do |i|
        results[i] = i
    end

    (12..n).each do |i|
        results[i] = results[i - 3] + results[i - 6] + results[i - 9] + results[i - 12]
    end

    return results[n]
end

# Recursiva de cola
def fun_rec_cola(n)

  if n >= 0 && n < 12
    return n
  end

  def recursion_aux(n, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11)
    if n < 12
      return f11
    end

    recursion_aux(n - 1, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f0 + f3 + f6 + f9)
  end

  recursion_aux(n, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
end

# Funcion principal para generar los tiempos de ejecución
def main()
  valores = [10, 20, 30, 40, 50]
  resultados = []

  valores.each do |valor|
    tiempo_iterativo = Benchmark.realtime { fun_iter(valor) }
    tiempo_recursivo = Benchmark.realtime { fun_rec(valor) }
    tiempo_recursivo_cola = Benchmark.realtime { fun_rec_cola(valor) }

    resultados << [valor, tiempo_iterativo, tiempo_recursivo, tiempo_recursivo_cola]
  end

 generar_grafico(resultados)
end

# Funcion para generar el grafico
def generar_grafico(resultados)
  g = Gruff::Bar.new
  g.title = 'Tiempos de Ejecución'

  valores = resultados.map { |r| r[0] }
  tiempos_iterativos = resultados.map { |r| r[1] }
  tiempos_recursivos = resultados.map { |r| r[2] }
  tiempos_recursivos_cola = resultados.map { |r| r[3] }

  g.labels = valores.each_with_index.map { |valor, index| [index, valor.to_s] }.to_h
  g.data(:Iterativo, tiempos_iterativos)
  g.data(:Recursivo, tiempos_recursivos)
  g.data(:Recursivo_Cola, tiempos_recursivos_cola)

  g.write('tiempos_ejecucion.png')
end


main()