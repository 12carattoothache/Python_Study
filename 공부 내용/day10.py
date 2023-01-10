'''
5. 제어문 - for
5.1 단일 for문
    : 문법
        for 변수 in range(초기값, 끝값, 증감값):
            수행코드(종속문장)
        
        for 변수 in 리스트(문자열 또는 튜플): 
            수행코드1
            수행코드2
            ...
            
5.2 실습

# 1. range(초기값, 끝값, 증감값 유무에 따른 실습)

i = 1101                 # 적용이 안되는 변수 
for i in range(1,10):    # range에 2개가 있으면 (초기값, 끝값, x)이다.
    print("i = %d" % i)  # 끝값은 '끝값-1'이 될때까지만 출력
                         # 변수의 값이 적용이 안 되는 이유: for문에서 변수를 지정했으므로
                         # 그보다 먼저 변수의 값을 지정하더라도 적용이 안 된다.
    
for i in range(10):       # range(x, 끝값, x)
    print("i = %d" % i)   # 초기값이 없는 경우 '0'부터 출력
    
for i in range(10,2):      # range(초기값, 끝값, x)
    print("i = %d" % i)    # 조건에 맞지 않기 때문에 오류(출력x)
    
for i in range(0,10,2):     # range(초기값, 끝값, 증감값)
    print("i = %d" % i)   
     
for i in range(1,10,2):     # range(초기값, 끝값, 증감값)
    print("i = %d" % i)     # 끝값은 '끝값-1'이 될때까지만 출력
  
i = 1101
for i in range(1,11,1): 
    if i % 2 == 0: print("i(OK) : %d" % i)    
    else: print("i(Fail) : %d" % i)
    
# 2. List 
for a in 'one', 'two', 'three':     # 그냥 문자열
    print(a)

for b in 1,2,3:     # 그냥 숫자
    print(b)
    
for c in range(1, 12):
    if c < 11: print("작은 수까지 출력(%d)" % c)
    else: print("크거나 같은 수 출력(%d)"% c)
    
test_list=['one', 'two', 'three']     # 리스트
for a in test_list[:]:                # 슬라이싱(전부 출력)
    print(a)
    
 - 실습 
# 3. 1부터 10까지의 합을 구하는 소스
sum = 0     # 값이 누적되는 경우에는 반드시 누적되는 변수를 초기화 해야 한다.
n = 0
for b in range (1, 11, 1):
    sum += b     # sum = sum + b 라는 뜻이다.  # 즉 b라는 수열의 합을 구하는 변수이다.
    n += 1       # 1이라는 상수 수열의 합을 구하는 변수 설정
    print("a(%d) = %d | s(%d) = (%d)"%(n,b,n,sum))
print("\ns(%d) = %d"%(n,sum))


#4. 1부터 51까지의 숫자를 출력하는데 7의 배수인 경우와 7의 배수가 아닌 경우의 소수 코딩
for b in range(1,52,1):
    if b%7 != 0:
        print("%d는 7의 배수가 아니다." % b)
    else:
        print("%d는 7의 배수이다." % b)
        
#5. 누적에 따른 합산(값(3가지 요소)을 입력해서 합산을 하는 소스)
sum = 0  
sum = 0
a1 = int(input("시작값 입력 : "))
a2 = int(input("끝값 입력 : "))
a3 = int(input("증감값 입력 : "))
for b in range(a1,a2,a3):
    sum += b
    print("b는 %d, 총 합계는 %d" % (b,sum))      # 위의 연산 식과 들여쓰기를 맞추면 진행상황까지,
print("\n총 합계 = %d" % sum)                    # 왼쪽 정렬을 하면 최종결과만 출력된다.
     
#6. 임의의 값을 입력받은 후 0부터 입력받은 값까지 단계별 출력과 합계를 구하는 소스
sum=0
n = 0
a = int(input("값을 입력하세요 : "))
for b in range(a+1):      # 하나만 입력하면 끝값. 이때 시작값은 0, 증감값은 1.
    sum += b
    n += 1
    print("a(%d) = %d | S(%d) = %d" %(n,b,n,sum))
print("\nS(%d)= %d" % (n,sum))

a = [(1,2),(3,4),(5,6)]      # 리스트 안에 튜플이 정의
for (samadal,madal) in a:
    print("%d+%d = %d" % (samadal,madal,(samadal + madal)))
    
# 7. 다음의 값이 주어졌을 때 합격, 불합격 여부를 출력하는 소스
     : 60점 미만인 학생을 '불합격'을, 이 이외에는 모두 '합격'을 출력
     : 주어진 값(95, 25, 67, 45, 80)

b= (95, 25, 67, 45, 80)
num = 0
for a in b:
    num += 1
    if a<60:
        print("%d번 학생은 %d점이므로 불합격입니다." % (num, a))
    else:
        print("%d번 학생은 %d점이므로 합격입니다." % (num, a))

- 실습: 위의 예시를 그대로 사용하되 점수를 입력받아 학생의 합격, 불합격을 출력하는 소스
num = 0
a1=int(input("1번 학생의 점수 : "))
a2=int(input("2번 학생의 점수 : "))
a3=int(input("3번 학생의 점수 : "))
a4=int(input("4번 학생의 점수 : "))
a5=int(input("5번 학생의 점수 : "))
a6=int(input("6번 학생의 점수 : "))

list = [a1,a2,a3,a4,a5,a6]    # 튜플과 리스트 모두 가능
for i in list:
      num += 1 
      if i >= 60:
            print("%d번 학생은 %d점이므로 합격입니다." % (num,i))
      else:
            print("%d번 학생은 %d점이므로 불합격입니다." % (num,i))

# 8. A학급에 총 10명의 학생이 있고 이 학생들의 중간고사 점수는 다음과 같다.
    : 이 학생들의 평균 점수를 구한다.
    : 주어진 값(70,60,55,75,95,90,80,85,100)
        
list = [70,60,55,75,95,90,80,85,100]
sum = 0
for i in list:
    sum += i
    print("학생 1의 점수(%d), 누적 합계(%d)" % (i, sum))
a= sum/10 
print(a)
print("총 합계(%d), 평균(%d)" % (sum, a))

# 9. 하단의 리스트 중에서 홀수에만 2를 곱하고 출력하는 소스
     : 주어진 값[1,2,3,4,5]
'''
a=[1,2,3,4,5]
result = []
for i in a:
    if i % 2 ==1:
        result.append(i * 2)
print(result)



      