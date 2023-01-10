'''
7. 함수
7.4 이중함수(매우 중요)
    - 단순하게 함수를 여러 개 나열하는 것이 아니라 함수 안에 또 다른 함수를
    호출하는 것을 말한다.  

def display():
    num = int(input("1_기본급 | 2_일 한 일수 : "))
    if num == 1: 
        result1 = alba()    # 함수 안에 또다른 함수를 호출
    elif num == 2:
        day = int(input("몇 일 동안 일 했냐? : "))
        result1 = alba(day)    # 함수 안에 또다른 함수를 호출
    print("당신의 급여는 %d원입니다." % result1)
    
def alba(day = 30, time = 8, pay=9160): 
    result2 = day * time * pay
    return result2
display()

    - 이중함수를 이용한 사칙연산
    
num1,num2=int(input("값 1 : ")),int(input("값 1 : "))
a=input("부호 : ")

def cal1(x,y):
    return (x+y)
def cal2(x,y):
    return (x-y)
def cal3(x,y):
    return (x*y)
def cal4(x,y):
    return (x/y)

def cal(k):
    if k =='+':
        result1 = cal1(num1,num2)
    elif k =='-':
        result1 = cal2(num1,num2)
    elif k =='*':
        result1 = cal3(num1,num2)
    elif k =='/':
        result1 = cal4(num1,num2)
    else:
        result1 = "다시 입력해세요."
    return result1

print("%d %s %d = %.0f" % (num1,a,num2,cal( a)))


7.5 기타

    - 매개변수에 초기값 저장 
def say_samadal(name,old,man=False):     # 이름과 나이는 함수 밖에서 받아서 처리, man은 함수 내에서 처리
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:    # 'man이라는 변수에 값이 있다면' 이라는 뜻이다. 
        print("Female")    # True는 값이지만 False는 아니다.
    else:
        print("Male")      
say_samadal("사마달",20)

    
    - 지역변수와 전역변수
a=2           # 함수 밖에 선언된 변수(전역변수, 소스 전반에 걸쳐 영향을 주는 변수)
def vartest(a):
    a=4       # 함수 안에 선언된 변수(지역 변수, 함수 안에서만 영향을 주는 변수)
    a=a+1     # 전역변수보다 지역변수가 우선한다.
    return a
b = vartest(a)
print(b)
# 전역변수 a와 지역변수 a는 다른 변수이다. 위의 예시를 아래처럼 이해하면 쉽다.

c=2  
def vartest(a):
    a=4       
    a=a+1     
    return a
b = vartest(c)   
print(b)
# 전역변수 c에 2가 들어가므로 2가 지역변수 a의 역할을 한다고 보면된다.
#  아래의 예시처럼 이해하자.

def vartest(a):
    a=4       
    a=a+1     
    return a
b = vartest(2)
print(b)


    - 키워드 파라미터(**kwargs)   
def print_kwargs(**kwargs):   # 변수명 갯수와 무관하게 입력받은 내용 모두 출력
    print(kwargs)
print_kwargs(name='samadal', age=3)   # 딕셔너리로 출력

      
    - 함수의 결과값(함수값)은 반드시 한 개만 존재
def add_and_mul(a,b):   
    ab = a+b
    ba = b*a
    print(type(ab))
    print(type(ba))
    return ab,ba
print(add_and_mul(3,4))  # 함수 호출과 출력을 동시에 하므로 수행문장의 결과와 return값을 동시에 출력
# 함수값은 반드시 하나여야 하므로 두 값을 튜플로 묶어서 하나의 값으로 출력


    - Lambda
        : 함수와 동일한 역할을 수행한다.
        : 매개변수를 이용한 표현식을 사용한다.
        : return문은 사용할 수 없다.
        : 표현식
            lambda 매개변수1, 매개변수2, .... : 계산식

x,y = 3,4
def sum1(a,b):   # 매개변수
    return a + b
print(sum1(x,y))

sum2 = lambda a,b: a+b    # 매개변수
print(sum2(x,y))
# print(lambda x,y : x+y)    출력은 되지만 값은 나오지 않는다. 


def num(a,b):
    sum=a+b
    avg=sum/2
    return avg
print(num(3,4))

def num(*args):
    sum=0
    for i in args:
        sum+= i
    avg= sum/len(args)     # args의 원소 개수가 몇 개인지 모르므로 len()함수 사용
    return avg
print(num(3,4,5,6,7))
'''
a,b,c,d,e=3,4,5,6,7
samadal= lambda a,b,c,d,e:(a+b+c+d+e)/5
print(samadal(3,4,5,6,7))

