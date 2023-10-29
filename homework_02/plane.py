"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo =0):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        new_cargo = self.cargo + add_cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload('перегруз')
        else:
            self.cargo = new_cargo

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo