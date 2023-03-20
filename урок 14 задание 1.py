def sp_el(x):
    if x < 0:
        return
    print(x)
    sp_el(x - 1)


sp_el(16)
print('конец списка')
