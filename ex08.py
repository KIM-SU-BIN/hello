# 확장 연산자
x = 2
x+=5
print(x)

x-=3
print(x)

x**=3
print(x)

print("===================================")

# 관계 연산자
print(1 > 3)
print(2 < 4)
print(4 <= 5)
print(4 >= 5)
print(6 == 9)
print(6 != 9)

print("===================================")

a = 6
print(0 < a < 10)
print(0 < a and a < 10)

print("===================================")

a = 10
b = 20
c = a

print(id(a))    # 2743137927696 (주소값 | 매번 달라짐)

print(a == b)
print(a is b)
print(a is c)

print("===================================")
# 논리 연산자
print(True and True)
print(False and True)

print(True or True)
print(False or True)

print(not True)
print(not False)

print("===================================")
print(abs(-3))      #절대값으로 : 3
print(int(3.1415))      #정수형으로 : 3
print(float("3"))      #실수형으로 : 3.0
print(complex("3"))      #복소수형으로 : (3+0j)
print(pow(2,10))        #승수계산 : 1024