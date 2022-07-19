s="i like Python"

print(s.upper()) #대문자
print(s.lower()) #소문자
print(s.swapcase())#대문자<->소문자
print(s.capitalize()) #첫글자만 대문자로 변환
print(s.title()) #단어의 첫글자만 대문자로 변환
print(s*3)
print(s+s)


#검색관련
s = 'I Like Phyton. I Like Java Also'

print(s.find("Like"))
print(s.find("Like", 5))
print(s.find("Like", 5, 40))

print(s.find("JS"))

print(s.rfind('Like'))      #마지막 인덱스를 찾아줌
#print(s.lfind('Like'))

print(s.startswith('I Like'))
print(s.startswith('Like', 2))
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))
