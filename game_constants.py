from enum import IntEnum, Enum, StrEnum


class CharacterConstants(IntEnum):
    HEALTH = 100
    MOSQUITO_EXCEPTIONAL_HEALTH = 1
    MAX_INCREASE_HEALTH = 25


class Precision(IntEnum):
    """percentage"""
    ARTILLERY = 33
    TANK = 50
    MOSQUITO = 100


class WeaponPower(IntEnum):
    ARTILLERY = 60
    TANK = 40
    MOSQUITO = 1
