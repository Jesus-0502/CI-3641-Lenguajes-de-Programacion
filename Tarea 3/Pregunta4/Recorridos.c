// CI-3641 Lenguajes de Programación
// Alumno: Jesus Gutierrez
// Carnet: 20-10332
// Pregunta 4. Recorridos


#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <signal.h>
#include <setjmp.h>

jmp_buf env; 

void manejadorSegfault(int sig) {
    
    longjmp(env, 1);
}
void manejarError() {
    
    longjmp(env, 1);
}

void recorrerFilaColumna(int filas, int columnas, int **matriz) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            matriz[i][j];
        }
    }
}

void recorrerColumnaFila(int filas, int columnas, int **matriz) {
    for (int j = 0; j < columnas; j++) {
        for (int i = 0; i < filas; i++) {
            matriz[i][j];
        }
    }
}

int main() {
    
    signal(SIGSEGV, manejadorSegfault);

    FILE *file = fopen("resultados.csv", "w");
    if (file == NULL) {
        perror("Error al abrir el archivo");
        return 1;
    }

    
    fprintf(file, "Promedio FilaColumna,Promedio ColumnaFila\n");

    int tiempos[] = {100, 1000, 10000, 100000, 1000000};
    // float arregloTiempoF[16] = {0};
    // float arregloTiempoC[16] = {0};
    float promedio1;
    float promedio2;
    int s = 0;
    clock_t inicio1, inicio2, fin1, fin2;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int N = tiempos[i];
            int M = tiempos[j];
           
            if (setjmp(env) == 0) { 
                printf("%d", setjmp(env));
                
                printf("--------------------\n");
                printf("Matriz de %d x %d\n", N, M);


                int **matriz = (int **)malloc(N * sizeof(int *));
                if (matriz == NULL) {
                    perror("Error al asignar memoria");
                    manejarError();
                    continue; 
                }

                

                for (int k = 0; k < N; k++) {
                    matriz[k] = (int *)malloc(M * sizeof(int));
                    if (matriz[k] == NULL) {
                        perror("Error al asignar memoria");
                        
                        manejarError();
                        continue; 
                    }
                }

                for (int k = 0; k < 3; k++) {
                    printf("-Intento %d\n", k + 1);
                    // Recorrido Fila Columna
                    inicio1 = clock();
                    recorrerFilaColumna(N, M, matriz);
                    fin1 = clock();
                    double tiempo1 = (float)(fin1 - inicio1) / CLOCKS_PER_SEC;
                    promedio1 += tiempo1;
                    printf("--> Tiempo FilaColumna: %f\n", tiempo1);

                    // Recorrido Columna Fila
                    inicio2 = clock();
                    recorrerColumnaFila(N, M, matriz);
                    fin2 = clock();
                    double tiempo2 = (float)(fin2 - inicio2) / CLOCKS_PER_SEC;
                    promedio2 += tiempo2;
                    printf("--> Tiempo ColumnaFila: %f\n", tiempo2);
                }

                promedio1 /= 3;
                promedio2 /= 3;
                // arregloTiempoF[s] = promedio1;
                // arregloTiempoC[s] = promedio2;
                printf("Promedio FilaColumna: %f\n", promedio1);
                printf("Promedio ColumnaFila: %f\n", promedio2);

                fprintf(file, "%f,%f\n", promedio1, promedio2);
                
                for (int k = 0; k < N; k++) {
                    free(matriz[k]);
                }
                free(matriz);
                s++;
            } else {
                // fallo de segmentación
                printf("Saltando a la siguiente iteración debido a un fallo de segmentación.\n");
                s++;
            }
        }
    }
    fclose(file);
    return 0;
}