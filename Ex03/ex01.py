no = 3

if 3==no :
    print("정답")
    print("축하합니다.")
else :
    print("오답")
    print("다시 도전하세요")

    print("종료")

    
'''
if(3 == no) {
    System.out.print("정답")
} else{
    System.out.print("오답")
    System.out.print("다시 도전하세요")
}

System.out.print("종료")
'''


print("숫자를 입력하세요")
num = input("숫자: ")
#print(num, type(num))

num = int(num)


if num > 0 :
    print("양수")
elif num < 0 :
    print("음수")
else :
    print("0")


print("종료")