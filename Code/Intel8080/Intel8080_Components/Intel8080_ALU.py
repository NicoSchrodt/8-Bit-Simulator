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

    def set_acu(self, value):
        self.accumulator = value

    def get_acu(self):
        return self.accumulator

    def set_temp_acu(self, value):
        self.temp_accumulator = value

    def get_temp_acu(self):
        return self.temp_accumulator

    def set_temp_register(self, value):
        self.temp_register = value

    def get_temp_register(self):
        return self.temp_register

    def set_zero_flag(self, state):
        self.flags[0] = state

    def get_zero_flag(self):
        return self.flags[0]

    def set_carry_flag(self, state):
        self.flags[1] = state

    def get_carry_flag(self):
        return self.flags[1]

    def set_sign_flag(self, state):
        self.flags[2] = state

    def get_sign_flag(self):
        return self.flags[2]

    def set_parity_flag(self, state):
        self.flags[3] = state

    def get_parity_flag(self):
        return self.flags[3]

    def set_auxiliary_carry_flag(self, state):
        self.flags[4] = state

    def get_auxiliary_carry_flag(self):
        return self.flags[4]
