// CI-3641 Lenguajes de Programación
// Alumno: Jesus Gutierrez
// Carnet: 20-10332
// Pregunta 1: Inciso 1

package main

import "fmt"

// Funcion count:
// 		Calcula el número de pasos necesarios para reducir un número entero n a 1
// 		siguiendo las reglas del problema de la conjetura de Collatz.
// 		La función devuelve el número de pasos realizados.
//
// Parámetros:
// 		- n: un número entero positivo.
//
// Retorna:
// 		- Un entero que representa el número de pasos necesarios para reducir n a 1.
func count(n int) int {
	contador := 0
	for n != 1 {
		if n % 2 == 0 {
			n = n / 2
			contador++
		} else {
			n = 3 * n + 1
			contador++
		}
	}
	return contador
}

func main() {
	n := 42
	result := count(n)
	fmt.Println("Contador:", result)
}