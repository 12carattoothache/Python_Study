import sys

dic = {'ID' : 'seho614', 'PW' : 'rlaeogus200'}
id = input('아이디를 입력하세요 : ')

if id == dic['ID'] :
    pw = input('비밀번호를 입력하세요 : ')
    length = len(pw)
    if length >= 7 :
        i = 0
        while i <= (length - 1) :
            if pw[i].encode().isalpha() or pw[i].isdigit() :
                i += 1
                continue
            else :
                print('비밀번호는 영문과 숫자로만 구성됩니다.')
                sys.exit()
        if pw == dic['PW'] :
            print('로그인에 성공하셨습니다.')
        else :
            print('비밀번호가 일치하지 않습니다.')
    else : 
        print("비밀번호는 7자 이상이어야 합니다.")          
else :
    input('입력하신 아이디는 존재하지 않습니다.')
    

