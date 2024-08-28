import matplotlib.pyplot as plt

# Leer los tiempos del primer archivo (algoritmo clásico)
with open('tiempoClasica.txt', 'r') as file1:
    line1 = file1.readline().strip()
    tiempos_clasico = [float(time) for time in line1.split(',')]

# Leer los tiempos del segundo archivo (algoritmo por bloques)
with open('tiempoBloques.txt', 'r') as file2:
    line2 = file2.readline().strip()
    tiempos_bloques = [float(time) for time in line2.split(',')]

# Tamaños de matriz correspondientes
tamaños = [100, 500, 1000, 2000]

# Graficar ambos conjuntos de datos
plt.plot(tamaños, tiempos_clasico, marker='o', color='blue', label='Algoritmo Clásico')
plt.plot(tamaños, tiempos_bloques, marker='o', color='red', label='Algoritmo por Bloques')

# Configurar la gráfica
plt.title('Comparación de Tiempos de Ejecución')
plt.xlabel('Tamaño de Matriz')
plt.ylabel('Tiempo de Ejecución (ms)')
plt.grid(True)
plt.legend()  # Añadir leyenda para distinguir entre las dos líneas

# Mostrar la gráfica
plt.show()