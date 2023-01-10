
'''
7.6 입력과 출력
- 파일 읽고 쓰기
    - 파일 생성
        : 특징
             : 자바에서의... => 객체 = 메서드()
             : 파일이 있으면 내용을 삭제하고 없으면 지정 경로에 생성
             : 문법
            파일 객체(0ject) = open("경로명/파일명", "열기모드(r(읽기),w(쓰기),a(추가)")
            파일 객체.close()

a= open("samadal.txt", "w")    # 실행은 되지만 오류, 이렇게는 사용 안 함.
a.close()

a= open("c:/python/samada1.txt", "w")    # 일반적으로 사용하는 방법
a.close()  

a= open("c:/python/post.txt","w")  
for i in range(1,11):
    data = "%d번째 줄입니다\n" % i
    a.write(data)
a.close()

- 외부에 저장된 파일 읽기 

a= open("c:/python/post.txt","r")    # 읽기 권한
line = a.readline()     # 1. readline() 함수: 한 줄만 출력
print(line)
a.close()

a= open("c:/python/post.txt","r")   # 읽기 권한
while True:
    line = a.readline()     # 1. readline() 함수: 한 줄만 출력
    print(line)
    if not line: break
a.close() 

a= open("c:/python/post.txt","r")   # 읽기 권한
lines = a.readlines()     # 2. readlines() 함수: 모든 줄을 출력
for line in lines:
    print(line)
a.close() 

a= open("c:/python/post.txt","r")   # 읽기 권한
data = a.read()     # 3. read() 함수: 모든 줄을 출력(문서 내용 그대로 출력)
print(data)
a.close() 

a= open("c:/python/post.txt","w")   
for i in range(1,11):     
    data = "%d번째 줄입니다\n" % i
    a.write(data)
a.close() 

a= open("c:/python/post.txt","a")   # 내용 추가
for i in range(11,21):     
    data = "%d번째 줄입니다\n" % i
    a.write(data)     # 4. write()함수 : 파일에 새로운 내용 추가
a.close() 

a= open("c:/python/post.txt", "w")
a.write("pm4")
a.close()      # 기존 파일의 내용들이 전부 삭제, 신규 내용만 추가


a=open("c:/python/post.txt","w")
for i in range(1,11):
    data = "%d번째 줄입니다\n." % i
    a.write(data)
a.close()

with open("c:/python/post.txt","w") as k:   # 5. with ~ as문 : close()함수 없이 자동으로 열고 닫는다.
    k.write('post')  

with open("c:/python/post.txt","a")  as k:   # j라는 대표명으로 문서를 열어라!
    for i in range(1,11):      
        data = "%d번째 줄입니다\n" % i
    k.write(data)    

a= open("c:/python/post.txt", "w")
a.write()
a.close()
'''
# 6. sys 모듈로 매개변수 주기
import sys    # 파이썬 시스템의 내장 모듈(Module)
args = sys.argv[1:]       # 실행순서만 기억
for i in args:
    print(i) 

