from threading import Thread
from time import sleep
from random import Random
rnd = Random(0)
d = {'a':1,'b':2,'c':3}

def f(k):
    return k ** 2

def target1():
    while True:
        print(f'thread1 {len(d) = }')
        # d[len(d)] = None
        d[k] = f(d[k:= rnd.choice([*d.keys()])])
        '''
        random.choice([*d.keys()]): 
        This selects a random key from the dictionary d. [*d.keys()] is used to convert
        the dictionary keys to a list, and then random.choice picks one of the keys randomly.
        
        k := random.choice([*d.keys()]): This is an assignment expression, using the
        walrus operator :=. It assigns the randomly selected key to the variable k and also
        returns its value. So, k will hold the randomly selected key.
        
        f(d[k]): This calls the function f with the value corresponding to the randomly selected
        key k from the dictionary d. The function f calculates the square of this value.

        d[k] = f(d[k]): This assigns the calculated square value back to the dictionary
        with the key k.
        
        '''
        sleep(1)

def target2():
    while True:
        # print(f'thread2 {len(d) = }')
        print(f'thread1 {len(d) = }')
        # d[len(d)] = None
        d[k] = f(d[k:= rnd.choice([*d.keys()])])
        sleep(1)

pool = [Thread(target=target1),Thread(target=target2)]