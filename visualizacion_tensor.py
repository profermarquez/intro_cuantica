"""
Lo que estás viendo en esa imagen es la representación gráfica de un tensor cuántico 
mediante su matriz de densidad, visualizada con plot_state_hinton de Qiskit.

Explicación de la imagen:
Panel Izquierdo (Re[ρ]): Muestra la parte real de la matriz de densidad del estado.

Panel Derecho (Im[ρ]): Muestra la parte imaginaria (que en este caso es toda cero, 
lo que es común para ciertos estados como los de Bell).

Celdas blancas y grises:

Las celdas blancas representan valores positivos.
Las celdas grises representan valores negativos.
El tamaño de cada celda es proporcional al valor absoluto del elemento correspondiente 
en la matriz de densidad.

"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_hinton
import matplotlib.pyplot as plt

# Crear un circuito cuántico de 2 qubits
qc = QuantumCircuit(2)

# Aplicar una puerta Hadamard al primer qubit
qc.h(0)

# Aplicar una puerta CNOT con el primer qubit como control y el segundo como objetivo
qc.cx(0, 1)

# Obtener el estado resultante como un vector de estado
state = Statevector.from_instruction(qc)

# Visualizar el tensor usando plot_state_hinton
plot_state_hinton(state)
plt.show()