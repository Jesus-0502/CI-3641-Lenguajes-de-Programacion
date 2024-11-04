// CI-3641 Lenguajes de Programación
// Alumno: Jesus Gutierrez
// Carnet: 20-10332
// Pregunta 1: Inciso 2, implementar el algoritmo de ordenamiento Merge Sort.


package main

import "fmt"

// Funcion MergeSort: 
//      ordena un arreglo de números flotantes utilizando el algoritmo de ordenación Merge Sort.
//
// Parámetros:
//      - arr: []float64 - El arreglo de números a ordenar.
//
// Retorna:
//      - []float64 - Un nuevo arreglo con los elementos ordenados.
func MergeSort(arr []float64) []float64 {
    if len(arr) <= 1 {
        return arr
    }

    mid := len(arr) / 2
    left := MergeSort(arr[:mid])
    right := MergeSort(arr[mid:])

    return merge(left, right)
}


// Funcion auxiliar merge:
//      toma dos subarreglos de float64 ordenados, left y right, y los combina en un solo arreglo ordenado.
//      Devuelve un nuevo slice que contiene todos los elementos de left y right en orden ascendente.
//
// Parámetros:
//      - left: subarreglo de float64 ordenado.
//      - right: subarreglo de float64 ordenado.
//
// Retorno:
//      - Un nuevo arreglo de float64 que contiene todos los elementos de left y right en orden ascendente.
func merge(left, right []float64) []float64 {
    result := make([]float64, 0, len(left)+len(right))
    i, j := 0, 0

    for i < len(left) && j < len(right) {
        if left[i] < right[j] {
            result = append(result, left[i])
            i++
        } else {
            result = append(result, right[j])
            j++
        }
    }

    result = append(result, left[i:]...)
    result = append(result, right[j:]...)

    return result
}

func main() {
    arr := []float64{38, 27, 43, 3, 9, 82, 10.1}
    fmt.Println("Original array:", arr)
    sortedArr := MergeSort(arr)
    fmt.Println("Sorted array:", sortedArr)
}