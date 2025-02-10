from abc import ABC, abstractmethod
from random import randint

from typing import Self

from game_constants import CharacterConstants, Precision, WeaponPower


class Character(ABC):
    def __init__(self, name: str, precision: int, power: int):
        self.name = name
        self._health = CharacterConstants.HEALTH.value
        self.precision = precision
        self.power = power

    @abstractmethod
    def __str__(self):
        pass

    @property
    def is_alive(self) -> bool:
        return self._health > 0

    def attack(self, other: Self):
        if not self.is_alive:
            print(f'{self} out of game')
            return

        if not other.is_alive:
            print(f'{other} already has gone')
            return

        random_value = randint(0, 100)
        is_enemy_hit = self.precision >= random_value
        if is_enemy_hit:
            other._health -= self.power
            print(f'{self} hit {other}')

        if not other.is_alive and hasattr(other, 'is_nuclear'):
            print(other.is_nuclear, 5555555555)
            self._health = 0
            print('A' * 50)


class Tank(Character):
    def __str__(self):
        return f'I am a Tank. My brand name is {self.name}, currently I have {self._health} points of health'

    def __init__(self, name: str):
        super().__init__(name, precision=Precision.TANK.value, power=WeaponPower.TANK.value)


class NuclearTank(Tank):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_nuclear = True


class Artillery(Character):
    def __str__(self):
        return f'I am an arta unit. My name is {self.name}, currently I have {self._health} points of health'

    def __init__(self, name: str):
        super().__init__(name, precision=Precision.ARTILLERY.value, power=WeaponPower.ARTILLERY.value)


class Mosquito(Character):
    def __str__(self):
        return f'I am a mosquito. My name is {self.name}, currently I have {self.health} points of health'

    def __init__(self, name: str):
        super().__init__(name, precision=Precision.MOSQUITO.value, power=WeaponPower.MOSQUITO.value)
        self.health = CharacterConstants.MOSQUITO_EXCEPTIONAL_HEALTH.value


tank = Tank('T-64')
tank2 = Tank('Abrams')
arta = Artillery('M-777')
mosc = Mosquito('M-777')
nucl = NuclearTank('Chernobyl-22')
print(arta)
print(tank)

arta.attack(tank2)
arta.attack(nucl)
arta.attack(nucl)

arta.attack(nucl)
arta.attack(nucl)
arta.attack(nucl)
arta.attack(nucl)
arta.attack(nucl)
arta.attack(nucl)
arta.attack(nucl)
arta.attack(nucl)
mosc.attack(nucl)
mosc.attack(nucl)
mosc.attack(nucl)
mosc.attack(nucl)

n = 'ghg'



m = []


mm = hasattr(n, 'extend')

pass
