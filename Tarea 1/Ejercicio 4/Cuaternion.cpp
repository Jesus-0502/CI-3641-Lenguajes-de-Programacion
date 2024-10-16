#include <iostream>
#include <cmath>
using namespace std;

/**
 * @class Cuaternion
 * @brief Representa un cuaternión y proporciona operaciones básicas sobre cuaterniones.
 * 
 * La clase Cuaternion permite la creación y manipulación de cuaterniones, incluyendo
 * operaciones como suma, producto, inverso y cálculo del módulo.
 * 
 * @var float a
 *      Parte real del cuaternión.
 * @var float b
 *      Componente i del cuaternión.
 * @var float c
 *      Componente j del cuaternión.
 * @var float d
 *      Componente k del cuaternión.
 */

class Cuaternion {
private:
    float a, b, c, d;

public:
    
    /**
     * @brief Constructor de la clase Cuaternion.
     * 
     * Este constructor inicializa un cuaternión con los valores proporcionados.
     * 
     * @param a Componente escalar del cuaternión.
     * @param b Componente i del cuaternión.
     * @param c Componente j del cuaternión.
     * @param d Componente k del cuaternión.
     */
    Cuaternion(float a, float b, float c, float d) {
        this->a = a;
        this->b = b;
        this->c = c;
        this->d = d;
    }
     
    /**
     * @brief Sobrecarga del operador de suma para cuaterniones.
     * 
     * Esta función permite sumar dos cuaterniones componente a componente.
     * 
     * @param v El cuaternión que se va a sumar al cuaternión actual.
     * @return Cuaternion +> El resultado de la suma de los dos cuaterniones.
     */
    Cuaternion operator+(const Cuaternion& v) const {
        return Cuaternion(a + v.a, b + v.b, c + v.c, d + v.d);
    }

    /**
     * @brief Sobrecarga del operador + para sumar un escalar a un cuaternión.
     * 
     * @param escalar Valor escalar que se sumará al componente 'a' del cuaternión.
     * @return Cuaternion +> Resultado de la suma del escalar con el cuaternión original.
     */
    Cuaternion operator+(float escalar) const {
        return Cuaternion(a + escalar, b, c, d);
    }
    
    // Operador de inverso
    /**
     * @brief Operador de conjugación para el cuaternión.
     *
     * Este operador devuelve el conjugado del cuaternión actual. 
     *
     * @return Cuaternion => El cuaternión conjugado.
     */
    Cuaternion operator~() const {
        return Cuaternion(a, -b, -c, -d);
    }
    
    
    /**
     * @brief Sobrecarga del operador de multiplicación para cuaterniones.
     * 
     * Este operador realiza la multiplicación de dos cuaterniones y devuelve el resultado como un nuevo cuaternión.
     * 
     * @param v El cuaternión con el cual se multiplicará el cuaternión actual.
     * @return Cuaternion El resultado de la multiplicación de los dos cuaterniones.
     */
    Cuaternion operator*(const Cuaternion & v) const {
       float x = a * v.a - b * v.b - c * v.c - d * v.d;
       float y = a * v.b + b * v.a + c * v.d - d * v.c;
       float z = a * v.c - b * v.d + c * v.a + d * v.b;
       float w = a * v.d + b * v.c - c * v.b + d * v.a;
       return Cuaternion(x, y, z, w);
    }
    
    // Operador producto entre cuaternion y escalar
    /**
     * @brief Sobrecarga del operador de multiplicación (*) para un Cuaternion.
     * 
     * Este operador permite multiplicar un cuaternión por un escalar.
     * 
     * @param escalar El valor escalar por el cual se multiplicará el cuaternión.
     * @return Cuaternion El resultado de la multiplicación del cuaternión por el escalar.
     */
     Cuaternion operator*(float escalar) const {
        return Cuaternion(a * escalar, b, c, d);
     }
     
    /**
     * @brief Sobrecarga del operador & para calcular la magnitud del cuaternión.
     * 
     * Esta función calcula y devuelve la magnitud (norma) del cuaternión utilizando
     * la fórmula de la raíz cuadrada de la suma de los cuadrados de sus componentes.
     * 
     * @return La magnitud del cuaternión.
     */
    float operator&() const {
        return std::sqrt(a * a + b * b + c * c + d * d);
    }
    
    void mostrar() const {
        cout << a << " + (" << b << ")i + (" << c <<")j + (" << d << ")k\n";
    }
};

int main() {
    Cuaternion v(1, 1, 1, 1);
    Cuaternion w(2, 2, 2, 2);
    //cout << "La suma de v+w es: ";
    //(v+w).mostrar();
    //cout << "La suma de v+3 es: ";
    //(v+3).mostrar();
    
    //cout << "El producto de v*w es: ";
    //(v*w).mostrar();
    //cout << "El producto de w*3 es: ";
    //(w*3).mostrar();
    
    //cout << "El inverso de v es: ";
    //(~v).mostrar();*/
    
    cout << "El módulo del cuaternion v es: " << (&v) << endl;
    return 0;
}