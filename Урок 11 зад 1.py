a = int(input('введите число '))
def fact(a):
    b =[]
    pr = 1
    for i in range(1,a+1):
        pr = pr*i
        b.append(pr)
        b.sort(reverse=True)
    print('факториал числа:',a,'=',pr)
    print(b)
fact(a)
