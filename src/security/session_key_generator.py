import random
import time


class LightweightSessionKeyGenerator:

    def __init__(self, seed=None):

        if seed is None:
            seed = int(time.time())

        self.seed = seed

    def generate_key(self):

        random.seed(self.seed)

        session_key = ''.join(
            random.choice('0123456789ABCDEF')
            for _ in range(32)
        )

        return session_key


generator = LightweightSessionKeyGenerator()

key = generator.generate_key()

print("Generated Session Key:")
print(key)