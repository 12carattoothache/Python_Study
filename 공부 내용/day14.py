'''
7. 함수
7.3 실습
   - 다음의 주어진 값을 각각 10진수로 표현하는 값을 함수로 표현
       : 주어진 값(0o177,0x8ff,0xABC,0b11011011)
       : 개별적인 함수로 표현해야 하고 출력문은 반드시 함수 밖에서 표현

a,b,c,d=0o177,0x8ff,0xABC,0b11011011
print("%d" % a)
print("%d" % b)
print("%d" % c)
print("%d" % d)

a,b,c,d=0o177,0x8ff,0xABC,0b11011011
def post(a,b,c,d):
    print("%d" % a)
    print("%d" % b)
    print("%d" % c)
    print("%d" % d)
post(a,b,c,d)

def bin(): 
    a=0b11011011   
    return a
def oct(b):
    bb = int(b)
    return bb
def hexa1():
    c= 0x8ff
    return int(c)
def hexa2(k):
    dd = ("%d" % k)
    return dd
aa= bin()
print("2진수 a를 10진수로 표현(%d)" % aa)
b=0o177
print("8진수 b를 10진수로 표현(%d)" % oct(b))
c= hexa1()
d=0xABC
ddd=int(hexa2(d))    # 함수의 내용이 %문자열이므로 정수형으로 변환
print("16잔수 c(%x) 와 d(%x)를 10진수로 표현(%d,%d)"%(c,ddd,c,ddd))


7.3 실습
    - 홍길동씨의 과목별 점수는 다음과 같다고 할 때 합계와 평균을 함수로 표현
    : 주어진 값(국어/85.5, 영어/79.3, 수학/95.4)

def post():
    국어 = 85.5
    수학 = 79.3
    영어 = 95.4
    a= 국어+수학+영어
    b= a/3
    print("합계 = %.1f" % a)
    print("평균 = %.d" % (b))
post()

def post(a,b,c):
    d=a+b+c
    return d
def malone(h):
    return h/3
a1,a2,a3= 85.5,79.3,95.4
pm3=post(a1,a2,a3)
pm4=malone(pm3)
print("합계(%.1f), 평균(%.1f)" % (pm3, pm4))


x, y = 15, 10
if x>y:
    print("x(%d)는 y(%d)보다 크다" % (x,y))

def x(a):
    return a
def y(b):
    return b
a, b = 15,10
aa,bb=x(a), y(b)
if aa>bb:
    print("x(%d)는 y(%d)보다 크다." % (aa,bb))
    
def x(a):
    return a
def y(b):
    return b
h=int(input("h = "))
i=int(input("i = "))
aa,bb=x(h), y(i)
if aa>bb:
    print("x(%d)는 y(%d)보다 크다." % (aa,bb))

a= 15
if a > 10 or a != 15:
    print("True")
else:
    print("False")

def post(a):
    if a < 10 or a != 15:
        return True
    else: return False
x=int(input("값을 입력 : "))
y=post(x)
print("결과 : {}".format(y))
print(type(y))   # 함숫값의 유형은 bool 대수이다. (참 or 거짓)

def post():
    madal = "KG It Bank Samadal"
    string = input("찾고자 하는 문자열 : ")
    if string in madal:
        print("찾는 문자열 %s는 있다." % string)
    else:
        print("찾는 문자열 %s는 없다." % string)
post()

def post(string):
    madal = "KG It Bank Samadal"
    if string in madal:
        print("찾는 문자열 %s는 있다." % string)
    else:
        print("찾는 문자열 %s는 없다." % string)
string1 = input("찾고자 하는 문자열 : ")
post(string1)

pm = "kg it bank"
pm4= input("문자열 입력해라 : ")
def malone(post):
    if post in pm:
        return True
    else:
        return False
a=malone(pm4)
if a is True:
    print("찾는 문자열 %s는 '%s'에 있다."%(pm4,pm))
else:
    print("찾는 문자열 %s는 '%s'에 없다."%(pm4,pm))
    

- 2개의 정수값을 입력 받고 비교한 후 큰 값과 작은 값을 출력
    : print()문의 경우 소스의 내용에 따라서 결과가 다르게 나올 수 잇다.
    : 따라서 가급적 함수 안에 넣지 않는 것이 좋다.
    : 즉, 함수 안에는 변동이 없는 등이 내용으로 구성하는 것이 좋다. (상수 형태)
    : 그러나 조건식에 따라 함수 안에 출력문을 포함하는 것이 코딩에 유리한 경우도 있다.
    : 예를 들어 이 소스의 경우가 그렇다.
      
num1 = int(input("정수를 입력하세요 : "))
num2 = int(input("정수를 입력하세요 : "))
def post(a,b):
    if a>b:
        print("%d는 %d보다 크다" % (a,b))
    elif a<b:             # else를 사용하는 3개 이상의 조건문은 꼭 if 다음에 elif를 사용
        print("%d는 %d보다 크다" % (b,a))
    else:
        print("두 수는 같다")
post(num1,num2)    

num1 = int(input("정수를 입력하세요 : "))
num2 = int(input("정수를 입력하세요 : "))
def post1(a,b):
    if a>b:
        return True
    else:
        return False
def post2(a,b):
    if a<b:
        return True
    else:
        return False
def post3(a,b):
    if a==b:
        return True
    else:
        return False
if post1(num1,num2) is True: print("큰 수 : %d | 작은 수 : %d" % (num1,num2))
if post2(num1,num2) is True: print("큰 수 : %d | 작은 수 : %d" % (num2,num1))
if post3(num1,num2) is True: print("%d와 %d는 크기가 같다." % (num1,num2))

def compare(a,b):
    if a>b : return "큰 값 : %d, 작은 값 : %d" % (a,b)
    elif a<b : return "큰 값 : %d, 작은 값 : %d" % (b,a)
    else : return "두 값은 동일하다" 
a,b= int(input("값 1 : ")), int(input("값 2 : "))
print(compare(a,b))
# return을 마치 print처럼 사용.


    - 받아들인 값(기호)에 따라 사칙연산을 하는 소스
    
a,b= int(input("야 입력해 wwww : ")), int(input("야 입력해 wwww : "))
c = input("기호를 입력 : ")
def post(x,y,z):
    if z == '+':
        print("%d" % (x+y))
    elif z == '-':
        print("%d" % (x-y))
    elif z == '*':
        print("%d" % (x*y))
    elif z == '/':
        print("%d" % (x/y)) 
    else: print("다시 입력해 wwww") 
post(a,b,c)  

a,b= int(input("야 입력해 wwww : ")), int(input("야 입력해 wwww : "))
c = input("기호를 입력 : ")
def pm1(x,y,z):
    if z == '+':
        print("%d" % (x+y))
def pm2(x,y,z):
    if z == '-':
        print("%d" % (x-y))
def pm3(x,y,z):        
    if z == '*':
        print("%d" % (x*y))
def pm4(x,y,z):
    if z == '/':
        print("%d" % (x/y)) 
pm1(a,b,c)
pm2(a,b,c)
pm3(a,b,c)
pm4(a,b,c)

a,b= int(input("야 입력해 wwww : ")), int(input("야 입력해 wwww : "))
c = input("기호를 입력 : ")
def pm1(x,y,z):
    if z == '+':
        return "%d %s %d = %d" % (x,z,y,(x+y))
def pm2(x,y,z):
    if z == '-': 
        return "%d %s %d = %d" % (x,z,y,(x-y))
def pm3(x,y,z):        
    if z == '*':
        return "{} {} {} = {}" .format(x,z,y,(x*y))
def pm4(x,y,z):
    if z == '/':
        return "%d %s %d = %d" % (x,z,y,(x/y))
a1=pm1(a,b,c)
a2=pm2(a,b,c)
a3=pm3(a,b,c)
a4=pm4(a,b,c)
if c == '+' : print(a1)
if c == '-' : print(a2)
if c == '*' : print(a3)
if c == '/' : print(a4)


select = 0   # 소스에 전혀 영향을 주지 않는다.
select = int(input("1. 콜라 | 2. 사이다 | 3. 환타 : "))
if select == 1: print("콜라")
elif select == 2: print("사이다")
elif select == 3: print("환타")
else : print("야 이 개 병신새끼야")
'''

def post(select, *args):    
    if select == '+' : return num1+num2
    elif select == '-' : return num1-num2
    elif select == '*' : return num1*num2
    elif select == '/' : return num1/num2
num1,num2= int(input("값 1 : ")), int(input("값 2 : "))
a=input("부호 : ")
b= post(a)
print(b)
# 매개변수에 변수명이 아닌 *args가 들어간 경우 함수 밖의 변수와 안의 변수가 반드시 일치해야 한다.
# 다만 위의 예시에서 부호에 해당하는 매개변수는 'select'로 정의되었으므로,
# 함수 밖의 변수와 매개변수가 일치하지 않아도 된다.




