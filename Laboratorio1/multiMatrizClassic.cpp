#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Función para multiplicar dos matrices
void multiplicacionClasica(const vector<vector<int>>& A, const vector<vector<int>>& B, vector<vector<int>>& C, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int N = 2000;  // Tamaño de la matriz (N x N)

    // Inicializar matrices A y B con valores aleatorios
    vector<vector<int>> A(N, vector<int>(N, 1));  // Matriz N x N llena de 1
    vector<vector<int>> B(N, vector<int>(N, 2));  // Matriz N x N llena de 2
    vector<vector<int>> C(N, vector<int>(N, 0));  // Matriz resultado N x N inicializada en 0

    auto start = high_resolution_clock::now();
    multiplicacionClasica(A, B, C, N);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "Tiempo de ejecución para la multiplicación de matrices de tamaño " << N << "x" << N << ": " 
        << double(duration.count()) / 1000000.0 << " ms" << endl;

    return 0;
}
