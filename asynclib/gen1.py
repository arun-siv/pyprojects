from random import Random
from collections import namedtuple
from string import ascii_lowercase
from statistics import mean, pstdev

rnd = Random(0)

class Entity(namedtuple('EntityBase','name value')):
    @classmethod
    def from_random(cls,*,random_state=None):
        random_state = random_state if random_state is not None else Random()
        return cls(
            name=''.join(rnd.choices(ascii_lowercase,k=4)),
            value=rnd.randint(-1_000, +1_000)
        )


class Analysis:
    def __init__(self,random_state=None):
        self.random_state = random_state if random_state is not None else Random()
    
    def load(self):
        self.data = [
            Entity.from_random(random_state=self.random_state)
            for _ in range(100)
            ]
        return self.data

    def clean(self):
        pass
    def compute(self):
        pass

obj = Analysis(random_state=None)
data = obj.load()
print(f'{data = }')