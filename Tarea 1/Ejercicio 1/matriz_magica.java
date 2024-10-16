


public class matriz_magica {
       
    /**
     * Verifica si una matriz cuadrada es una matriz mágica.
     * Una matriz mágica es aquella en la que la suma de cada fila, 
     * cada columna y las dos diagonales principales son iguales.
     *
     * @param matriz La matriz cuadrada a verificar.
     * @return true si la matriz es mágica, false en caso contrario.
     * @throws IllegalArgumentException si la matriz no es cuadrada.
     */
    public static boolean esMagica(int[][] matriz) {
        if(matriz.length != matriz[0].length) {
            throw new IllegalArgumentException("La matriz no es cuadrada");
        }
        int suma_cols[] =  new int[matriz.length];
        int suma_filas = 0;
        int suma_diag1 = 0;
        int suma_diag2 = 0;
        for (int i = 0; i < matriz.length; i++) {
            suma_diag1 += matriz[i][i];
            suma_diag2 += matriz[i][matriz.length - 1 - i];
            for (int j = 0; j < matriz.length; j++) {
                
                suma_filas += matriz[i][j]; 
                suma_cols[i] += matriz[j][i];
            }
        
            if (suma_filas != suma_cols[i]) {
                return false;
            }

            suma_filas = 0;
        }
       
        
        return !(suma_diag1 != suma_diag2 || suma_diag1 != suma_cols[0]);
    }
}