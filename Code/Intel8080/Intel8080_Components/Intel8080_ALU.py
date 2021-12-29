import numpy as np


class Intel8080_ALU():
    def __init__(self):
        self.accumulator = np.uint8(0)
        self.temp_accumulator = np.uint8(0)
        self.flags = [0,  # Zero
                      0,  # Carry
                      0,  # Sign
                      0,  # Parity
                      0  # Auxiliary Carry
                      ]
        self.temp_register = np.uint8(0)

    def perform_operation(self):
        pass
        # Perform an Operation with the ALU
