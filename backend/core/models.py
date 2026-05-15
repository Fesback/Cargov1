from dataclasses import dataclass

@dataclass
class Package:
    id: str
    name: str
    weight: int
    value: int

@dataclass
class Container:
    max_weight: int
    