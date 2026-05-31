"""
DLKS-MQTT Replay Attack Protection Module

This module implements nonce-based replay attack
detection for lightweight MQTT communication.

Author: DLKS-MQTT Contributors
"""

import time

class ReplayAttackProtection:
"""
Lightweight nonce validation system
for replay attack mitigation.
"""

```
def __init__(self):
    self.used_nonces = set()

def generate_nonce(self):
    """
    Generate time-based nonce.
    """

    return str(int(time.time() * 1000))

def validate_nonce(self, nonce):
    """
    Validate nonce to prevent replay attacks.
    """

    if nonce in self.used_nonces:
        return False

    self.used_nonces.add(nonce)
    return True
```

if **name** == "**main**":

```
protection = ReplayAttackProtection()

nonce = protection.generate_nonce()

print("Generated Nonce:", nonce)

if protection.validate_nonce(nonce):
    print("Valid communication request")
else:
    print("Replay attack detected")
```
