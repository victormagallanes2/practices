#include <iostream>
//using namespace std;

int main() 
{
    std::map<std::string, int> diccionario {
        {"uno", 1},
        {"dos", 2}
    };

    cout << diccionario;
    cout << diccionario["uno"];
    return 0;
}