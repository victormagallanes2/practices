#include <vector>
#include <iostream>
using namespace std;

int main() {
  // Crear una lista vacía
  std::vector<int> lista;

  // Agregar elementos a la lista
  lista.push_back(1);
  lista.push_back(2);
  lista.push_back(3);

  // Obtener el primer elemento de la lista
  int primer_elemento = lista[0];

  // Obtener el segundo elemento de la lista
  int segundo_elemento = lista[1];

  // Obtener el tercer elemento de la lista
  int tercer_elemento = lista[2];

  // Imprimir los elementos de la lista
  std::cout << "El primer elemento es " << primer_elemento << std::endl;
  std::cout << "El segundo elemento es " << segundo_elemento << std::endl;
  std::cout << "El tercer elemento es " << tercer_elemento << std::endl;
  // nota: para imprimir la lista completa no es posible hacerlo directamente
  // asi cout << lista;, para esto se debe recorrer con un ciclo for
  return 0;
}