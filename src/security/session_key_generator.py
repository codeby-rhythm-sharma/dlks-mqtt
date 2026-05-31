"""
DLKS-MQTT Lightweight Session Key Generator

This module implements lightweight ephemeral session key
generation for secure MQTT-based IoT communication.

Author: DLKS-MQTT Contributors
"""

import time
import hashlib

class LightweightSessionKeyGenerator:
"""
Lightweight ephemeral session key generation
using a simple Linear Congruential Generator approach.
"""

```
def __init__(self, seed=12345):
    self.seed = seed

def generate_session_key(self):
    """
    Generate lightweight session key.
    """

    current_time = int(time.time())

    generated_value = (
        (1103515245 * (self.seed + current_time) + 12345)
        % (2**31)
    )

    session_key = hashlib.blake2s(
        str(generated_value).encode()
    ).hexdigest()

    return session_key
```

if **name** == "**main**":

```
generator = LightweightSessionKeyGenerator()

key = generator.generate_session_key()

print("Generated Lightweight Session Key:")
print(key)
```
