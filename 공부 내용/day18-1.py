'''
8.Class
8.1 개요
    - 함수와 변수들의 집합체를 말한다.
    - 클래스 안에는 Instance(인스턴스, 객체)를 만들어서 사용할 수 있다.
    - 문법
        class 클래스명:
            [클래스 변수1]
            [클래스 변수2]
            ....
            함수 정의():    # 클래스 안에 있는 함수를 'Method(메서드)'라고 한다.
                내용
8.2 클래스 관련 용어
    - 클래스 멤버
        : 메서드(Method), 클래스 변수(Class Variable), 초기자(Initializer)
        : 인스턴스 변수(Instance Variable), 소멸자(Destructor)
    - 클래스 변수
        : 클래스 안에 존재하고 메서드 밖에 있는 변수를 말한다.
        : 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수를 말한다.
        : 클래스 내부와 외부에서 '클래스명.변수명'으로 접근이 가능하다.
    - 인스턴스 변수
        : 하나의 클래스로부터 여러 객체 인스턴스를 생성해서 사용한다.
        : 클래스 안에 있는 메서드 안에서 사용되면서 'self.변수명'처럼 사용되는 변수를 말한다.
        : 클래스 밖에서는 '객체변수.인스턴스변수'와 같이 접근할 수가 있다.
    - 초기자
        : 클래스로부터 새 객체를 생성할 때마다 실행되는 '__inhit__()'라는 메서드를 말한다.
        : 초기자는 클래스로부터 객체를 만들 때 인스턴스 변수를 초기화 하거나 객체의 초기상태를
         만들기 위한 문장들을 실행하는 곳을 말한다.
    - 메서드 
        : 클래스 안에 정의된 함수를 말한다.
        : 인스턴스 메서드, 정적 메서드, 클래스 메서드 등이 있다.
8.3 실습
    - 클래스 이해하기
    - 클래스 생성
        : 한 개의 클래스 안에 모든 내용 넣기
        : 기본 self와 함께 표현

result1 = 1       # 전역변수
def add1(num):
    result1 = 2      # 지역변수(전역변수에 우선한다.)
    result1+=num
    return result1
print(add1(3))    # 5
print(add1(4))    # 6   전역변수인 result1과 지역변수인 result1이 다르므로
                      # 지역변수인 result1 = 2 만 유효하다. 따라서 값 누적 x
 
result2 = 1      # 전역변수
def add2(num):
    global result2     # 전역변수(함수 안에 정의되어있다고 해서 모두 지역변수인 것은 아님.)
    result2 += num     # 지역변수를 전역변수로 전환.
    return result2
print(add2(3))     # 4
print(add2(4))     # 8    # result2가 전역변수로 선언됨, 따라서 하나의 값으로 통일되어 움직임.
                          # 그래서 값이 누적됨. 

result1=result2=0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2     
    result2 += num
    return result2
print(add1(3))    # 3
print(add1(4))    # 7
print(add2(3))    # 3
print(add2(7))    # 10


class Calculator:
    def __init__(self):       # 초기자 메서드
        self.result = 0       # self(class 안에 정의되는 함수는 무조건 'self'를 맨 앞에서 정의)
    def add(self,num):
        self.result+=num       # self.변수명 -> 인스턴스 변수
        return self.result     # self는 Calculator라는 클래스 자체를 말하며 임의로 변경 가능
cal = Calculator()             # 'Object(객체) = Method()'와 같이 생각하면 된다.
print(cal.add(4))              # 클래스 안에 정의된 함수(메서드)를 사용하겠다.
print(Calculator().add(3))     

class Fourcal1:  
    def madal(self,first,second):
        self.first = first
        self.second = second
    def add(self):    # 인자값 없이 이 메서드를 호출하면 메서드 안에 있는 내용이 실행   
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
fc = Fourcal1()     # 객체(fc)는 클래스의 인스턴스
fc.madal(4,2)     # 클래스의 모든 것을 위임받은 객체(fc)의 Method()에 값을 대입
print(fc.add())
add= fc.add()
print(add)
print(fc.sub())
print(fc.mul())
print(fc.div())
      
class Fourcal2:                   
    def add(self,first,second):    
        self.first=first
        self.second=second
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
fc = Fourcal2()    
add= fc.add(4,2)
print(add)
print(fc.sub())
print(fc.mul())
print(fc.div())

class Fourcal3:
    def __self12___(self):    # 기본 생성자(__init__)만 사용할 경우에는 이렇게 임의로 설정해도 된다.
        self.postmalone=0     # FourCal2라는 클래스 자체(self)를 하위의 함수들이 사용하게 하겠다.            
    def add(self,first,second):     # 이 메서드는 실제 소스에는 영향을 전혀 미치지 않음. 
        self.first=first
        self.second=second
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
fc = Fourcal3()    
add= fc.add(4,2)
print(add)
print(fc.sub())
print(fc.mul())
print(fc.div())


- 실습
    - 한 개의 클래스로 구성되어 있는 소스를 4개의 클래스로 분리해서 코딩

class pm1:
        def post(self,a,b):
            self.a=a
            self.b=b
        def add(self):   
            result1=self.a+self.b
            return result1
fc1= pm1()
fc1.post(4,2)
print(fc1.add())

class pm2:
        def sub(self,a,b):   
            self.a=a
            self.b=b
            result2=self.a-self.b
            return result2
fc2=pm2()
print(fc2.sub(4,2))

class pm3:
        def mul(self,a,b):   
            self.a=a
            self.b=b
            result3=self.a*self.b
            return result3
fc3=pm3()
mul=fc3.mul(4,2)
print(mul)

class pm4:
        def __int__(self):     # 실제 소스 내부에 영향을 주지 않아서 init 대신 int만 써도 됨.
            self.result=0 
        def div(self,a,b):
            # self.a=a     # 변수로 치환하는 과정이 없을 때는 받은 값을 그대로 적용
            # self.b=b
            result4=a/b
            return result4
print(pm4().div(8,4))

class pm4:
        def __int__(self):     # 실제 소스 내부에 영향을 주지 않아서 init 대신 int만 써도 됨.
            self.re=0 
        def div(self,a,b):
            self.a=a
            self.b=b
            result4=self.a/self.b
            return result4
print(pm4().div(8,4))
'''
