from qutip import Bloch, tensor, basis# tensor: producto tensorial y basis: base de un espacio de Hilbert
import numpy as np
import matplotlib.pyplot as plt

b = Bloch()
punto = [1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3)] # Coordenadas del punto

b.add_points(punto)
b.render()  # Renderiza el gráfico
#plt.show()  # Muestra la ventana emergente

# dibujar un vector en la esfera de Bloch
# Vector a graficar (x, y, z)
vector = [1/np.sqrt(2), 1/np.sqrt(2), 0] # Coordenadas del vector

# Agregar el vector a la esfera
b.add_vectors(vector)

# Renderizar y mostrar
b.render()
#plt.show()

#representar un tensor en la esfera de Bloch

# Estado base |0> y |1>
zero = basis(2, 0)
one = basis(2, 1)
# en la Esfera de Bloch solo permite visualizar estados de un qubit. 
# Los tensores (estados de múltiples qubits) no se pueden representar 
# directamente en una sola esfera, ya que estos viven en un espacio de Hilbert de mayor dimensión.
# Crear un estado de dos qubits |ψ> = (|0> + |1>) ⊗ |0>
psi = tensor((zero + one).unit(), zero)

# Obtener las matrices de densidad parciales
rho1 = psi.ptrace(0)  # Primer qubit
rho2 = psi.ptrace(1)  # Segundo qubit

# Visualizar cada qubit en su propia Esfera de Bloch
b1 = Bloch()
b2 = Bloch()

b1.add_states(rho1)
b2.add_states(rho2)

b1.render()
plt.show()

b2.render()
plt.show()