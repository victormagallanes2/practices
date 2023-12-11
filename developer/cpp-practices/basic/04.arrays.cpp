#include <iostream>
using namespace std;

int main() 
{
    // Los arrays en c++ deben declararse especificando el numero de items que contendra
    // si no se especifica automaticamente tomara el tamaño e items que se le asigne inicialmente
    string lista[3] = {"Hola Mundo", "otra cosa"};
    // Nota: No es posible en c++ crear arrays de diferentes tipos de datos
    // A cada item de la lista o array se le asigna un valor, comenzando desde 0
    // con esto podemos seleccionar el valor de la lista que queramos
    cout << lista[1] << endl;
    // Tambien podemos reescribir el valor de una lista ubicandolo por su posicion
    lista[0] = "Hola universo";
    cout << lista[0] << endl;
    return 0;
}