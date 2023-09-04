from multiprocessing import Process
from itertools import product
from time import sleep

def target(x,y):
    sleep(1)
    print(f'{x ** y = }')

pool = [Process(target=target, kwargs={'x':x , 'y':y}) for x,y in product(range(3),repeat=2)]
for x in pool: x.start()
for x in pool: x.join()


