str1 = "FirstString"
str2 = "SecondString"

#문자열과 숫자 조합은 안됨
#print(str1 + 10)
#print(str2 * 3)

print(str1 + str(10))
print(str1*3)
print(str1[5])
print(str1[-4])
print(str1[2:5])
print(str1[1:9:3])
print(str1[:9])
print(str1[2:])
print(len(str1))

print(str1[:])
print(str1[-6:-2])

print(str1[::-1])

print("=========================================")

name = "우영호"
name2 = name[::-1]
name3 = name[:-1:]

print(name2)
print(name3)

str1[7] = a
print(str1)
#바꿀 수 없음