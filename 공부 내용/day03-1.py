'''
2. 자료형
2.2 문자(열)형
2.2.7 문자열 인덱싱(Indexing)
  - 개요
    : 원하는 임의의 위치의 값을 출력
    : 책에서의 '목차'에 해당. 즉 '위치'를 표시
  - 인덱싱 요령
    : 앞에서 인덱싱(기호(-)가 없는 형태)할 때는 '0'부터 
    : 뒤에서 인덱싱(기호(-)가 있는 형태)할 때는 '1'부터  
-실습
a = "KgItBank, Samadal, Python"
print(a)
print(a[0])
print(a[8])
print(a[-1])
print(a[-6])
b = "kg_It_Bank"
print(b[3])
c=b[3]
print(c)
print(len(c))
print(len(b[3]))

print('SAM','samadal,', sep=' = ')
b = "kg_It_Bank"
d=b[0]
print('d', b[0], sep=' = ')
print('d', d, sep=' = ')
print('b[0]', b[0], sep=' = ')
print(10,20,30, sep='-')

print(10,20,30, sep='% ')
print('사마달', end='씨\n')  #end가 있을 경우에는 아랫줄이 모두 한 줄로 붙어서 출력
print(10,20,30, sep='% ',end='%')
 - 출력 문구가 'C:\Program Files\Python310\'과 같이 되게 하려면?
print('C:\\Program Files\\Python310\\')
print('C:','Program Files','Python310', sep='\\', end='\\')
 - 출력 문구가 'C:\\Program Files\\Python310\\'과 같이 되게 하려면?
'''
print('C:\\\Program Files\\\Python310\\\\')  #'\'는 뒤에 '단 한 개의 기호'를 삽입하는 것이므로 '\\\'를 입력하면 오류가 뜬다.
print('C:\\', 'Program Files\\', 'Python310\\', sep='\\',end='\\''\n')