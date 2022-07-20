def plus(a,b):
    sum = a+b
    return  sum


result = plus(3,7)
print(result)

'''
result = plus(3,"한글")
print(result)
숫자 + 문자는 불가함
'''

print("================================================")

def my_function():
    print("hello world")

my_function()

print("================================================")

'''
a, b = (1, 2)
print(a)
print(b)
'''

#합과 곱을 같이 줌!
def sum_and_mul(a,b):
    sum = a+b
    mul = a*b
    return sum,mul

num1,num2 = sum_and_mul(3,7)
print(num1)
print(num2)

result = sum_and_mul(3,7)
print(result, type(result))
print(result[0])
print(result[1])

print("================================================")

def plusPrint(a=0, b=0):
    print("a=%d, b=%d 이고 합은 %d 입니다." % (a,b, a+b))

plusPrint(3,7)
plusPrint(7)
# plusPrint(, 7)  #오류
plusPrint(b=70)
plusPrint(b=7, a=3)

print("================================================")
def sum_many(name, *data):
   print(name)
    #data = (1,2,3,4,5)
    #data = (2,1)

   sum = 0;
   for num in data:
       sum = sum + num

       return sum

print(sum_many(1,2,3,4,5,6,7,8,9,"황일영"))

print(sum_many(1,2,"황일영"))
print(sum_many(1,2,3))
print(sum_many(1,2,3,4))

print("================================================")

def sum_mul(mode, *args):
    #더하기
    if mode == "sum":
        result = 0
        for i in args:
            result = result + i

    elif mode == "mul":
        result=1
        for i in args:
            result = result * i

    else:
        result ="오류"

        return result


print(sum_mul("sum",1,2,3,4,5))
print(sum_mul("mul",1,2,3))