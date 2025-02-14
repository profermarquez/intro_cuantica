"""
La Esfera de Bloch solo puede representar estados de un solo qubit.
 Por lo tanto, solo puedes visualizar directamente las puertas 
 cuánticas de un qubit en la Esfera de Bloch.
 Lo que puedes visualizar en la Esfera de Bloch:
 
    Todas las puertas de un qubit, como:
    Puerta X (Rotación en el eje X, similar a una NOT clásica).
    Puerta Y (Rotación en el eje Y).
    Puerta Z (Rotación en el eje Z).
    Puerta H (Hadamard): Coloca un qubit en superposición.
    Puertas 𝑅𝑥,𝑅𝑦,𝑅𝑧 : Rotaciones arbitrarias en cada eje.
    Puerta S y T: Rotaciones de fase.
    Identidad (I): No cambia el estado.

 """

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit.circuit.library import HGate, XGate, YGate, ZGate, SGate, TGate, RXGate, RYGate, RZGate, IGate
import matplotlib.pyplot as plt

# Función para aplicar puertas y mostrar la esfera de Bloch
def aplicar_puerta(qc, puerta, nombre):
    qc.append(puerta, [0])
    state = Statevector.from_instruction(qc)
    plot_bloch_multivector(state)
    plt.title(f"Después de {nombre}")
    plt.show()

# Estado inicial |0>
qc = QuantumCircuit(1)
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
plt.title("Estado inicial |0⟩")
plt.show()

# Puerta Hadamard (H)
aplicar_puerta(qc, HGate(), "Hadamard (H)")

# Puerta X
aplicar_puerta(qc, XGate(), "X")

# Puerta Y
aplicar_puerta(qc, YGate(), "Y")

# Puerta Z
aplicar_puerta(qc, ZGate(), "Z")

# Puerta S
aplicar_puerta(qc, SGate(), "S")

# Puerta T
aplicar_puerta(qc, TGate(), "T")

# Rotación Rx(π/4)
aplicar_puerta(qc, RXGate(3.14159/4), "Rx(π/4)")

# Rotación Ry(π/4)
aplicar_puerta(qc, RYGate(3.14159/4), "Ry(π/4)")

# Rotación Rz(π/4)
aplicar_puerta(qc, RZGate(3.14159/4), "Rz(π/4)")

# Puerta Identidad (I)
aplicar_puerta(qc, IGate(), "Identidad (I)")
