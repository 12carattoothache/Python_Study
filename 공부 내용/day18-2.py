'''
    - 문자열(kgItBank2022128)을 일반코드, 함수코드, 클래스코드로 출력하는 소스를 코딩

# 일반 코드
a= "KgItBank2022128"
a1,a2=a[:8],a[8:]
print("%s + %s = %s"%(a1,a2,(a1+a2)))

# 함수 코드 
def malone(c):
    b1=c[:8]
    b2=c[8:]
    return ("%s + %s = %s"%(b1,b2,(b1+b2)))
h=malone(a)
print(h)

# 클래스 코드
a= "KgItBank2022128"
a1,a2=a[:8],a[8:]
class k1:
    def madal(self,x,y):
        self.x,self.y=x,y
    def cd(self):
        return ("%s + %s = %s" % (self.x,self.y,(self.x+self.y)))

a1,a2=a[:8],a[8:]
class k2:
    def pm1(self,x):
        self.x=x
    def pm2(self,y):
        self.y=y
    def post1(self):
        return self.x
    def post2(self):
        return self.y

kg1=k1()
kg1.madal(a1,a2)
print(kg1.cd())

kg2=k2()
kg2.pm1(a1)
kg2.pm2(a2)
print("%s + %s = %s" % (kg2.post1(),kg2.post2(),(kg2.post1()+kg2.post2())))

- 3개의 정수값을 입력받고 비교한 후 가장 큰 값과 가장 작은 값만을 출력

# 일반 코드
a,b,c=int(input("num1 = ")),int(input("num2 = ")),int(input("num3 = "))
if a>b and a>c : print("가장 큰 값은 %d입니다" % a)
elif b>a and b>c : print("가장 큰 값은 %d입니다" % b)
elif c>b and c>a : print("가장 큰 값은 %d입니다" % c)
else: print("두 개 이상의 값이 가장 큽니다.")

if b>a and c>a : print("가장 작은 값은 %d입니다" % a)
elif a>b and c>b : print("가장 작은 값은 %d입니다" % b)
elif b>c and a>c : print("가장 작은 값은 %d입니다" % c)
else: print("두 개 이상의 값이 가장 작네요.")

# 함수 코드
x,y,z=int(input("num1 = ")),int(input("num2 = ")),int(input("num3 = "))
def big(a,b,c):
    if a>b and a>c : print("가장 큰 값은 %d입니다" % a)
    elif b>a and b>c : print("가장 큰 값은 %d입니다" % b)
    elif c>b and c>a : print("가장 큰 값은 %d입니다" % c)
    else: print("두 개 이상의 값이 가장 큽니다.")   
big(x,y,z)

def small(a,b,c):
    if b>a and c>a : print("가장 작은 값은 %d입니다" % a)
    elif a>b and c>b : print("가장 작은 값은 %d입니다" % b)
    elif b>c and a>c : print("가장 작은 값은 %d입니다" % c)
    else: print("두 개 이상의 값이 가장 작네요.")
small(x,y,z)

# 클래스 코드1
x,y,z=int(input("num1 = ")),int(input("num2 = ")),int(input("num3 = "))
class k1:
    def big(self,a,b,c):
        self.a,self.b,self.c=a,b,c
        if self.a>self.b and self.a>self.c : print("가장 큰 값은 %d입니다" % self.a)
        elif self.b>self.a and self.b>self.c : print("가장 큰 값은 %d입니다" % self.b)
        elif self.c>self.b and self.c>self.a : print("가장 큰 값은 %d입니다" % self.c)
        else: print("두 개 이상의 값이 가장 큽니다.")
a1=k1()
a1.big(x,y,z)

class k2:
    def small(self,a,b,c):
        self.a,self.b,self.c=a,b,c
        if self.b>self.a and self.c>self.a : print("가장 작은 값은 %d입니다" % self.a)
        elif self.a>self.b and self.c>self.b : print("가장 작은 값은 %d입니다" % self.b)
        elif self.b>self.c and self.a>self.c : print("가장 작은 값은 %d입니다" % self.c)
        else: print("두 개 이상의 값이 가장 작습니다.")
a2=k2()
k2().small(x,y,z)


    - 1개의 정수값(1~24)을 입력 받고 시간을 출력.

time=int(input("시간을 입력하세요 : "))
if 1 <= time <= 24:
    if time == 12: print('정오')
    elif time == 24: print('자정')
    elif 1 <= time <= 11: print('오전')
    elif 13 <= time <= 23: print('오후')
else: print("제대로 된 값을 입력하세요.")

time=int(input("시간을 입력하세요 : "))
def post(a):
    if 1 <= a <= 24:
        if a == 12: return '정오'
        elif a == 24: return '자정'
        elif 1 <= a <= 11: return '오전'
        elif 13 <= a <= 23: return '오후'
    else: return "제대로 된 값을 입력하세요."
print(post(time))
'''
time=int(input("시간을 입력하세요 : "))
class malone:
    def post(self,a):      # 클래스 안에 정의되어 있는 메서드(함수)의 첫 항목은 무조건 'self'가 와야 한다.
        if 1 <= a <= 24:   
            if a == 12: return '정오'
            elif a == 24: return '자정'
            elif 1 <= a <= 11: return '오전'
            elif 13 <= a <= 23: return '오후'
        else: return "제대로 된 값을 입력하세요."
pm=malone()
b=pm.post(time)
print(b)
print(f"시간이 {time}시이므로 {b}입니다.")

time=int(input("시간을 입력하세요 : "))
class malone:
    def post(self,a):
        self.a=a
    def malone(self):
        if 1 <= self.a <= 24:
            if self.a == 12: return '정오'
            elif self.a == 24: return '자정'
            elif 1 <= self.a <= 11: return '오전'
            elif 13 <= self.a <= 23: return '오후'
        else: return "제대로 된 값을 입력하세요."
pm=malone()
pm.post(time)
b=pm.malone()
print(f"시간이 {time}시이므로 {b}입니다.")