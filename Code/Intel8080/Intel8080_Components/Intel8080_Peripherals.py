import numpy as np


class Intel8080_Peripherals():
    def __init__(self):
        self.data_bus_latch = np.uint8(0)
        self.address_buffer = np.uint16(0)

    def set_address_buffer(self, value):
        self.address_buffer = np.uint16(value)

    def set_data_bus_latch(self, value):
        self.data_bus_latch = np.uint8(value)