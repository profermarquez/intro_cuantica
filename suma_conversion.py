from qiskit_aer import Aer
"""
Aer: Es el módulo de simulación cuántica de Qiskit. Proporciona simuladores 
clásicos que permiten ejecutar circuitos cuánticos sin necesidad de acceder 
a un dispositivo cuántico real.
"""
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram


# Función para convertir decimal a binario (de longitud fija)
def decimal_a_binario(num, longitud=2):
    return format(num, 'b').zfill(longitud)

# Función para convertir binario a decimal
def binario_a_decimal(bin_str):
    return int(bin_str, 2)

# Números decimales de entrada
num1 = 1
num2 = 1

# Convertir a binario
bin1 = decimal_a_binario(num1)
bin2 = decimal_a_binario(num2)

print(f"Números en binario: {bin1} y {bin2}")

# Crear un circuito cuántico con 2 qubits y 1 bit clásico
qc = QuantumCircuit(2, 1)

# Preparar los qubits en los valores binarios
if bin1[1] == '1':
    qc.x(0)  # Qubit 0 en estado 1
if bin2[1] == '1':
    qc.x(1)  # Qubit 1 en estado 1

# Aplicar una puerta CNOT para realizar la suma módulo 2
qc.cx(0, 1)

# Medir el segundo qubit para obtener el resultado
qc.measure(1, 0)

# Dibujar el circuito
print(qc.draw())

# Ejecutar el circuito en el simulador cuántico seleccionando el backend del simulador
simulator = Aer.get_backend('qasm_simulator')

# Transpilar el circuito para el backend seleccionado
transpiled_qc = transpile(qc, simulator)

# Ejecutar el circuito transpileado en el backend
job = simulator.run(transpiled_qc, shots=1000)
result = job.result()

# Obtener el conteo de resultados
counts = result.get_counts(qc)

# Mostrar los resultados en binario
print("Resultado en binario:", counts)
plot_histogram(counts)

# Convertir el resultado binario a decimal
resultado_binario = max(counts, key=counts.get)
resultado_decimal = binario_a_decimal(resultado_binario)

print(f"\nEl resultado de la suma en decimal es: {resultado_decimal}")
