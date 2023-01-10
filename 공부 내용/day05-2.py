'''
2.자료형
2.2 문자(열)형
2.2.13 변수의 유형
var1,var2,var3="1", 1, 1.0
print('{}' .format(type(var1)))
print('{}' .format(type(var2)))
print('{}' .format(type(var3)))

var1, var2, var3 = int(var1), float(var2), str(var3)  #Cast 연산(강제형 변환)
print('{}' .format(type(var1)))
print('{}' .format(type(var2)))
print('{}' .format(type(var3)))

   - 실습
     홍길동씨의 주민등록번호는 881120-1068234이다.
     '-'을 기준으로 좌측과 우측으로 분리, 출력

id = "881120-1068234"
id1, id2 = id[:6], id[-7:]
print("%s-%s" % (id1, id2))
print("{}-{}" .format(id1, id2))
print(f"{id1}-{id2}")
print(id.split('-')) # split 함수에 '-'를 대입했으므로 이것이 곧 나누는 기준이 된다.

2.3 List
2.3.1 유형별 구분
    - 리스트명(변수) = [요소1,요소2,요소3,....]
    
    - 실습
a=[]
b=[1, 2, 3]
c=['Sanmadal', 'sam', 'madal']
d=[1,2,'Samadal', 'sam']
e=[1,2,['samadal', 'sam']]
print(a, b, c, d, e)
print(type(a))
print("%s\n%s\n%s\n%s\n%S\n" % (a,b,c,d,e))

2.3.2 리스트 인덱싱

a=[1,2,3]     # 1. 단일 인덱싱
print(a)
print(type(a[0]))         # 리스트 안의 숫자는 모두 정수이다.
print(type(a[1]+a[2]))    
print(a[1]+a[2])
print(a[1]-a[2])

b=[1,2,3, ['a','b','c']]   # 2. 다중 인덱싱
print(b)
print(b[0])
print(b[1])
print(b[3])
print(b[3][0])
print("%s" % b[3][0])

c=[1,2,['a','b',['Kg','It','Bank']]]
print(c)
print(c[0])
print(c[2])
print(c[2][1])
print(c[2][2][1])
print(c[-1][0])   # 인덱싱의 순서(왼쪽이 첫 번째)는 가장 큰 단위부터 적용된다.

2.3.3 리스트 슬라이싱

a=[1,2,3]  
print(a[:])
print(a[1:])
print(a[:2])
b = [1,2,3,['a','b','c'],4,5]
print(b[2:5])
print(b[3][:2])    # 인덱싱과 슬라이싱이 함께 적용

2.3.4 리스트 기타
      - 리스트 연산
a=[1,2,3]
b=[4,5,6]
print(a+b)   # 실제 연산되지 않고 목록을 더한다.
print(a * 2)
print(a[2]+4)

      - 리스트 수정
a=[1,2,3]
a[2] = 4
print(a)   # 3번째 원소인 3이 4로 교체

a[1] = ['a', 'b', 'c']  # 2번째 원소인 2가 리스트로 교체 
print(a)
print(a[1])    # 인덱싱이므로 리스트인 원소가 그 자체로 출력
print(a[1:2])   # 슬라이싱이므로 리스트인 원소에 리스트가 하나 더 붙어서 출력

a[1:2] = ['d','e','f']   # 슬라이싱이므로 리스트 안에 구성요소들로만 교체됨
print(a)
a[1:2] = [['d','e','f']]   # 슬라이싱이지만 리스트 안에 리스트가 있으므로 리스트로 교체
print(a)

     - 리스트 삭제
a = [1,['a', 'b', 'c'], 'b', 'c', 4]
print(a[1:3])
a[1:3] = []    # 슬라이싱이므로 해당 부분 삭제
print(a) 

b = [1,2,['a','b',['Kg','It','Bank'],4,['c','d']]]   
print(b)
print(b[2][2][1]) 
b[2][2][1]=[]    # 인덱싱이므로 해당 부분은 []로 대체.
print(b)
del b[2][2][1]    # 삭제
print(b)

a=[500,200,300,400]
sum = 0   # 조건문의 합을 구할 때는 반드시 초기값을 지정해야 한다.
sum = a[0] + a[1] + a[2] + a[3]
print(sum)

a,b=[1,2,3], '48'
print(type(a),type(b))
print(type(a[2]),type(b))  # 리스트 안의 요소가 정수형
print(a[2])   
print(int(b))
print(type(int(b)))
aa, aaa= str(a[1]), str(a[2])  # 정수형을 문자열로 변환
print(type(aa), type(aaa))
print(aa,aaa)  
print(a[1],a[2])  
print(aa+aaa)   # 문자열끼리의 연산은 단순 이어쓰기
print(a[1]+a[2])   # 정수형끼리의 진짜 연산

2.3.5 리스트 관련 함수
a=[1,2,3]
a.append(4)    # 1. 요소 추가.  변수명.append([인수1, 인수2,....])
print(a)
print(5,6)    # 하나의 요소만 추가 가능하므로 오류
a.append([5,6])    # 리스트 자체를 하나로 취급해 추가
print(a)
# print(a.append([5,6]))    # 출력은 되지만 오류(None). 출력과 동시에 
                            # 요소 추가 불가능. 이때 요소는 추가됨.
                                            
a=[1,2,3]
a.extend([5,6])   # 2. 확장.  변수명.extend([인수1,인수2,....])
print(a)          # 여러개의 요소를 추가 가능하므로 리스트의 요소들을 전부 추가
print(a.extend([5,6]))  # 출력은 되지만 오류(None). 출력과 동시에 요소 추가 불가능.  
                        # 이때 요소는 확장됨.
b=[7,8] 
a.extend(b)
print(a)


a=['z','b','t','c']    # 3. 뒤집기.  변수명.reverse()
b=[1,4,3,2]
a.reverse() 
b.reverse()   
print(a)
print(b)
print(a.reverse())   # 출력은 되지만 오류(None). 출력과 동시에 뒤집기 불가능
                     # 이때 뒤집기만 됨.


a.sort()       # 4. 정렬.  변수명.sort()
print(a)       # 알파벳 순 정렬
b.sort()
print(b)       # 숫자 크기 순 정렬
print(a.sort())     # 출력은 되지만 오류(None). 출력과 동시에 정렬 불가능
                    # 이때 정렬만 됨.


a=[1,7,13]      # 5. 위치 확인.  변수명.index(위치를 확인하고자 하는 원소 값)
#b1 = a.index(0)
#print(b1)
b1=a.index(1) 
# b2=a.index(2)  # 리스트 안에 '2'가 없기 때문에 오류
# print(b2)
b2=a.index(7)  
b3=a.index(13)
print(b1,b2,b3)

a=[1,7,13]      # 6. 삽입.  변수명.insert(값을 삽입할 위치, 삽입할 값)
b=[1,2,3,1,2,3]
a.insert(0,4)   
print(a)
a.insert(3,5)
print(a)

b.remove(3)     # 7. 삭제.  변수명.remove(삭제할 값 중 첫번째)
print(b)
b.remove(2)
print(b) 
'''

a=[3,2,1]       # 8. 꺼내기.  변수명.pop(꺼낼 숫자의 위치)
b=[1,2,3,4,5]        # ()에 위치를 안 적으면 맨 뒤에서부터 꺼낸다.
c=[1,2,2,3,3,3]
a.pop()     
print(a)    
a.pop()
print()

b.pop(2)     # 3번째 원소가 빠진다.
print(b)

print(c.count(3))    # 9. 갯수 세기.  변수명.count(갯수를 셀 숫자)