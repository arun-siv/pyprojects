from threading import Thread,Lock
from time import sleep
from random import Random
rnd = Random(0)

lock = Lock()

def f(k):
    return k + 1

def target1():
    owned = _owned['target1']
    while True:
        print(f'thread1 {shared = } {owned =}')
        with lock:
            k = rnd.choice([*shared.keys()])
            v = shared[k]
            shared[k] = f(v)
            owned[k] = f(v)  
        sleep(1)

def target2():
    owned = _owned['target2']
    while True:
        print(f'thread2 {shared = } {owned =}')
        with lock:
            k = rnd.choice([*shared.keys()])
            v = shared[k]
            shared[k] = f(v)
            owned[k] = f(v)  
        sleep(1)

shared = {'a':1,'b':2,'c':3}

_owned = {
    'target1': {'a':1,'b':2,'c':3},
    'target2': {'a':1,'b':2,'c':3},

}

pool = [Thread(target=target1),Thread(target=target2)]
for i in pool:i.start()
for i in pool: i.join()