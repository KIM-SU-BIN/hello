#복소수

#복소수 타입의 객체는 실수부+허수부로 나뉘며 허수부에는 j 또는 J를 숫자 뒤에 붙인다.
a = 4 + 5j
print(type(a))  #<class 'complex'> => a의 타입이 complex
print(isinstance(a, complex))   #true

#복소수 연산이 가능하며 실수부와 허수부 값만 따로 참조할 수 있다.
a = 4 + 5j
b = 7 - 2j
print(a + b)    #(11+3j)
print(b.real, b.imag)   #7.0 -2.0

#complex 함수를 이용하여 복소수 타입의 객체를 만들 수 있다. 타입 판별함수가 아니다.
a = 2.0
print(type(a))
print(complex(a))

