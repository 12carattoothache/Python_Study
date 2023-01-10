'''
2.자료형
2.4 Tuple(튜플)
2.4.1 튜플 자료형의 특징
   - 리스트와 거의 모두 동일하지만 값의 생성, 수정, 삭제가 불가능하다.
   - 문자열(%, .format(), f-string), [List], (Tuple), {Dictionary}

2.4.2 튜플 자료형의 유형
    t1 = ()
    t2 = (, )
    t3 = (1,2,3)
    t4 = 1, 2, 3
    t5 = ('a', 'b', ('ab', 'ba'))

2.4.3 기타
t6 = (1, 2, 'a', 'b')
print(t6)
# t6[0]= 4    # 튜플 수정 불가
# print(t6)    

#del t6[1]     # 튜플 삭제 불가
#print(t6)

a=(1,2,'a','b')
b=(3,4,'c','d')
print(a[0])    # 인덱싱
print(b[3])    

print(a[:2])   # 슬라이싱
print(b[1:])

print(a + b)   # 연산
print(b*4) 

# (1,2,3)이라는 튜플에 4라는 값을 추가해서 (1,2,3,4)가 출력되려면?
a,b=(1,2,3),(4, )    # 추가
print(a,b)
print(type(a), type(b))   # 괄호 안에 오직 정수만 있으면 int, ','까지 있으면 튜플이다.
a += b     # a = a + b 
print(a)
 
2.4.4 튜플 관련 함수
'''
tp=100,200, "함수", 300, "갯수"    # 괄호가 없는 유형으로도 튜플 표현 가능
# 변수명.index(항목의 값)
print("tp안의 200의 위치 :",tp.index(200),"\b번째 인덱스")
pt = tp.index(100)
print(type(tp), type(pt))
print("tp안의 100의 위치 : %d번째 인덱스" % pt)
print('tp안의 "함수"의 갯수 :',tp.count("함수"),"\b개")
print(f"tp안의 300의 갯수 : {tp.count(300)}개")
