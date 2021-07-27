# -*- coding: utf-8 -*-

"""
1. print() = 출력

2. input() = 입력
"""
######################
#print
######################

help(print)
#print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#내가 출력할 값, sep = 구분자, end = 종료시! \n은 다음줄로

#1. 기본인수
print("value =", 10, 10+20)
print('010', '1234', '1111', sep='-')

#end 속성
print("value =", 10, end=',')
print("value =", 20) #생략히 공백 1개로 대체됨.


#1-2. %양식문자
# 형식) print('%양식문자' %값) - ppt.23

num1 = 10; num2 = 20
tot = num1 + num2
print('%d + %d = %d' %(num1, num2, tot))

print('이름은 %s이고, 나이는 %d이다.' %('홍길동', 35))

print('원주율 = %8.3f' %(3.14159)) #전체 8자리, 소수점 3자리 표시

print('전체 찬성률은 %d%%이다.'%50)

#1-3. format()함수
# 형식) '{형식}' .format(값)
print('이름은 {}이고, 나이는 {}이다.' .format('홍길동', 35))

#{상수위치:형식}
print('정수형 = {0:d}, {1:5d}, {2:3,d}'.format(123,123, 2500))
#첫번째 자리는 그대로, 두번째 자리는 5개 자리에 2번째 자리부터 시작함

print('원주율 = {0:.3f}, {1:8.3f}'.format(3.14159,3.14159))

name = '홍길동'; age = 35
sql = f"select * from emp where name = '{name}' and age = {age}"


########################
#input
########################

help(input)

ftemp = input(prompt='ftemp :')

#1. 문자 -> 정수형, 실수형 변환

x = int(input('숫자 입력 :'))
y = float(input('숫자 입력 :'))

#2. 형변환
print(int(24.5)) #실수를 입력했지만 int로 바꿔서 정수로 나옴. 24
#그러나, 문자형을 실수로 바꾸는 등의 명령은 안먹힘. 에러!

print(int(True))
print(int(False))


