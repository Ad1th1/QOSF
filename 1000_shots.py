import numpy as np
from qiskit import QuantumCircuit, Aer, execute

n = 5
qc = QuantumCircuit(n, n)

qc.h(range(n))

qc.measure(range(n), range(n))

simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots = 1000)

result = job.result()

counts = result.get_counts(qc)

num_shots = sum(counts.values())
num_0s = sum(counts[key] for key in counts if '0' in key)
num_1s = sum(counts[key] for key in counts if '1' in key)

proportion_0s = num_0s / num_shots
proportion_1s = num_1s / num_shots

with open('randomness_results.txt', 'w') as f:
    f.write("Counts:\n")
    for outcome, count in counts.items():
        f.write(f"{outcome}: {count}\n")
    f.write(f"Proportion of 0s: {proportion_0s}\n")
    f.write(f"Proportion of 1s: {proportion_1s}\n")

    
