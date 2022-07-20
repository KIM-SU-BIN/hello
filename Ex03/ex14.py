x=1

def func(a):
    global x
    x=100
    return a + x

print(func(10))
print(x)

print("===========================================")

g = 1
def func3(a):
    global g
    g = 3
    return a + g

print(func3(10))
print(g)
