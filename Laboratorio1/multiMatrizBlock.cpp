#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

void multiplicacionBloques(const vector<vector<int>>& A, const vector<vector<int>>& B, vector<vector<int>>& C, int N, int blockSize) {
    for (int i = 0; i < N; i += blockSize) {
        for (int j = 0; j < N; j += blockSize) {
            for (int k = 0; k < N; k += blockSize) {
                for (int ii = i; ii < min(i + blockSize, N); ii++) {
                    for (int jj = j; jj < min(j + blockSize, N); jj++) {
                        for (int kk = k; kk < min(k + blockSize, N); kk++) {
                            C[ii][jj] += A[ii][kk] * B[kk][jj];
                        }
                    }
                }
            }
        }
    }
}

int main() {
    int N = 2000;  // Tamaño de la matriz (N x N)
    int blockSize = 50;  // Tamaño del bloque

    // Inicializar matrices A y B con valores aleatorios
    vector<vector<int>> A(N, vector<int>(N, 1));  // Matriz N x N llena de 1
    vector<vector<int>> B(N, vector<int>(N, 2));  // Matriz N x N llena de 2
    vector<vector<int>> C(N, vector<int>(N, 0));  // Matriz resultado N x N inicializada en 0

    // Medir el tiempo de ejecución
    auto start = high_resolution_clock::now();
    multiplicacionBloques(A, B, C, N, blockSize);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<nanoseconds>(stop - start);

    cout << "Tiempo de ejecución para la multiplicación de matrices de tamaño " << N << "x" << N << ": " 
        << double(duration.count()) / 1000000.0 << " ms" << endl;

    return 0;
}