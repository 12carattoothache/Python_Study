'''
7. 함수
7.1 개요
    - 어떤 내용이 소스 내에서 지속적으로 반복될 경우 소스의 길이가 늘어나게 된다.
    - 이와 같이 반복되는 소스의 내용을 임의의 형태로 묶어두고 필요할 때 불러서 사용하면 된다.
    - 즉, 소스의 형태를 간결하게 할 수 있는 기능이 '함수'이다.
7.2 구조
    - 형식1.    # 수행할 문장이 여러 개
        def 함수명(매개변수):
            <수행할 문장1>
            <수행할 문장2>
            ....
    - 형식2.    # 수행할 문장이 한 개 
        def 함수명(매개변수):
            <수행할 문장>
    - 형식3.    # 입력값이 몇 개인지 모를 때
        def 함수명(*매개변수):
            <수행할 문장>

7.3 실습
# 기본 실습 1(사칙연산)

# 형식 1. 수행할 문장이 여러 개
x, y = 4,2      # 고정변수와 값 설정
# number(a,b)     # 매개변수는 항상 '함수 선언부'보다 하위에 위치해야 한다.
def number(a,b):     # 함수 선언부 : def 함수명(매개변수1,2)
    print(a+b)       # 수행할 문장 1(수행문장의 결과가 함숫값이다.)
    print(a-b)       # 2
    print(a*b)       # 3
    print(a/b)       # 4
number(x,y)     # 함수 호출부(함수값을 출력한다). 이때 고정변수가 매개변수와 달라도 된다.

# 형식 2. 함수가 여러 개, 함수 당 수행 문장 1
x,y = 4,2
def num1(a,b):
    print(a+b)
def num2(a,b):
    print(a+b)
def num3(a,b):
    print(a*b)
def num4(a,b):
    print(a/b)
num1(x,y)
num2(x,y)
num3(x,y)
num4(x,y)

   
x, y = 4,2
def num1(a,b):    # 함수 호출부
    c= a+ b
    return c      # 함수값을 돌려받는 부분
def num2(a,b):
    return a- b
d = num1(x,y)    # (함수를 변수로 치환)
print(d)         # 출력부
print(num1(x,y))   # 출력부
print(num2(x,y))
# 이때 수행문장에 print가 아니라 return이 들어오는 경우
# 함수를 호출만 하면 출력이 되지않는다. 직접 출력문에 함수를 넣어야 한다.

def samadal():      # 입력값이 없는 함수
    return 'madal'  # 입력값이 없기 때문에 이 함수를 호출하면
                    # 리턴값으로 문자열을 반환한다.
a=samadal()         # 함수를 호출하고 결과를 받아와서 변수에 대입
print(a)            # 출력


# 기본 실습 2
a,b=3,4   # 고정변수의 값 설정은 반드시 함수 선언부보다 위
def sum(a,b):   
    c = a + b
    print("%d + %d = %d" % (a,b,c))
sum(a,b)  
# 패턴 1. 수행문장(print)을 작성하고 함수를 호출

def sum(a,b):
    return a+b
a,b =3,4
c= sum(a,b)
print("%d + %d = %d" % (a,b,c))
# 패턴 2. return을 사용해 함숫값을 받고 함수를 직접 출력

 
# 기본 실습 3
- 입력값이 몇 개인지 모를 때

def sum(a,b,c):
    return a+b+c
a,b,c = 3,4,5
print(sum(a,b,c))

def sum(*args):     # 3. 입력받은 값은 기본적으로 값을 받아들이는 인수(변수, Arguments)가 있어야
    sum = 0         # 하는데 인수의 개수와 무관하게 어떤 값이던 받아서 처리할 수 있게 하기
    for i in args:  # 위해 예약어인 'urgs'를 사용한다.
        sum += i    
    return sum
a,b,c = 3,4,5     # 1. 변수에 값을 입력
d = sum(a,b,c)   # 2. 입력받은 3개의 값을 받아서 처리할 함수 호출
print(d)

a= "kgItBank 2022121"
b,c,d,e=a[:8],a[-7:-3],a[-3],a[-2:]
print("%s %s년 %s월 %s일" % (b,c,d,e))
# 함수로 소스를 만들고 싶을 때 함수가 없는 형태로 먼저 만들고 함수를 추가하자.


# 1. 프린트 수행문장, 함수 호출
a= "kgItBank 2022121"
b,c,d,e=a[:8],a[-7:-3],a[-3],a[-2:]
def sum(b,c,d,e):
    print("%s %s년 %s월 %s일" % (b,c,d,e))
sum(b,c,d,e)

def post(a):
    b,c,d,e=a[:8],a[-7:-3],a[-3],a[-2:]
    print("%s %s년 %s월 %s일" % (b,c,d,e))
s = "kgItBank 2022121"
post(s)

# 2. return, 함수 직접 출력
def sum(b,c,d,e):
    return "%s %s년 %s월 %s일" % (b,c,d,e)
a= "kgItBank 2022121"
b,c,d,e=a[:8],a[-7:-3],a[-3],a[-2:]
k = sum(b,c,d,e)
print(k)

#3.(의미 x)
def sum():
    a= "kgItBank 2022121"
    b,c,d,e=a[:8],a[-7:-3],a[-3],a[-2:]
    print("%s %s년 %s월 %s일" % (b,c,d,e))
sum()

# 실습
   - 임의의 값을 받아들인 후 10으로 나눴을 때 몫과 나머지를 구하는 소스
 
b=int(input("값을 입력하세요 : "))
while True:     # 무한루프
    a1 = b//10
    a2 = b%10
    print("입력값(%d), 몫(%d), 나머지(%d)" % (b,a1,a2))
    # if not b :    # b가 값이 있으므로 if절 추가하면 정지 불가
    break    # 무한루프 정지
print("프로그램 종료")

def madal():
    b=int(input("값을 입력하세요 : "))
    while True:     # 무한루프
        a1 = b//10
        a2 = b%10
        print("입력값(%d), 몫(%d), 나머지(%d)" % (b,a1,a2))
        break    # 무한루프 정지
madal()
print("프로그램을 종료합니다.")

k=int(input("값을 입력하세요 : "))
def madal(b):
    while True:  
        a1=b//10
        print("입력값(%d), 몫(%d)" % (b,a1))
        a2=b%10
        print("입력값(%d), 나머지(%d)" % (b,a2))
        break
madal(k)
print("프로그램을 종료합니다.")
'''

def malone():     # 2. 인수가 없으므로 함수 안에 있는
    a = int(input("값을 입력하세요 : "))   # 3. 함수 안의 내용의 결과를
    return a      # 4. 호출한 곳으로 리턴.
num = malone()    # 1. 함수를 호출하고 결과값을 변수로 치환
b1= num//10       # 5. 받아온 값을 조건에 맞게 처리
b2= num%10
print("입력값(%d), 몫(%d), 나머지(%d)" % (num,b1,b2))  
# 6. 처리한 결과를 출력
      
     

