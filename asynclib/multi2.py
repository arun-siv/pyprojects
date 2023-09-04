from concurrent.futures import ProcessPoolExecutor
from itertools import product
from collections import namedtuple


def target(d):
    return d.x ** d.y

Data = namedtuple('Data','x y')
dataset = [Data(x,y) for x,y in product(range(3),repeat=2)]
with ProcessPoolExecutor(max_workers=4) as pool:
    results = pool.map(target,dataset)
# print(f'{[*results] = }')
print(f'{dataset = }')
print(f'{dict(zip(dataset,results)) = }')