'''
    - 실습(한 개의 문자열에 2개의 값이 들어있다. 이를 분리하고 분리된 각 값들에서 
           문자와 숫자를 또 한 번 분리한다.)
           kg = "나이:30, 키:180"

kg = "나이:30, 키:180"
itbank =kg.split(',')  # split으로 나누면 리스트의 형태로 출력된다.
print(itbank)
age=(itbank[0].split(':')[1])   # 출력된 리스트의 인덱싱 *2
height=(itbank[1].split(':')[1])  # 출력된 리스트의 인덱싱 *2
print(age, height)

# if age <= 30 and height >= 180:  # 오류가 발생하는 이유: age와 height는 문자열에서 나누어진 문자열이므로.
    # print("정상적으로 분리가 잘 되었습니다.")
# else:
    # print("소스를 다시 보세요.")

print(type(age), type(height))
if int(age) <= 30 and int(height) >= 180:   # 등식(부등식)에는 문자열이 아닌 정수(실수)가 들어가야 함.
    print("정상적으로 분리가 잘 되었습니다.")
else:
    print("소스를 다시 보세요.")
print(type(age), type(height))   # cast 연산은 영구적으로가 아니라 일시적으로 변수의 형태를 변환.
                                 # 따라서 다시 type을 확인해보면 int가 아닌 str.


4. 제어문 - if
4.4 다중 if문
    - 문법
        if <조건문>:
            <수행할 문장1>
            <수행할 문장2>
            ....
        elif <조건문>:
            <수행할 문장3>
            <수행할 문장4>
            ....
        elif <조건문>:
            <수행할 문장5>
            <수행할 문장6>
            ....
        else <조건문>:
            <수행할 문장7>
            <수행할 문장8>
            ....
    
    - 실습(3개의 정수값을 입력받은 후 비교해서 가장 큰 값과 가장 작은 값을 출력)

num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))
num3 = int(input("정수3 : "))
if num1 != num2 != num3 != num1:
      if num1 > num2 and num1 > num3: num_max = num1
      elif num2 > num1 and num2 > num3: num_max = num2
      elif num3 > num1 and num3 > num2: num_max = num3
      print("최댓값 = %d" % (num_max))   
else:
      print("다시 입력 쳐 하세요.")
if num1 != num2 != num3 != num1:
      if num2 > num1 and num3 > num1: num_min = num1
      elif num1 > num2 and num3 > num2: num_min = num2
      elif num1 > num3 and num2 > num3: num_min = num3
      print("최솟값 = %d" % (num_min))


num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))
num3 = int(input("정수3 : "))
if num1 != num2 != num3 != num1:
      if num1 > num2 and num1 > num3: print("최댓값은 %d" % num1)
      elif num2 > num1 and num2 > num3: print("최댓값은 %d" % num2)
      elif num3 > num1 and num3 > num2: print("최댓값은 %d" % num3)  
else:
      print("다시 입력 쳐 하세요.")
if num1 != num2 != num3 != num1: 
      if num2 > num1 and num3 > num1: print("최솟값은 %d" % num1)
      elif num1 > num2 and num3 > num2: print("최솟값은 %d" % num2)
      elif num1 > num3 and num2 > num3: print("최솟값은 %d" % num3)

      
- 실습(임의의 정수 값(날짜)을 입력 받고 이에 해당하는 요일을 출력하는 소스)
    : 1(월요일) ~ 7(일요일)
    : 만약 올바르지 않은 입력값일 경우 재입력을 권하는 문구 출력

day = int(input("날짜를 입력 : "))
if 1 <= day <= 31:
    if day%7 == 1: print("월요일")
    elif day%7 == 2: print("화요일")
    elif day%7 == 3: print("수요일")
    elif day%7 == 4: print("목요일")
    elif day%7 == 5: print("금요일")
    elif day%7 == 6: print("토요일")
    elif day%7 == 7: print("일요일")
else:
    print("다시 입력하세요.")
    
    - 실습(임의의 정수값(1~24)을 입력 받아서 시간을 출력하는 소스)
        : 정오(12시), 자정(24시), 오전(1시 ~ 11시), 오후(13시 ~ 23시)
        : 만약 올바르지 않은 입력값일 경우 재입력을 권하는 문구 출력

time=int(input("시간을 입력하세요 : "))
if 1 <= time <= 24:
    if time == 12: print('정오')
    elif time == 24: print('자정')
    elif 1 <= time <= 11: print('오전')
    elif 13 <= time <= 23: print('오후')
else: print("제대로 된 값을 입력하세요.")


- 실습(임의의 값(이름, 키, 몸무게)을 입력 받은 후 비만도를 구하는 소스)
   : 비만도 결과 출력(100을 기준으로 코딩)
     100 미만이면, '저체중. 곧 가겠네요'
     100 이상 110 미만, "정상"
     110 이상 120 미만, "과체중, 먹는 것을 줄이세요"
     120 이상 130 미만, "비만. 곧 따라가겠네요."
     130 이상, "고도비만. 옆자리에 앉았겠군요."
   : 표준 체중 계산       표준 체중 = (현재 키 - 100) * 0.9
   : 비만도 계산          비만도(%) = 현재 체중 / 표준 체중 * 100

name=input("이름을 입력하세요 : ")
height=int(input("키를 입력하세요 : "))
weight=int(input("몸무게를 입력하세요 : "))
표준체중=(height-100) * 0.9
비만도 = weight/표준체중*100

if 비만도<100: 
    print('{}님의 비만도는 %.0f이며 저체중입니다. 곧 가겠네요' .format(name) % (비만도))
elif 100<=비만도<110:
    print('{}님의 비만도는 %.0f이며 정상입니다. 곧 가겠네요' .format(name) % (비만도))
elif 110<=비만도<120:
    print('{}님의 비만도는 %.0f이며 과체중입니다. 먹는 것을 줄이세요' .format(name) % (비만도))
elif 120<=비만도<130:
    print('{}님의 비만도는 %.0f이며 비만입니다. 따라가겠네요' .format(name) % (비만도))
elif 130<=비만도:
    print('{}님의 비만도는 %.0f이며 고도비만입니다. 옆자리에 앉았겠군요' .format(name) % (비만도))
# 조건문이 비슷한 형태로 반복되는 경우 마지막을 else로 끝내면 안된다.    
    - 숙제(임의의 값을 입력 받은 후 윤년을 구하는 소스)
        : 4의 배수인 경우는 윤년이고 그 이외는 모두 평년
        : 4의 배수 중, 4의 배수이면서 100의 배수인 경우는 평년이고 그 이외는 모두 윤년이다.
        : 4와 100의 배수 중, 400의 배수인 경우는 윤년, 그 이외는 모두 평년

year = int(input("값을 입력하세요 : "))   # 조건문에 계산, 등(부등)식이 포함될 경우
if year%4==0:                             # 반드시 변수를 정수형으로 설정하자.
      if year%100==0:
            if year%400==0: print("%d년은 윤년입니다." % (year))
            else: print("%d년은 평년입니다." % (year))
      else: print("%d년은 윤년입니다." % (year))
else : print("%d년은 평년입니다." % (year))
# 조건문의 제작에서 숫자의 배수, 규칙성, 반복이 이용될 경우 "나머지(%)" 를 사용하자.

    - 실습 : 사용자로부터 'Gbyte'를 입력받은 후 'byte, Kbyte, Mbyte'로 출력하는 소스
           : 원하는 용량을 선택해서 출력하도록 한다.
           : byte < Kbyte < Mbyte < Gbyte < Tbyte < .....
'''

cap = int(input("용량(Gbyte) : "))
mb = cap * 10e2 # 10e2 == 10 * e2. 이때 en은 10의 n 거듭제곱
kb = cap * 10e5
b = cap * 10e8
unit = int(input("단위를 선택하시오 : 1_MB | 2_KB | 3_byte "))
if unit == 1: print("%dGbyte를 MB로 변환하면 %dMbyte" % (cap, mb))
elif unit == 2: print("%dGbyte를 KB로 변환하면 %dKbyte" % (cap, kb))
elif unit == 3: print("%dGbyte를 byte로 변환하면 %dbyte" % (cap,b))
print("%dGbyte는 %dbyte, %dKbyte, %dMbyte이다." % (cap,b,kb,mb))