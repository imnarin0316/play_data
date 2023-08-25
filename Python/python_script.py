# 파이썬 코드를 실행하는 방법

#1. python script 파일 => 파이썬 실행파일

def plus(n1, n2):
    print("덧셈을 실행")
    return n1 + n2

a = 10
b = 20
c = int(input("정수 : "))
print(a + b + c)
r1 = plus(a,b)
r2 = plus(b,c)
r3 = plus(a,c)

print(r1,r2,r3)