#정수형

a = 101
print(type(a))
print(isinstance(a, int))

#2, 8, 16진수 표현 가능 => 10진수로 표현 가능
b = 0b101  # 2진수
c = 0o101  # 8진수
d = 0x101  # 16진수
print(b,c,d)

#10진수 => 2, 8, 16진수 표현
print(bin(5))
print(oct(65))
print(hex(257))

#파이썬 3.x 에서는 long형이 없어지고 int 타입으로 처리된다.  따라서 표현범위는 무한대이다.
e = 2**1024
print(type(e))
print(e)
