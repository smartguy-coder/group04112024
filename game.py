from abc import ABC, abstractmethod

from game_constants import CharacterConstants, Precision


class Character(ABC):
    def __init__(self, name: str, precision: int):
        self.name = name
        self.health = CharacterConstants.HEALTH.value
        self.precision = precision

    @abstractmethod
    def __str__(self):
        pass


class Tank(Character):
    def __str__(self):
        return f'I am a Tank. My brand name is {self.name}'

    def __init__(self, name: str):
        super().__init__(name, precision=Precision.TANK.value)


class Artillery(Character):
    def __str__(self):
        return f'I am an arta unit. My name is {self.name}'

    def __init__(self, name: str):
        super().__init__(name, precision=Precision.ARTILLERY.value)


tank = Tank('T-64')
tank2 = Tank('Abrams')
arta = Artillery('M-777')
print(arta)
print(tank)
pass
