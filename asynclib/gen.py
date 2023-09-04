def f(data, *, mode):
    if mode:
        return data ** 2
    return data ** 3
print(f'{f(123,mode=True) = :,}')
print(f'{f(123,mode=False) = :,}')