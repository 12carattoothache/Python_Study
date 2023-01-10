'''
2.2.9 %문자열(매우 중요!!)
  - 문자열 포맷 코드
    :%d(정수, Decimal. Integer), %s(문자열, String), %c(문자, Character), %f(실수,Float), %b(2진수, Binary), %o(8진수, Octal), %x(16진수, Hexa-Decimal)
  - 문법
    print('%유형1,%유형2,........' % (값1,값2,.......))  
  - 실습
    # 2진수를 10진수 표현 
print(0b1101010001110001)   # 2진수를 10진수로 표현
bin1 = 0b1101010001110001
bin2 = 1101010001110001
print('%d' % bin1)  # 정수형으로 변환된 후 출력
print('%d' % bin2)  # 일반적인 숫자와 동일하게 출력

hexa = 0x3D5F         # 16진수를 10진수로 표현
print("%d" % hexa)

dec = 1024   # 10진수를 16진수로 표현 
print('%x' % dec)

decsum = 3452 + 5786
print("%x" % decsum)
dec1, dec2 = 3452, 5786
print("%x" % (dec1 + dec2))
dec3 = dec1 + dec2
print('%x' % dec3)
hexa, oct = 0x5C90, 0o652
ho = hexa + oct   # 16진수와 8진수를 더한 값을 10진수로 표현
print(ho)
print("%d" % (0x5C90 + 0o652))
print("%d" % (ho))
print("16진수(0x5C90) + 8진수(0O652) = 10진수(%d)" % ho)
print("16진수(%x)+8진수(%o)=10진수(%d)" % (hexa, oct, ho))
print(type(hexa), type(oct))

dh = ("%d" % 0x5C90)   # 왼쪽에 있는 변수에 값이 아닌 문장(String) 형태로 저장되어 있다.
do = ("%d" % 0o652)
print(dh + do)
print(("%d" % 0x5C90))
print("%d" % 0o652)
a = 1
b = 2
print(type(dh), type(do)) # class 'str'은 정수(int)가 아닌 문자열로 인식하기 때문에 오류가 발생
                          # 문자열은 연산이 안되고 단지 순서대로 나열만 된다.
a, b = 1, 2
print(type(a), type(b))
print(a+b)

a = 'KgItBank 2022년 1월 10'
print("KgItBank %s년 1월 10" % 2022)
print("KgItBank %d년 1월 10"  % 2022)
print("KgItBank %s년 1월 10" % "2022")

# 위의 내용의 모든 값을 변수로 치환한 후 출력하려면? (인덱싱, 슬라이싱, %문자열이 모두 포함) 
a, b, c, d = "KgItBank", 2022, '1', 10 # 문자열, 정수, 문자열, 정수
print("%s %d년 %s월 %d일" % (a, b, c, d))

e = "KgItBank2022110"   # 변수가 문자열로 정의되어 있기 때문에
f, g, h, i = a[:8], e[8:12], e[12], e[-2:]
print("%s %s년 %s월 %s일" % (f, g, h, i)) # 받아오는 값도 문자열이다.

print("%d%%" % 54)  # 특수 기호가 붙은 문자열
print("%d\n" % 54) 
'''
print("01234567890123456789")
print("%+15s" % 'samadal')      # 자리 확보한 후 우측(+) 정렬  (기호(+)는 생략 가능)
print("%-15s" % 'samadal')      
print("%-15s" % 'samadal')      # 자리 확보한 후 좌측(-) 정렬

print("%f" % 3.14)              # 실수형은 기본적으로 소수 이하 6자리까지 출력
print("%0.3f" % 3.14)           
print("%.2f" % 3.14)  
print("%8.2f" % 3.14)           # .좌측(자리확보) / .우측(소수 이하 자릿수)
