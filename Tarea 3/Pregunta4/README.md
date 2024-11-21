### Aclaraciones:
- Para los experimentos se hicieron las pruebas hasta N, M = 10^5 ya que al tratar de ejecutar con N,M = 10^6, la ejecucion nunca terminaba a pesar de esperar
1h. A pesar de eso con los resultados obtenidos, se obtuvieron las conclusiones necesarias para responder las preguntas que se plantean.

- Para mejor visualizacion, los resultados se dividieron en 4 graficas.


### Respuestas a las preguntas planteadas:


- ¿Hay alguna diferencia en tiempo de ejecución entre las dos implementaciones propuestas?
    Los resultados obtenidos en el experimento muestran que el recorrido Columna-Fila (segundo programa) es mas rápido. 
    Esta diferencia es muy pequeña e incluso casi despreciable. Esto ocurre ya que en C, las matrices se almacenan en memoria en orden de fila mayor (row-major order).
    Cuando se accede a los elementos por columna, se salta entre filas, lo que puede causar más fallos de caché y, por lo tanto, ser menos eficiente.

- ¿La forma de la matriz tiene algún efecto sobre el tiempo de la ejecución?
    En los resultados obtenidos, se puede ver que las matrices donde N > M tardaban mas en recorrerse para cualquiera de los dos programas, a pesar de que el numero de "casillas" es el mismo. 
    Esto es porque se estan accediendo a un numero grande de filas lo cual cambia el coste en tiempo a diferencia de las columnas.

- ¿Los tiempos de ejecución cambian al ejecutar más de una vez la misma configuración?
    Si, a pesar que los resultados muestran el promedio de las 3 ejecuciones para cada Matriz NxM, cabe destacar que al momento de la ejecucion, se puede notar que los tiempos varian, a pesar que se recorre la misma matriz. Esta variacion es en la mayoria de los casos nula. 
    Esta variacion ocurre ya que hay diversos factores como declaraciones y almacenamiento en memoria que no son los mismos para todas las ejecuciones.

- ¿Afecta a los tiempos de ejecución si la matriz se declara de forma global (memoria estática) o local (pila)?
    Mas que los tiempos de ejecucion, al declarar la matriz estatica de forma local, para valores muy grandes de N o de M, la pila se desborda de forma inmediata y da un error de secuenciacion el cual no es captado por el manejador de excepciones en C. 
    Por ello para ese experimento no se puede concluir con los resultados obtenidos si una matriz declarada estaticamente afecta a los tiempos de ejecucion, ya que solo se podia hacer dichas pruebas para valores de N y M relativamente pequeños y 
    la diferencia en los tiempos no era notoria como para concluir.