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

## ⚙️ Setup Instructions

### 1. 🧬 Clone the Repository

```bash
git clone https://github.com/radhikajamwal/Quantum-Random-Number-Generator.git
cd Quantum-Random-Number-Generator
```

### 2.🔐 Create `.env` File

In the root folder, create a .env file and add your IBM Quantum API token:
```bash
TOKEN=your_ibmq_token_here
```

### 3. 📦 Install Dependencies

Make sure Python 3.11+ is installed and IBM account is active

### 4. 🚀 Run the Django Server

```bash
python manage.py runserver
```
Open in browser: http://127.0.0.1:8000

---

## 📡 API Usage

🔸 Endpoint: /random
Method: POST

Content-Type: application/json

🔸 Sample Request:
```bash
{
  "device": "ibmq_qasm_simulator",
  "min": 0,
  "max": 100
}
```

🔸 Sample Response:
```bash
{
  "result": 47,
  "entropy": 4.91,
  "bitstrings": {
    "01001": 57,
    "10011": 43
  }
}
```
---

## 🔢 Entropy Calculation

Shannon entropy is used to measure unpredictability of the bitstring distribution:
```bash
H(X) = -Σ p(x) * log₂(p(x))
```
🔸 Ideal entropy for 5 qubits = 5.0

🔸 Higher entropy = better randomness

---

## 📁 Project Structure

```bash
qsite/
├── qrng/              # Django app (views, URLs)
│   ├── views.py
│   └── urls.py
├── templates/         # Frontend templates
│   └── index.html
├── static/            # CSS/JS assets (optional)
├── qsite/             # Django config
├── .env               # Your IBM Quantum token (ignored in git)
├── .gitignore
├── manage.py
└── README.md
```
---

## ✅ .gitignore

```bash 
.env
__pycache__/
*.pyc
*.log
db.sqlite3
```
---

## 🛡️ Security Notes

🔸 Use os.getenv("TOKEN") in your code to fetch the API key

🔸 Never hardcode secrets in Python files

🔸 Revoke/reset your IBM Q token if accidentally exposed

---

## 📖 References

[Qiskit Documentation](https://quantum.cloud.ibm.com/docs/en)

[IBM Quantum Platform](https://www.ibm.com/quantum)

[Django Docs](https://docs.djangoproject.com/en/5.2/)

[Shannon Entropy (Wikipedia)](https://en.wikipedia.org/wiki/Entropy_(information_theory))

---

## 👩‍💻 Author  

**Radhika Jamwal**  
🔗 [LinkedIn](https://www.linkedin.com/in/radhika-jamwal-0631472b6)  
🌐 [GitHub](https://github.com/radhikajamwal)

