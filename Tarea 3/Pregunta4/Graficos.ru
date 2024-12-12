# CI-3641 Lenguajes de Programación
# Alumno: Jesus Gutierrez
# Carnet: 20-10332
# Pregunta 4. Generacion de Graficas


require 'gruff'
require 'csv'

def crear_grafico(titulo, datos_columna_1, datos_columna_2, etiquetas, nombre_archivo)
  g = Gruff::Bar.new
  g.title = titulo

  g.data('Recorrido Fila-Columna', datos_columna_1)
  g.data('Recorrido Columna-Fila', datos_columna_2)

  g.labels = etiquetas
  g.write(nombre_archivo)
end

columna_1 = []
columna_2 = []
tamaños = ["10^2", "10^3", "10^4", "10^5"]

CSV.foreach('resultados.csv', headers: true) do |row|
  columna_1 << row[0].to_f  
  columna_2 << row[1].to_f  
end

4.times do |i|
  inicio = i * 4
  fin = inicio + 4

  etiquetas = {}
  index = 0
  tamaños.each do |t1|
    break if index >= 4
    etiquetas[index] = "M = #{t1}"
    index += 1
  end

  crear_grafico(
    "Gráfico de Tiempos Recorridos (N = #{tamaños[i]})",
    columna_1[inicio, 4],
    columna_2[inicio, 4],
    etiquetas,
    "tiempos_ejecucion_#{i + 1}.png"
  )
end