class Switch:
    def __init__(self, name: str, status: bool = False):
        self.name = name
        self.status = status

    def turn(self):
        self.status = not self.status

    def clone(self) -> "Switch":
        return Switch(self.name + ".copy", self.status)

    def __str__(self):
        status = "on" if self.status else "off"
        return f"switch({self.name}) is {status}"


class Light:
    def __init__(self, name: str, switch: Switch):
        self.name = name
        self.switch = switch

    def turn(self):
        self.switch.turn()

    def get_status(self) -> str:
        status = "on" if self.switch.status else "off"
        return status

    def set_switch(self, new_switch):
        self.switch = new_switch

    def clone(self):
        return Light(self.name + ".copy", self.switch.clone())

    def __str__(self):
        return f"light({self.name}) with {self.switch}"
