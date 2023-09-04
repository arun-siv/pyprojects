from threading import Thread
from time import sleep
from random import Random
rnd = Random(0)


def f(k):
    return k + 1

def target1():
    owned = _owned['target1']
    while True:
        print(f'thread1 {shared = } {owned =}')
        k = rnd.choice([*shared.keys()])
        k = rnd.choice([*shared.keys()])
        shared[k] = f(shared[k])
        owned[k] = f(owned[k])  
        sleep(1)

def target2():
    owned = _owned['target2']
    while True:
        print(f'thread2 {shared = } {owned =}')
        k = rnd.choice([*shared.keys()])
        shared[k] = f(shared[k])
        owned[k] = f(owned[k])
        sleep(1)

shared = {'a':1,'b':2,'c':3}

_owned = {
    'target1': {'a':1,'b':2,'c':3},
    'target2': {'a':1,'b':2,'c':3},

}

pool = [Thread(target=target1),Thread(target=target2)]
for i in pool:i.start()
for i in pool: i.join()