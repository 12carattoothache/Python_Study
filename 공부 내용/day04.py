'''
2. 자료형
2.2 문자(열)형
2.2.10 .format()함수 (매우 중요)
   - 문법
     print("{0}{1}...." . format(값1, 값2, ...))
   - %문자열과의 비교  
print("KgItBank %d년 1월 10일" % 2022)
print("KgItBank {0}년 1월 10일" .format(2022))
print("KgItBank {}년 1월 10일" .format(2022))  # 숫자는 생략 가능하다.
a = "KgItBank {}년 1월 10일"
print(a .format(2022))

b, c, d = 2022, 1, 10
print("KgItBank %d년 %d월 %d일" % (b, c, d))
print("KgItBank {0}년 {1}월 {2}일" .format(b,c,d))
     - 실습
        '사마달님의 나이는 200살입니다.'를 %문자열과 .format()로 표현하려면?
# 내 답안    
a = '사마달님의 나이는 %d살입니다.'
b = '사마달님의 나이는 {}살입니다.'
print(a  % (200))
print(b .format(200))
# 선생님 답안
age, name= 200, '사마달'
c="%s님의 나이는 %d살입니다."
d="{}님의 나이는 {}살입니다."
print(c%(name,age))
print(d.format(name,age)) 

g="사마달님의 나이는"
h="살입니다."
print("%s %d%s" % (g,200,h))
print("{0} {1}{2}" .format(g,200,h))

- 실습
 출력 내용이 "사마달님의 나이는 200살입니다." 인 것을 문자열로 표현.

a,name,age="{}님의 나이는 %d살입니다.", '사마달', 200
print("%s님의 나이는 {}살입니다." .format(age) % name)
# print("{}님의 나이는 %d살입니다." % age .format(name))  # 퍼센트 문자열을 .format함수보다 먼저 사용하면 안 된다.
print(a .format(name) %age)

b = "{0}님의 나이는 {1}살입니다."
c = "%s님의 나이는 %d살입니다."
d,e= '사마달', 200
print(b .format(d,e))
print(c % (d,e))

- 실습
   출력 내용이 "사마달님의 나이는 200살입니다."인 것을 문자열로 표현
   변수의 값(사마달, 200)을 인덱싱 또는 슬라이싱으로 변경 후 같은 내용을 출력

a="사마달,200"
print(a[:3],a[-3:])
print('{}님의 나이는 %s살입니다.' .format (a[:3]) % a[-3:])
print("%s님의 나이는 %s살입니다." % (a[:3],a[-3:]) )
print("{}님의 나이는 {}살입니다." .format(a[:3],a[-3:]))


# - 실습(출력문에 이름 넣기)
year, month =2022, 1
print("%d(KgItBank) %d(Samadal)" % (year,month))
print("{}(KgItBank) {}(Samadal)" .format(year, month))

#print("{}(KgItBank) {}(Samadal)" .format(year=2022, month=1))
print("{}(KgItBank) {}(Samadal)" .format('year=2022', 'month=1')) # {}에 지정된 변수가 없으므로 문자열 처리해서 대입

# print("{year}(KgItBank) {month}(Samadal)" .format(2022,1))
print("{year}(KgItBank) {month}(Samadal)" .format(year=2022, month=1)) # {}에 지정된 변수가 있으므로 '변수=~' 처리해서 대입

# - 실습(정렬)
print("{}" .format('0123456789'))  
print("{0:<10}" .format('samadal'))   # 왼쪽 정렬
print("{:<10}" .format('samadal'))
print("{0:>10}" .format('samadal'))   # 오른쪽 정렬
print("{0:^10}" .format('samadal'))   # 가운데 정렬
print("{0:=^10}" .format('samadal'))  # 가운데 정렬 후 공백을 '='로 채우기
    
#    -실습(소수점 표현)
print("{0:f}" .format(3.41214234))   # 실수는 기본적으로 6자리까지 출력
print("{0:0.4f}" .format(3.41215234))
    
#    -기타
'''
print("{:,}" .format(2000000))      # 천 자리 구분