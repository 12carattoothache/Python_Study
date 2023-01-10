'''
5. 제어문 - for
5.2 다중 for문
     : 문법
        for 변수 in range(초기값1, 끝값1, 증감값1)
            수행코드(종속문장)
            for 변수 in 리스트(초기값2, 끝값2, 증감값2)
                수행코드1
                수행코드2
                ...
    
    : 실습(구구단)            

for i in range(1,10,1):
    for j in range(1,10,1):
        print("%d*%d=%d"%(i, j, i*j))
    print("\n")

for i in range(1,10,1):
    for j in range(2,10,1):
        print(i,'x',j,'=',i*j,end='\t')         
# 가로줄 출력

print("\n")
for i in range(1,10,1):
    for j in range(2,10,1):
        print(j,'x',i,'=',i*j,end='\t')
# 세로줄 출력
    
a= int(input("입력 : "))  
for i in range(a, a+1):
    for j in range(1,10):
        print("%d * %d = %d" % (i, j, i*j))
# 입력된 수에 해당되는 값만 출력
          
6. 제어문 - while
6.1 개요
    - 프로그램 실행 후 종속 문자 등의 실행을 계속 진행할 수 있도록 한다.
    - 조건문이 부정확할 경우 무한루트에 빠지기 쉽다. (무한 루프 종료: ctr1 + c)
6.2 문법
        while <조건문> :
            <수행할 문장1>
            <수행할 문장2>
            ...
6.3 실습

while True:       # 무한루프에서 빠져나오기
    print("^난^")

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍엇다." % treeHit) 
    if treeHit == 10:
        print("끝")      

number = 0
prompt = "1_Add | 2_Del | 3_List | 4_Quit | 5_Name : "  
while number != 4:
    number = int(input(prompt))
    if number == 4:   
        break      # 종료 기호이다.
        
coffee, money = 5, 300
while money:     # 'money라는 변수가 값을 가지고 있다면' 이라는 뜻 
    print("커피 한 잔을 뽑습니다.")
    coffee -= 1  # 한 잔을 뽑았기 때문에 
    money = money + 300
    print("남은 커피 수량은 %d잔이고 총 금액은 %d입니다." % (coffee , money-300))
    if coffee == 0:
        print("오늘 준비한 수량은 모두 소진되었습니다.\n판매를 중지합니다.")
        break    # 무한 루프 사전 방지.
        
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        print("%d는 짝수이다." %(a))
    else:
        print("%d는 홀수이다."%(a)) 

# 아래 모양을 출력하는 소스 제작.
* 
**
***
****
*****
        
star = 0
while star < 5:
    star += 1
    print('*' * star)   # print('=' * 50) 과 같은 방법으로 생각하면 된다.


- 1부터 100까지의 자연수 중 3의 배수의 합을 구하는 소스
print("a(n)은 수열의 n번째 항, s(n)은 n항까지의 수열의 합")
a = 0
s = 0
n = 0
while a < 99:
    a += 3     
    s += a     # 수열 a(n)을 누적해서 더하는 s(n)
    n += 1
    print("a(%d) = %d, s(%d) = %d" % (n,a,n,s))
print("\ns(%d) = %d" % (n,s))

i,sum,n = 1, 0 ,0
while i <= 100:
    i += 1
    if i % 3 == 0:
        sum += i
        n+= 1
        print("a(%d) = %d, s(%d) = %d"%(n,i,n,sum))

    - 실습
    - 커피 한 잔의 값은 300원이고 오늘 판매할 수량은 10잔이 준비되어 있다,
    - 커피 한 잔을 뽑을 때마다 판매할 수량은 1잔씩 차감되고 입력된 금액은 차감된 금액을
    제하고 거스름돈을 돌려주는 소스
   
coffee , money = 10, 300
while True:
    money = int(input("돈을 넣어 주세요 : "))
    if money == 300:        # 한 잔만 주문
        print("한 잔만 가능한 돈이므로 커피를 줍니다.")
        coffee -= 1
        print("남은 커피 수량은 %d잔입니다.\n" % (coffee))
    elif money > 300:         # 주문하고 거스름돈 돌려받음
        print("거스름돈 %d원을 주고 커피 한 잔을 줍니다." % (money - 300))
        coffee -= 1
        print("남은 커피 수량은 %d잔입니다.\n" % (coffee))
    else:          # 주문할 돈이 부족할 때
        print("입력받은 돈은 %d원이므로 돈을 다시 돌려주고 커피를 안 줍니다." % money)
        print("남은 커피 수량은 %d잔입니다.\n" % coffee)
    if not coffee:    # 커피가 0잔 남음
        print("준비된 10잔의 커피는 모두 소진되었습니다.\n판매를 중지합니다.")
        break
        '''