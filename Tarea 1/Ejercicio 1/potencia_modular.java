public class potencia_modular {

    /**
     * Calcula la potencia modular (a^b) % c.
     *
     * @param a El número base, debe ser no negativo.
     * @param b El exponente, debe ser no negativo.
     * @param c El módulo, debe ser mayor o igual a 2.
     * @return El resultado de (a^b) % c.
     * @throws IllegalArgumentException Si alguno de los parámetros no cumple con las condiciones especificadas.
     */
    public static long calculateModularExpression(long a, long b, long c) {
        if(a < 0 || b < 0 || c < 2){
            throw new IllegalArgumentException("Por favor, ingrese los datos de forma correcta.");
        }

        if(b != 0){
            long aModC = a % c;
            long aPowBMinus1ModC = modularExponentiation(a, b - 1, c);
            return (aModC * aPowBMinus1ModC) % c;  
        }

        return 1;
    }

    /**
     * Calcula la potencia modular de una base elevada a un exponente bajo un módulo dado.
     * 
     * @param base La base que se va a elevar.
     * @param exp El exponente al que se va a elevar la base.
     * @param mod El módulo bajo el cual se realizará la operación.
     * @return El resultado de (base^exp) % mod.
     * 
     * Este método utiliza el algoritmo de exponenciación binaria para calcular la potencia modular 
     * de manera eficiente.
     */
    public static long modularExponentiation(long base, long exp, long mod) {
        long result = 1;
        base = base % mod; 
        while (exp > 0) {
            if ((exp % 2) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp /=  2;
        }
        return result;
    }
}