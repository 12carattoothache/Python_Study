'''
- %문자열과 .format()함수의 차이
bin1 = 0b1101010001110001
bin2 = 1101010001110001
print("bin1 = %d\nbin2 = %d" % (bin1, bin2))
print("bin1 = {}\nbin2 = {}" .format(bin1,bin2))

hexa, dec, a, b = 0x3D5F, 1024, 3452, 5786
print("hexa = {}, dec = {}" .format(hexa,dec))
decsum = a+b
sumdec ="%x" % decsum
print("{}" .format(sumdec))
a,b,c,d,e = "KgItBank", 2022, "1", 10, "KgItBank2022110"
f,g,h,i=e[:8], e[8:12],e[12], e[-2:]
print("{} {}년 {}월 {}일" .format(a,b,c,d)) #.foramt()함수의 경우에는 타입의 유형을 신경쓰지 않아도 된다.
print("{} {}년 {}월 {}일" .format(f,g,h,i))
print("%d%%" % 54)
print("{}%".format(54))

# %문자열은 입력값에 맞는 유형(입력값의 유형)을 함수에 지정해줘야 함, 반면 .format()함수는 따로 지정 X

#숙제: 지난 번 수업 때 print했던 것들을  %문자열과 .format()함수로 바꾸기!
'''

print("87%%를 표현하는 방법 1 : %d%%" %87)
print("87%%를 표현하는 방법 2 : {}%" .format(87))

