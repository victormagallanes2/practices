#include <iostream>
using namespace std;

int main() 
{
    int edad;
    std::cout << "¿Cuál es tu edad? ";
    std::cin >> edad;
    if (edad >=18 and edad <= 40)
    {
        cout << "Estas joven" << endl;
    }
    else if (edad > 0 and edad < 18)
    {
	    cout << "eres menor de edad" << endl;
    }
    else
    {
	    cout << "estas pasado" << endl;
    }
    return 0;
}