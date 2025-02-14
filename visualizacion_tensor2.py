from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere
import matplotlib.pyplot as plt

# Crear un circuito cuántico para un estado entrelazado (tensor de 2 qubits)
qc = QuantumCircuit(2)
qc.h(0)            # Puerta Hadamard en el primer qubit
qc.cx(0, 1)        # Puerta CNOT con el primer qubit como control y el segundo como objetivo

# Obtener el estado resultante como vector de estado
state = Statevector.from_instruction(qc)

# Visualizar el tensor usando plot_state_qsphere
plot_state_qsphere(state)
plt.show()
