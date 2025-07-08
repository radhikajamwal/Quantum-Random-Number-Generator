import json, math
import os
from dotenv import load_dotenv  
load_dotenv()
from django.http import JsonResponse
from django.shortcuts import render
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister,transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler, SamplerOptions, Session

TOKEN = os.getenv("TOKEN")

# Authenticate with IBMQ
service = QiskitRuntimeService(channel="ibm_quantum", token=TOKEN)

def home(request):
    return render(request, "index.html")

def shannon_entropy(counts_dict):
    total = sum(counts_dict.values())
    entropy = 0
    for count in counts_dict.values():
            probability = count / total
            entropy -= probability * math.log2(probability)
    return entropy


def random(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests allowed"}, status=405)

    try:
        body = json.loads(request.body)
        device = body.get("device")
        min_val = int(body.get("min", 0))
        max_val = int(body.get("max", 100))

        # Select backend
       # backend = service.get_backend("ibmq_qasm_simulator")
        backend = service.least_busy(operational=True, simulator=False)

        # Define quantum circuit
        num_q = 5 if device != "ibmq_qasm_simulator" else 32
        q = QuantumRegister(num_q, "q")
        c = ClassicalRegister(num_q, "c")
        circuit = QuantumCircuit(q, c)
        circuit.h(q)  # Hadamard gates for superposition
        circuit.measure(q, c)

        transpiled_circuit = transpile(circuit, backend=backend)
       

        # Run the sampler using Primitives V2
        with Session(service=service, backend=backend) as session:
            sampler = Sampler(mode=session)
            job = sampler.run([transpiled_circuit])
            job_result = job.result()[0]

            # Get measurement results
        
        counts = job_result.join_data().get_counts()
        entropy = shannon_entropy(counts)

        
        most_frequent_bitstring = max(counts, key=counts.get)
        result = int(most_frequent_bitstring, 2)  # Convert binary to integer

        # Scale result to user-defined range
        final_result = min_val + result % (max_val + 1 - min_val)

        return JsonResponse({
            "result": final_result,
            "entropy": round(entropy, 4),
            "bitstrings": counts
        })

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)
        
