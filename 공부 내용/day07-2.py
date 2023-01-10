'''
3. 변수(Variable)
3.1  고정변수
# 고정 변수는 값이 고정되어있는 변수를 말한다.
     - ':'을 이용한 변수 생성
a=[1,2,3]
b=a[:]
print(a)
print(b)
     
      - copy를 이용한 변수 생성
a=[1,2,3]
from copy import copy    # copy를 Module 안에 있는 copy()함수를 호출
print(copy(a))

3.2 가변 변수 : '변수명 = input()'  (매우 중요)
# 가변 변수는 값이 정해지지 않은 변수이다. 즉, 값을 입력해야 한다.
var = input("값을 입력하세요 : ")
print("{}을 입력 받았다." .format(var))
print(type(var))     # input()함수로 입력된 모든 값은 항상 '문자열'이다.
                     # 1을 입력했으나 변수의 타입은 int이 아니라 str.
print("%s을 입력 받았다." % var)
print(f"{var}을 입력 받았다.")

var1 = input("문자열 입력 : ")    # input()함수로 입력된 모든 값은 항상 '문자열'이다.
var2 = input("정수 입력 : ")
print("%s" % var1)
print("{}" .format(var2))
print(type(var1),type(var2))

- 실습: 두 개의 정수값을 받아서 사칙연산을 한다
'''
var1=int(input("값1 : "))
var2=int(input("값2 : "))
print("%d + %d = %d" %(var1, var2, var1+var2))

   
