'''
7. 함수
7.7 실습
    - 구구단을 3가지 방법(함수 미사용, 단일 함수 사용, 이중 함수 사용)으로 구현
    
for i in range(1,10,1):
    for j in range(1,10,1):
        print(i,'x',j,'=',i*j)         
# 가로줄 출력

for i1 in range(1,10,1):
        for i2 in range(1,10,1):
            print(i2,'x',i1,'=',i1*i2,end='\t')

def post():      
        for i1 in range(1,10,1):
            for i2 in range(1,10,1):
                print(i2,'x',i1,'=',i1*i2,end='\t')
            print("")
def malone(a,b):
    sum = a * b
    return sum
post()


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
    else:       
        print("입력받은 돈은 %d원이므로 돈을 다시 돌려주고 커피를 안 줍니다." % money)
        print("남은 커피 수량은 %d잔입니다.\n" % coffee)
    if not coffee:
        print("준비된 10잔의 커피는 모두 소진되었습니다.\n판매를 중지합니다.")
        break   # break는 while문에서만 사용.
   
   
   - 윤년을 3가지 방법(함수 미사용, 단일 함수 사용, 이중 함수 사용)으로 구현 

# 함수 미사용
year = int(input("값을 입력하세요 : "))    
if year%4==0:                             
      if year%100==0:
            if year%400==0: print("%d년은 윤년입니다." % (year))
            else: print("%d년은 평년입니다." % (year))
      else: print("%d년은 윤년입니다." % (year))
else : print("%d년은 평년입니다." % (year))

# 단일 함수 사용
def post(year):
    if year%4==0:                             
        if year%100==0:
            if year%400==0: print("%d년은 윤년입니다." % (year))
            else: print("%d년은 평년입니다." % (year))
        else: print("%d년은 윤년입니다." % (year))
    else : print("%d년은 평년입니다." % (year))
a= int(input("값을 입력하세요 : "))
post(a)

:(1) 4의 배수인 경우는 윤년이고 그 이외는 모두 평년  
:(2) 4의 배수 중, 4의 배수이면서 100의 배수인 경우는 평년이고 그 이외는 모두 윤년이다.
:(3) 4와 100의 배수 중, 400의 배수인 경우는 윤년, 그 이외는 모두 평년

# 이중 함수 사용

#(1)
def pm1(year):
    if year%4==0:
        pm2(year)
    else: return "%d년은 평년입니다." % (year)
#(2)
def pm2(year):
    if year%100==0:
        pm3(year)
    else: return "%d년은 윤년입니다." % (year)
#(3)
def pm3(year):
    if year%400==0: print("%d년은 윤년입니다." % (year))
    else: return "%d년은 평년입니다." % (year)
    '''


        
    
    
 
       



        




 
