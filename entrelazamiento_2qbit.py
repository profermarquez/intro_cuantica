
"""
El código crea y visualiza un estado cuántico entrelazado de dos qubits usando Qiskit.

Usa el primer qubit como control y el segundo qubit como objetivo.
Si el qubit de control está en 
∣0⟩, no hace nada. Pero si está en ∣1⟩, invierte el segundo qubit.
"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere, plot_state_city
import matplotlib.pyplot as plt

# Crear un circuito cuántico de 2 qubits
qc = QuantumCircuit(2)
qc.h(0)            # Hadamard en el primer qubit
qc.cx(0, 1)        # CNOT con el primer qubit como control

# Obtener el vector de estado resultante
state = Statevector.from_instruction(qc)

# Mostrar el circuito
print(qc.draw())

# Visualizar el estado entrelazado en la Q-Sphere con tamaño ajustado
plot_state_qsphere(state, figsize=(6, 6))
plt.title("Estado entrelazado en la Q-Sphere")
plt.show()

# Visualizar la matriz de densidad con plot_state_city y tamaño ajustado
plot_state_city(state, figsize=(6, 6))
plt.title("Matriz de densidad del estado entrelazado")
plt.show()
