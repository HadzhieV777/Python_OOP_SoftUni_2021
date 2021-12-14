from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        capacity = capacity * 0.25
        memory += memory * 0.75
        super().__init__(name, "Power", int(capacity), int(memory))
