Inicialización de un arreglo
```cpp
#include <iostream>
using namespace std;

int main(){
    int calificaciones[5]={10, 5, 8, 9, 8};

    cout << calificaciones[0] << "\n";
    cout << calificaciones[1] << "\n";
    cout << calificaciones[2] << "\n";
    cout << calificaciones[3] << "\n";
    cout << calificaciones[4] << "\n";

    return 0;
}
```

```cpp
#include <iostream>
using namespace std;

int main(){
    int calificaciones[5]={10, 5, 8, 9, 8};

    for(int i = 0; i < 5; i++){
        cout << calificaciones[i] << "\n";
    }

    return 0;
}
```
```cpp
#include <iostream>
using namespace std;

int main(){
    int calificaciones[5]={0};

    for(int i = 0; i < 5; i++){
        cout << "Introduzca calificación " << (i+1) << ": ";
        cin >> calificaciones[i];
    }
    
    for(int i = 0; i < 5; i++){
        cout << calificaciones[i] << ": ";
    }

    return 0;
}
```
```cpp
#include <iostream>
using namespace std;

int main(){
    int calificaciones[3][3]={0};

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << "Introduzca calificación " << (i+1) << "," << (j+1) << " : ";
            cin >> calificaciones[i][j];
        }
    }
    
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << calificaciones[i][j] << ": ";
        }
        cout << "\n";        
    }

    return 0;
}
```