# -*- coding: utf-8 -*-

"""
변수
 - 자료가 저장된 메모리 이름
 - 형식) 변수명 = 값 or 수식 or 변수명
 - 자료형 선언 없음. (R과 동일)
 - 모든 변수는 객체. (R과 동일)
"""

# F5 = 전체실행 / F9 = 부분실행
#1. 변수와 자료형

var1 = "Hello python"
var2 = 'Hello python'
print(var1)
print(var2)
print(type(var2), type(var1))

#type = 객체의 출처 확인 (클래스 확인)

var1 = 100
print(var1, type(var1))

var3 = 123.2345
print(var3, type(var3))

#2. 변수명 작성 규칙

"""
첫자 = 영문자 or _
두번째 = 숫자 사용 가능
대소문자 구별함
낙타체 = 두 단어 결합
키워드(클래스명, 함수명) 사용 불가, 한글 변수 비권장
"""

_num10 = 10
_Num10 = 20
print(_num10*2) # 20
print(_Num10*2) # 40

# 키워드 확인
import keyword
kword = keyword.kwlist
print(kword)
print('word 개수 = ', len(kword))


#낙타체
korScore = 89
matScore = 75
engScore = 55

tot = korScore + matScore + engScore
print('tot = ', tot)

#3. 참조변수 : 객체가 저장된 메모리 주소 저장
x = 150
y = 45.23
x2 = x
y2 = 45.23

print(x)
print(id(x))
print(id(x2))

print(y)
print(id(y))
print(id(y2))

