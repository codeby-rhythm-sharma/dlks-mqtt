# DLKS-MQTT

DLKS-MQTT (Dynamic Lightweight Key Sharing for MQTT) is a research-oriented IoT security framework designed to strengthen MQTT-based communication in resource-constrained environments through lightweight cryptographic mechanisms, secure authentication workflows, and attack-resistant communication protocols.

The framework integrates ephemeral 128-bit session key generation, nonce-based replay attack mitigation, lightweight hashing using BLAKE2s, and a secure MQTT handshake mechanism to enhance confidentiality, integrity, and authentication while maintaining minimal computational and communication overhead.

Developed with a focus on low-power IoT ecosystems, DLKS-MQTT addresses critical security threats including Man-in-the-Middle (MitM) attacks, replay attacks, unauthorized session reuse, and message tampering. The framework is designed for deployment across smart homes, Industrial IoT (IIoT), healthcare monitoring systems, smart cities, and sensor-based networks where security and efficiency must coexist.

Simulation and evaluation results demonstrate strong security characteristics while maintaining lightweight performance, achieving minimal communication overhead and efficient resource utilization suitable for constrained IoT devices.


---

## ✨ Key Features

* Implemented lightweight 128-bit ephemeral session key generation for secure communication.
* Protected against replay attacks through nonce validation mechanisms.
* Mitigated Man-in-the-Middle (MitM) attacks using secure authentication workflows.
* Achieved communication overhead of only 60 bytes while maintaining robust security properties.
* Demonstrated CPU energy consumption of approximately 0.000002 mJ in simulated environments.
* Evaluated using Contiki OS and Cooja Simulator for resource-constrained IoT deployments.


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
