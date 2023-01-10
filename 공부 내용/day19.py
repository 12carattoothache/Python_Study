'''
8. Class
8.4 클래스의 인자값 'self'
    - 특징
        : 클래스 밖에서 값을 받아들일 때는 'self'인자를 사용한다.(옵션)
        : self 사용할 때의 두 가지 유형
            1. 외부서 받아들인 값을 그대로 사용할 경우(메서드 안에만 'self'를 입력)
                class Fourcal:
                    def samadal(self,a,b):    # 외부에서 값(a,b)을 가져올 때
            2. 변수로 치환해서 사용할 경우(모든 변수에 'self'를 입력)
                class samadal(self,a,b):
                    self.a=a
                    self.b=b
                    return self.a + self.b

    - 실습    
 
class FC1:                # 2. 외부에서 받아들인 값을 그대로 사용
    def samadal(self):
        self.madal=0     # 이 구문은 소스 실행에 영향을 주지 못한다.
    def sum(self,a,b):
        self.sums = a+b
        return self.sums
    def sub(self,a,b):
        subs = a-b
        return subs
    def mul(self,a,b):
        muls = a*b
        return muls
    def div(self,a,b):
        self.divs = a/b
        return self.divs  
cal = FC1()      
num1,num2 = int(input("숫자 1 : ")), int(input("숫자 2 : "))  
a=cal.sum(num1,num2)
b=cal.sub(num1,num2)
c=cal.mul(num1,num2)
d=cal.div(num1,num2)
print(a)
print(b)
print(c)
print(d)

class FC2:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def 
    
8.5 클래스의 기타 특성(pass)
    - 실습

class Samadal:
    pass         # '수행할 내용이 없다'는 것을 말한다.      
a= Samadal()     # <__main__.Samadal object at 0x000001ABEAE4A650>
print(a)         # 문법상 오류는 아니지만 처리할 수 있는 객체(함수)가 없다.
print(type(a))   # <class '__main__.Samadal'>

8.6 클래스의 전반적인 내용을 이용한 예제(실제 많이 사용하는 유형)
    - 함수만 사용한 경우와 클래스를 사용한 경우의 비교
    - 클래스의 메서드로 대입되는 값의 유형을 알 수 없는 경우
    - 클래스의 메서드에 조건문이 있는 경우
    - 클래스 생성 시 맨 처음에 선언하는 초기자 메서드를 사용한 경우
    
    - 실습
        : 다음의 내용을 '일반식, 함수식(2가지), 클래스식(2가지)로 표현
        : 1. '내 이름은 '사마달'이고 전화번호는 '010-1234-5678'입니다...'
        : 2. 구구단 중에서 5단만 출력하는 소스
        : 3. 구구단 전체를 출력하는 소스 

odan = 5
def sam1():
    sam2()    # 이중함수를 사용
def sam2():
    for i in range(1,10):
        print("%d * %d = %d" % (odan, i ,odan*i))
sam1()

class Dan:
    def sam1(self,oh):
        self.oh=oh
    def sam2(self):
        for i in range(1,10):
            print("%d * %d = %d" % (oh,i,oh*i))
oh = int(input("단 입력 : "))
a=Dan()
a.sam2()
'''
for i in range(1,10):
    for j in range(1,10):
        print("%d * %d = %d" % (i,j,i*j), end='\t')
    print() 