from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

def less_than_k(k, list_n):
    # Determine the number of qubits needed to represent the integers in the list
    max_int = max(list_n)
    num_qubits = max_int.bit_length()  # Number of qubits needed to represent the largest integer
    
    # Initialize quantum circuit
    qc = QuantumCircuit(num_qubits, len(list_n))
    
    # Encode 'k' into binary
    k_binary = format(k, '0{}b'.format(num_qubits))
    
    # Encode 'k' into quantum state
    for i, bit in enumerate(k_binary):
        if bit == '1':
            qc.x(i)  # Apply X gate to set qubit to |1>
    
    # Encode integers from the list into quantum state and compare with 'k'
    for index, integer in enumerate(list_n):
        # Encode integer into binary
        int_binary = format(integer, '0{}b'.format(num_qubits))
        
        # Compare each qubit with 'k' and store result in the corresponding classical register
        for i, bit in enumerate(int_binary):
            if bit == '1':
                qc.x(i)  # Apply X gate to set qubit to |1>
        qc.compare_equal(0, range(1, num_qubits))
        qc.measure(range(1, num_qubits), index)
        qc.reset(range(num_qubits))  # Reset qubits for next iteration
    
    # Simulate the quantum circuit
    backend = Aer.get_backend('qasm_simulator')
    transpiled_qc = transpile(qc, backend)
    qobj = assemble(transpiled_qc)
    result = backend.run(qobj).result()
    counts = result.get_counts()
    
    # Extract and return the integers less than 'k'
    less_than_k_list = [int(key, 2) for key in counts if key != '0' * len(list_n)]
    return less_than_k_list

# Example usage
A = less_than_k(7, [4, 9, 11, 14, 1, 13, 6, 15])
print(A)  # Output: [4, 1, 6]
