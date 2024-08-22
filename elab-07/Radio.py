class Radio:
    def __init__(self, mode="FM", frequency=87.5):
        self.mode = mode
        self.frequency = frequency
        self.range = [87.5, 108]

    def set_mode(self, mode):
        if mode == "FM":
            self.frequency = 87.5
            self.range = [87.5, 108]
        else:
            self.frequency = 150
            self.range = [150, 280]
        self.mode = mode

    def set_frequency(self, frequency):
        if self.range[0] <= frequency <= self.range[1]:
            self.frequency = frequency

    def adjust_frequency(self, frequency):
        new_frequency = self.frequency + frequency
        if self.range[0] <= new_frequency <= self.range[1]:
            self.frequency = new_frequency
            return True
        return False

    def get_mode(self):
        return self.mode

    def get_frequency(self):
        return self.frequency

    def __str__(self):
        suffix = ""
        if self.mode == "FM":
            suffix = "MHz"
        else:
            suffix = "kHz"
        return f"{self.mode} Radio: {self.frequency:.1f} {suffix}"
