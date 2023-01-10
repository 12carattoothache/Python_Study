'''
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
        break
'''
커피=10
def pm1(money,coffee):
    coffee-=1
    print("한 잔만 가능한 돈이므로 커피를 줍니다." % (money))
    print("남은 커피 수량은 %d잔입니다.\n" % (coffee))

def pm2(money,coffee):
    coffee-=1
    print("거스름돈 %d원을 주고 커피 한 잔을 줍니다." % (money - 300))
    print("남은 커피 수량은 %d잔입니다.\n" % (coffee))

def pm3(money,coffee):
    print("입력받은 돈은 %d원이므로 돈을 다시 돌려주고 커피를 안 줍니다." % money)
    print("남은 커피 수량은 %d잔입니다.\n" % coffee)
    
def pm4():
        print("준비된 10잔의 커피는 모두 소진되었습니다.\n판매를 중지합니다.")
        
a = int(input("돈을 넣어 주세요 : "))
def coffeemachine(money,coffee):
    while True:
        if money==300:
            pm1(money,coffee) 
        elif money>300:
            pm2(money,coffee)
        else:
            pm3(money,coffee)
        if not coffee:
            pm4()
            break
coffeemachine(a,커피)


            
            
            
        
            
            



    
         
    
