# DLKS-MQTT

DLKS-MQTT is a lightweight secure communication framework designed for MQTT-based IoT environments. The project focuses on improving authentication, confidentiality, and integrity in resource-constrained devices by integrating ephemeral session key generation, lightweight hashing, and replay attack mitigation directly into the MQTT communication workflow.

The framework is inspired by lightweight cryptographic principles optimized for low-power IoT ecosystems such as smart homes, healthcare monitoring systems, industrial IoT (IIoT), and sensor-based networks.

## Key Features

- Lightweight ephemeral session key generation using Linear Congruential Generator (LCG)
- MQTT-based secure communication workflow
- Replay attack mitigation using nonce validation
- Message integrity verification using lightweight hashing
- Reduced communication and computational overhead
- Designed for resource-constrained IoT nodes
- Secure handshake mechanism integrated into MQTT communication flow
- Comparative performance analysis against traditional lightweight MQTT security approaches

## Security Objectives

The framework is designed to address major IoT communication threats including:

- Man-in-the-Middle (MitM) attacks
- Replay attacks
- Unauthorized session reuse
- Message tampering
- Lightweight authentication vulnerabilities

## Architecture Overview

The project follows a layered architecture consisting of:

1. Processing Layer  
   Handles key generation and cryptographic operations.

2. Security Logic Layer  
   Manages ephemeral session keys, hashing, and authentication workflows.

3. Data Interaction Layer  
   Controls MQTT communication and input/output handling.

4. Evaluation Layer  
   Performs performance monitoring and visualization analysis.

## Technologies Used

- MQTT Protocol
- Lightweight Cryptography
- C Programming
- Python (for analysis/visualization)
- BLAKE2s Hashing
- Linear Congruential Generator (LCG)
- Contiki OS
- Cooja Simulator

## Current Development Status

🚧 Under active development and refinement.

The repository is currently being structured into a modular security-focused IoT framework with implementation, simulation, benchmarking, and visualization support.

## Planned Enhancements

- Real-time MQTT broker simulation
- Interactive monitoring dashboard
- Machine learning-based anomaly detection
- Dockerized deployment support
- Cross-protocol IoT security extensions
- Post-quantum lightweight cryptographic experimentation

## Research Context

This project explores the balance between strong security and computational efficiency in IoT systems. The implementation emphasizes lightweight operations suitable for low-power devices while maintaining resistance against common communication attacks.

## License

This project is licensed under the MIT License.
