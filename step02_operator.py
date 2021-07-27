# -*- coding: utf-8 -*-
"""
step02_operator.py

연산자(operator)

1. 할당연산자(=) : 변수에 값 할당
2. 연산자 : 산술, 관계, 논리 연산자

"""

#1. 할당연산자

#i = 10
#tot = 10

i = tot = 10

print(i, tot)

i += 1 # 카운터 변수
print(i, tot)

tot += i # 누적 변수
print(i, tot)

#서로 다른 값 할당
v1, v2 = 100, 200
print(v1, v2)

#변수 값 교체
v1, v2 = v2, v1
print(v1, v2)

#패킹 할당
lst = [1,2,3,4,5] #vector 형태의 data 생성
print(lst)

v1, *v2 = lst # 서로 다른 패킹을 할당..?
print(v1, v2)

*v1, v2 = lst
print(v1, v2)


#2. 연산자

num1 = 100
num2 = 10

square = num1 ** num2
print(square)

div2 = num1 % num2
print(div2)

#2-2. 관계연산자

#같은가?, 다른가? T, F로 변환
result = num1 == num2 #같은가?
print(result)

result = num1 != num2 #다른가?
print(result)

#크기 비교
result = num1 >= num2 #1이 크거나 같나?
print(result)
result = num1 > num2 #1이 큰가?
print(result)

result = num1 <= num2 #1이 작거나 같나?
print(result)
result = num1 < num2 #1이 작은가?
print(result)


#2-3. 논리연산자
result = num1 >= 50 and num2 <= 20 #and를 활용하여 조건을 2개를 걸어서 참, 거짓을 확인
print(result)

