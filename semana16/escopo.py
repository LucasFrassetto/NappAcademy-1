def f1(a):
    print(a)
    print(b)

# f1(10)

b = 6
f1(10)

def f2(a):
    print(a)
    print(b)
    b = 9

# f2(10)

def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(10)
print(b)

from dis import dis
dis(f1)
dis(f2)
