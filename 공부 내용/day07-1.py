'''
2.자료형
2.5 Dictionary(딕셔너리)
2.5.1 문법
   - 묶음이 '{}'로 되어 있다.
   - {'Key1':Value1', 'key2':'Value2', .....}로 구성된다.
   - 연산시 입력한 순서대로 출력하지 않고 key를 통한 값을 호출한다.

2.5.2 생성, 추가, 삭제 및 주의 사항
# 1. 생성(1)
dic1 = {'name':'Samdal', 'phone':'010-1234-5678', 'birth':'0113'}
print(dic1)
print(type(dic1))
print(dic1['name'])     # key는 변수로 사용된다. 인덱싱처럼 []에 Key를 써서 항목을 호출 
                        # 따라서 ()를 사용하면 오류
dic2 = {'1':'madal'}
print(dic1['name'],dic2['1'])

dic3 = {'a':[1,2,3]}
print(dic1['name'],dic2['1'],dic3['a'])
# print(dic1['Samadal'])    # KeyError(키 대신에 값을 호출인자로 사용 불가능, 오류)

# 2. 추가
a= {1:'a'}
print(a[1])   # a의 2번째 값(in list)가 아니라 dictionary의 key와 맞는 값 호출 
a[20] = 'b'     
print(a)

# 3. 생성(2)
b={}
b['name'] = 'Samadal'
print(b)
b['madal'] = 'samadaL'
print(b)

# 4. 삭제
c={1:'samadal', 2:'madal'}
del c[2]      # 키를 삭제하면 키와 함께 값도 삭제된다.
print(c)
# del c['samadal']    # 삭제할 때는 키를 이용하고 값은 이용할 수 없다.
# print(c)

# 5. 주의 사항
a={2:'madaL'}  
# print(a+c)     # dictionary는 다른 연산 방식과 달리 병합이 안 된다.

c[2] = [5,6,7]    # dictionary의 Value는 리스트도 가능하다.
print(c)

2.5.3 딕셔너리 관련 함수
dic1={'name':'Samamdal','phone':'010-1234-5678','birth':'0113'} 
print(dic1.keys())      # 1. keys() : Key 목록을 출력
# print(dic1['name'].keys())    # str(문자열) 속성에는 keys 속성이 없어서 오류
print(type(dic1['name']))       # 위에서 얘기하는 문자열은 value인 'samadal'.
print(dic1.values())    # 2. values() : Value 목록을 출력
a = list(dic1.keys())   # cast 연산을 통해 리스트로 강제 형태 변환.
print(a)
print(list(dic1.values()))

print(dic1.items())   # 3. items() : 딕셔너리의 Key와 Value의 목록을 한 개의 리스트로 출력

dic1.clear()    # 4. clear() : key와 value 모두 삭제 
print(dic1)

a=dic1.get('name')    # 5. key를 이용한 value 호출
print(a)
print(dic1.get('name'))

print(dic1.get('madal','samadal'))  # key에 'madal'이라는 키명이 없기 때문에 기본값이 그냥 출력
                                    # get('없는 key명', '기본값')일 경우 기본값이 그대로 출력
print(dic1.get('phone', 'birth'))   #get(키명, 키명)이기 때문에 앞에 것만 출력
                                    #get('있는 key명', '기본값')일 경우 있는 key명이 출력            

print('name' in dic1)    # 6. Bool대수(참과 거짓을 판단)
print('madal' in dic1)
print('0113' in dic1)    # key가 있는 지만 판단하는 것. value와 관계 x
    
2.5.4 실습
       - 학생의 인적사항 등록 후 검색하는 프로그램을 작성
       : 포함 내용(인적사항 등록, 학생 등록, 인적사항 수정, 전체 인적사항 보기, 학생 삭제, 종료)
       - 인적사항 : 학번, 이름, 주민번호, 등급(A, B, C, D, F)     
'''

namelist2 = {}     # 1. 인적사항 등록
namelist2['num'] = '1234568'
namelist2['name'] = '마달이'   
namelist2['id'] = '123457-1456790'    
namelist2['grade'] = 'A'
print(namelist2)           

print(namelist2.get('name'))    # 2. 학생 검색

namelist2['grade'] = 'C'     # 3. 인적사항 수정
print(namelist2)

print(namelist2.items())    # 4. 전체 인적사항 보기

del namelist2['num']      # 5. 학생 삭제
del namelist2['name']
del namelist2['id']
del namelist2['grade']
# 또는 namelist2.clear() 한 뒤 출력
print(namelist2)

print("프로그램을 종료합니다.")     # 6. 종료