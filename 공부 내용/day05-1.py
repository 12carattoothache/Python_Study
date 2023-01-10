'''
2. 자료형
2.2 문자(열)형
2.2.11 f-string(매우 중요)
name, age = '사마달', 30
print(name,age)
print("%s %d" % (name, age))
print("{} {}" .format(name, age))
print(f"{name} {age}")
    - 실습 
      홍길동씨의 과목별 점수는 다음과 같다고 할 때 평균 점수(소수 첫째 자리까지)를 구하는 소스
      국어/88.5, 영어/79.3, 수학/95.4
a, b, c= 85.5, 79.3, 95.4
d=(a+b+c)/3
print(d)
print("%.1f" % d)
print("{:.1f}" .format(d))

     - 실습
      놀이공원을 가기 위해 11개의 지하철 역을 지나왔다
      출발역에서 37분이 걸렸다면 한 역을 지나는데 걸리는 시간은 얼마인가?(소수 이하 둘째 자리)
a=37/11
print(a)
print("%.2f" % a)
print("{:.2f}" .format(a))

     - 실습
      호텔 한 층의높이는 260cm이다.
      총 14개의 층을 쓰고 있으며 1층만 500.23cm라면 이 건물의 높이는 총 몇 m인가? (소수점 이하 두자리)
a=(500.23+260*13)/100
print("%.2f"%a)
print("{:.2f}" .format(a))



2.2.12 내장 함수
'''
a= 'samadal'    # 1. 문자 갯수 세기(count함수)
print(a.count('a'))

b = 'KgItBank Samadal'   # 2. 문자 위치 알려주기(find, index함수)
print(b.find('B'))
print(b[4:5])
print(b.index('k'))

print(",".join("samadal"))    # 3. 문자(열) 삽입하기(join 함수)

c,d = "SAMADAL" , "samadal"   # 4. 대소문자 바꾸기
print(c.lower())  # 대를 소로
print(d.upper())  # 소를 대로

e,f,g="     hi","hi     ","e     hi"   # 5. 공백 지우기
print(e.lstrip())   # left(왼쪽 공백 지우기)
print(f.rstrip())   # right(오른쪽 공백 지우기)
print(g.lstrip())   
print(g.strip())    #양쪽(both side) 공백 지우기

h="Samadal Madalgyo"  # 6. 문자열 교체하기 
print(h.replace("Madalgyo", "Sam"))

i = "KgItBank Samadal"  # 7. 문자열 나누기
j = "a:b:c:d"
print(i.split())  # split함수의 입력값에 공백을 대입했으므로 나누는 기준은 띄어쓰기이다.
print(j.split(':'))     # 나누어진 값들은 리스트 형태로 출력




 