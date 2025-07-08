# 🧪 Quantum Random Number Generator (QRNG) with Django & IBM Qiskit

This project implements a Quantum Random Number Generator (QRNG) using IBM Quantum's real quantum backends through Qiskit Runtime, wrapped in a Django web framework for API access and frontend interaction. It generates high-entropy quantum random numbers by leveraging quantum superposition and measurement, with support for entropy analysis and range-based random number scaling.

---

## 🌐 Live Preview

> Run locally on: `http://127.0.0.1:8000/`  
> Access the random number API at: `POST http://127.0.0.1:8000/random`

---

## 📌 Key Features

- ✅ Quantum randomness using real IBM Q backends (or simulator fallback)
- ✅ Secure IBM Quantum token handling using `.env` file
- ✅ Shannon Entropy analysis for randomness strength
- ✅ User-defined range scaling of quantum-generated output
- ✅ Web frontend + JSON API output
- ✅ Django-powered backend structure
- ✅ Modular and clean code organization

---

## 🧰 Tech Stack

| Component       | Technology                             |
|----------------|-----------------------------------------|
| Quantum Backend | IBM Quantum (Qiskit Runtime)            |
| Language        | Python 3.11                             |
| Web Framework   | Django                                  |
| Frontend        | HTML, CSS (Basic Styling)               |
| API Format      | JSON                                    |
| Hosting         | Localhost (127.0.0.1)                   |
| Security        | `.env` + `.gitignore` to hide secrets   |

---
