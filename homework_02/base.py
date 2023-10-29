from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            return
        elif self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError('топлива недостаточно для запуска двигателя')

    def move(self, distanse):
        fuel_required = distanse *self.fuel_consumption
        if self.fuel >= fuel_required:
            self.fuel -= fuel_required
            return self.fuel
        else:
            raise NotEnoughFuel('топлива недостаточно для преодоления дистанции')