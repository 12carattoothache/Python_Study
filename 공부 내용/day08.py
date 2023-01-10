'''
3. 변수(Variable)
3.2 가변 변수 : "변수명 = input()" (매우 중요)

     - 실습(홍길동씨의 과목(3과목)별 점수를 입력받은 후 합계와 평균(소수 첫째자리)을 구하는 소스)
var1 = input("국어 : ")
var2 = input("영어 : ")
var3 = input("수학 : ")
var123 = int(var1) + int(var2) + int(var3)     # cast 연산을 통해 str을 int로
print(var123)
varavg = var123/3
print(type(var1))
print("국어(%d), 영어(%d),수학(%d),합계(%d),평균(%.1f)"%(var1,var2,var3,var123,varavg))
# cast 연산은 그 순간 type을 바꾸는 것이지 영구적이지 x.
# 따라서 var123과 varavg는 int이지만 var1,2,3는 str.  

- 실습(다음의 변수에 저장되어 있는 값을 활용해서 동일한 결과가 나오게 하는 소스) 
    : 저장되어 있는 값. x,y,z='100',10.5,20
    : 출력 결과 
          결과 1 : 110.5
          결과 2 : 10020
          결과 3 : 10.520
          결과 4 : 110.520

내 답안
x,y,z='100',10.5,20   # 문자열은 더하면 문자열끼리 붙고, 
post = int(x)         #  실수(정수형)는 더하면 실수끼리 연산된다.
print(post+y)
pm4=post+y
malone = str(z)
print(x+malone)
pm=str(y)
print(pm+malone)
pm3=str(pm4)
print(pm3+malone)

선생님 답안
x,y,z='100',10.5,20 
print("결과 1 : %.1f" % (int(x)+y))
print("결과 2 : %s" % (x + str(z)))
print("결과 3 : %s" % (str(y) + str(z)))
print("결과 4 : %.3f" % (float(x)+y+z*0.001))

4. 제어문 - if
4.1 개요
   - 조건식이 참이면 실행할 문장이 처리되고 거짓이면 아무것도 실행하지 않고 프로그램 종료
4.2 단일 if문(if)
   - 문법
     if 조건문:
         수행할 문장1
         수행할 문장2
         ....
    - 주의사항    
      : 들여쓰기, 내어쓰기에 따른 오류 분석에 신경쓰드록 한다. 
      
    - 실습(주의사항)   
kgitbank = True 
if kgitbank:
    print('Samadal')
    print('madal')
    print('dals')
    
     - 실습
x,y=15,10       # 매개 변수
if x>y:
    print("15는 10보다 크다.")
    print("%d는 %d보다 크다." % (x,y))
    print("{}는 {}보다 크다." .format(x,y))
    print(f"{x}는 {y}보다 크다.")
    
    - 실습
x = 15        # 매개 변수
if x in (10,11,15):
    print("입력받은 값과 비교값(%d)는 동일하다." % x)
y = type(x) is int
if y:  
      print("정수(Integer)", type(x))
      
4.3 단일 if문(if ~ else)
   - 문법
     if 조건문:
        수행할 문장1
        수행할 문장2
        .....
     else:
        수행할 문장A
        수행할 문장B
        
    - 실습             
x=15
if x > 10 and x != 15:     # 'and'는 두 개의 조건식이 모두 만족했을 때만 참
    print("True")          # '!='는 같지 않다는 것을 말한다.
else:
    print("False")
    
if x > 10 and x == 15:     # '=='는 같다는 뜻이다(등호).
    print("True")          # 등호를 '='라고 착각하여 사용하지 말자.       
else:
    print("False")
    
if x > 10 or x != 15:      # 'or'는 둘 중 하나만 참이어도 참
    print("True")
else:
    print("False")

    -  실습  
money = 4000
card = False
if money >= 4000 or card:
    print("집에 갈 수 있다.")
else:
    print("신문지가 필요해!")
        
lotto_number = 23
lucky_list = [1, 9, 23, 46]       # List, 튜플도 가능 - (1, 9, 23, 46)
if lotto_number in lucky_list:
    print("세계여행")
else: 
    print("방콕")
     
    - 실습: 위의 예제에서 값을 받아들인 후 출력하도록 코딩
         : if문만 있는 경우
         : if ~ else문이 있는 경우 
lotto_number = int(input("값을 입력하세요 : "))
lucky_list = (1, 9, 23, 46)     
if lotto_number in lucky_list:
    print("세계여행")

lotto_number = int(input("값을 입력하세요 : "))
lucky_list = [1, 9, 23, 46]     
if lotto_number in lucky_list:
    print("세계여행")
else: 
    print("방콕")
     
    - 실습
       : 받아들인 값이 홀수인지 짝수인지를 비교하는 소스
num = int(input("값을 입력 : "))
if num % 2 == 0:
    print("짝수")
else: 
    print("홀수")
    
    - 실습
        : 두 개의 정수를 입력받은 후 또 입력받은 기호에 따른 사칙연산
num1, num2 = int(input("num1 = ")), int(input("num2 = "))
post = input("기호를 입력 : ")
if post == '+':
    print("%d" % (num1 + num2))
if post == '-':
    print("%d" % (num1 - num2))
if post == '*':
    print("%d" % (num1 * num2))
if post == '/':
    print("%d" % (num1 / num2))
else:
    print("다시 입력하시오.")

num1, num2 = int(input("num1 = ")), int(input("num2 = "))
post = input("기호를 입력 : ")
list = ['+','-','*','/']
if post == '+' in list:
    print("%d" % (num1+num2))
if post == '-' in list:
    print("%d" % (num1-num2))
if post == '*' in list:
    print("%d" % (num1*num2))
if post == '/' in list:
    print("%d" % (num1/num2))
else:
    print("다시 입력하시오.")

- 실습 : 두 개의 정수를 입력받고 크기를 비교하는 소스 
num1, num2 = int(input("num1 = ")), int(input("num2 = "))    
if num1 > num2:
    print("%d는 %d보다 크다" % (num1, num2))
else:
    print("%d는 %d보다 크거나 같다" % (num1, num2)) 

- 실습 : 두 개의 정수를 입력받고 비교한 후 '큰 값'과 '작은 값'을 출력
    '''
num1=int(input("숫자를 입력하세요 : "))
num2=int(input("숫자를 입력하세요 : "))
if num1!=num2:
    if num1>num2:
        print("큰 값은 %d\n작은 값은 %d" % (num1, num2))
    if num2>num1:
        print("큰 값은 %d\n작은 값은 %d" % (num2, num1))
else: 
    print("%d = %d"% (num1, num2))