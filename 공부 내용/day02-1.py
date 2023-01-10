'''
2. 자료형
2.1 숫자형
2.1.1 정수형
a, b = 123, -178     
print(a, b)  #a, b의 값을 출력
print(a + b) #a와 b의 더한 값을 출력
print(a - b) #a에서 b를 뺀 값을 출력
print(a * b) #a와 b를 곱한 값을 출력
print(a / b) #a를 b로 나눈 값을 출력 
2.1.2 실수형
a, b, c, d = 1.2, -3.45, 4.24E10, 4.24e10   #실수형은 모두 소수점 형태로 선언한다.
print(a, b, c, d)     
print(a + b) 
2.1.3 8진수와 16진수, 10진수
e, f, g = 0o177, 0x8ff, 0xABC  # 8진수(octal), 16진수(Hexa Decimal), 10진수(Decimal)
print(e, f, g)    #출력 결과는 모두 10진수이다.
print(e + f +g)
2.1.4 실습
a, b, c, d = 3, 4, 7, 3
print(a + b, c + d)
print(a - b, c - d)
print(a * b, c * d)
print(a / b, c / d)
print(a ** b)   #3^4=81
a, b, c, d = 3, 4, 7, 3
print(a % b)     # 3을 4로 나눈 나머지(나눌 수가 없기 때문에 나머지가 그대로 '3'으로 출력)
print(b % a)     # 4를 3으로 나눈 나머지('1'이 출력)
print(a // b)    # 3을 4로 나눈 몫(나눌 수가 없기 때문에 '0'이 출력)
print(b // a)    # 4를 3으로 나눈 몫('1'이 출력)
c, d = 7, 3
print(c % d)
print(d % c)
print(c // d)
print(d // c)
e, f = 14, 15
g = e % 2         #우측의 연산되는 값의 결과를 좌측의 변수에 대입.(14를 2로 나눈 나머지는 0)
print ('주어진 값의 나머지는', e%2, '가(이) 되므로 짝수이다')
print ("주어진 값의 나머지는", g, "가(이) 되므로 짝수이다")
'''