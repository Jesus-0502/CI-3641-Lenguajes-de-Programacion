/*
 * CI-3641 Lenguajes de Programación
 * Alumno: Jesus Gutierrez
 * Carnet: 20-10332
 * Prgeunta 4
 * Pruebas de la libreria Cuaternion
 */

#include "Cuaternion.cpp"
using namespace std;

int main() {
    Cuaternion v(1, 1, 1, 1);
    Cuaternion w(2, 2, 2, 2);
    cout << "La suma de v+w es: ";
    (v+w).mostrar();
    cout << "La suma de v+3 es: ";
    (v+3).mostrar();
    
    cout << "El producto de v*w es: ";
    (v*w).mostrar();
    cout << "El producto de w*3 es: ";
    (w*3).mostrar();
    
    cout << "El inverso de v es: ";
    (~v).mostrar();
    
    cout << "El modulo del cuaternion v es: " << (&v) << endl;
    return 0;
}

