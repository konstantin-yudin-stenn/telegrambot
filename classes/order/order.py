from dataclasses import dataclass


@dataclass
class Order:
    taste = None
    frosty = None
    strong = None

    def __str__(self):
        return (f'Taste: {self.taste}\n'
                f'Strong: {self.strong}\n'
                f'Frosty: {self.frosty}')
