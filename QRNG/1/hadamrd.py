from qiskit import QuantumCircuit, Aer, transpile, assemble

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply the Hadamard gate to put the qubit into superposition
qc.h(0)

# Measure the qubit to collapse it into a definite state
qc.measure(0, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)

# Execute the circuit and get the result
result = simulator.run(qobj).result()
counts = result.get_counts(qc)
print("Random bit:", list(counts.keys())[0])
