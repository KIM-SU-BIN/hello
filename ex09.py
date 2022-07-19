s = ''
str1 = 'hello world'
str2 = "안녕 세상"

print(s, str1, str2)
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

print(2,4,6,sep=" , ")  #이런경우 숫자 사이 공백과 콤마 표시가 나타남!

print("=========================================")

s01="aaa"
s02="bbb"
print(id(s01))
print(id(s02))

s01="aaaa"
print(id(s01))

print("=========================================")
str = "abcdefghijk"
print(id(str))

str3 = """ABCDEFG
abcdef
가나다라마
123456789"""
print(str3)

print("=========================================")
print('Hello\nWorld\nI\'d Say "hello World"')
print("Hello\nWorld\nI'd Say \"hello World\"")

print("Hello\rWorld")
print("Hello\bWorld")
print("Hello\tWorld")



