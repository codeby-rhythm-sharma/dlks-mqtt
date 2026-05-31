# DLKS-MQTT

DLKS-MQTT is a lightweight secure communication framework designed for MQTT-based IoT environments. The project focuses on improving authentication, confidentiality, and integrity in resource-constrained devices by integrating ephemeral session key generation, lightweight hashing, and replay attack mitigation directly into the MQTT communication workflow.

The framework is inspired by lightweight cryptographic principles optimized for low-power IoT ecosystems such as smart homes, healthcare monitoring systems, industrial IoT (IIoT), and sensor-based networks.

---

## ✨ Key Features

* Lightweight ephemeral session key generation using Linear Congruential Generator (LCG)
* MQTT-based secure communication workflow
* Replay attack mitigation using nonce validation
* Message integrity verification using lightweight hashing
* Reduced communication and computational overhead
* Designed for resource-constrained IoT nodes
* Secure handshake mechanism integrated into MQTT communication flow
* Comparative performance analysis against traditional lightweight MQTT security approaches

---

## 🔐 Security Objectives

The framework is designed to address major IoT communication threats including:

* Man-in-the-Middle (MitM) attacks
* Replay attacks
* Unauthorized session reuse
* Message tampering
* Lightweight authentication vulnerabilities

---

## 🏗️ Architecture Overview

![DLKS-MQTT Architecture](assets/architecture.png)

The project follows a layered architecture consisting of:

### Processing Layer

Handles key generation and cryptographic operations.

### Security Logic Layer

Manages ephemeral session keys, hashing, and authentication workflows.

### Data Interaction Layer

Controls MQTT communication and input/output handling.

### Evaluation Layer

Performs performance monitoring and visualization analysis.

---

## ⚙️ Technologies Used

* MQTT Protocol
* Lightweight Cryptography
* C Programming
* Python (for analysis and visualization)
* BLAKE2s Hashing
* Linear Congruential Generator (LCG)
* Contiki OS
* Cooja Simulator

---

## 🚧 Current Development Status

The repository is currently being structured into a modular security-focused IoT framework with implementation, simulation, benchmarking, and visualization support.

Planned additions include:

* Real-time MQTT broker simulation
* Interactive monitoring dashboard
* Machine learning-based anomaly detection
* Dockerized deployment support
* Cross-protocol IoT security extensions
* Post-quantum lightweight cryptographic experimentation

---

## 📊 Research Context

This project explores the balance between strong security and computational efficiency in IoT systems. The implementation emphasizes lightweight operations suitable for low-power devices while maintaining resistance against common communication attacks.

The framework is designed with a focus on:

* Lightweight authentication
* Secure MQTT communication
* Reduced latency and overhead
* IoT-specific attack mitigation
* Scalable security architecture for constrained environments

---

## 📁 Repository Structure

```bash
dlks-mqtt/
│
├── assets/         # Architecture diagrams and visual assets
├── docs/           # Technical documentation and project report
├── src/            # Core implementation files
├── results/        # Benchmarking and evaluation outputs
└── README.md
```

---
## Future Scope

* Real-time MQTT broker deployment
* Lightweight IoT node benchmarking
* Secure edge-device communication testing
* Dockerized simulation support
* Cloud-integrated MQTT monitoring
* AI-assisted anomaly detection for MQTT traffic

## Academic Context

This project was developed as part of an academic research-oriented exploration into lightweight IoT security frameworks and secure MQTT communication architectures for resource-constrained environments.

## 🤝 Contributors

* Rhythm Sharma
* Harshil Srivastava
* Sankalp Tripathi
* Mayank Singh
* Palla Pranavi

---

## 📄 License

This project is licensed under the MIT License.
