# -*- coding: utf-8 -*-

"""
step04 string

1. 문자열 처리

2. escape 문자
"""


#1. 문자열 처리(string)

"""
indexing, slicing 가능
수정은 불가능(상수 취급) : 새로운 객체로서 취급
"""

#1-1. 문자열 유형
lineStr = "this is one line string"
print(type(lineStr)) #class 'str'

multiLine = """This is 
multi line
 string"""

print(type(multiLine)) #class 'str'

multiLine2 = "This is\nmulti line\n string" #이런식으로 다중 줄 text도 입력 가능

#SQL문도 구현 가능
query = """select * from emp
where deptno = 1001
order by sal desc"""

print(query)

#2] indexing/slicing

'''
r index = 1부터 시작
python index = 0부터 시작
'''

#2-1. 색인 쓰기 : 기존의 문자를 참조해서 검색
print(lineStr)
print(lineStr[0]) #첫 글자 반환
print(lineStr[0:4]) #첫글자 ~ 5번째 글자까지 반환

#오른쪽에서 색인하기
print(lineStr[-1]) #마지막 글자 반환
print(lineStr[-6:]) #마지막에서 6번째 글자에서 끝까지


#2-2. slicing : 잘라서 새로운 객체 만들기. 주소는 다르지만, 검색한 값은 별도의 객체로 유지한다.
substr = lineStr[:4]

#2-3. 문자열 연산
print('python' + 'program') #두 문자열을 합침
print('-'*50) #-를 50번 반복


#3] 객체, 멤버

print(lineStr.count('t')) #2, 객체.method()

#3-2. 접두어 판단 ~ T? F?

lineStr.startswith('this') # True
lineStr.startswith('that') # False

'''
함수 vs method?
일반함수 = 함수
객체의 함수 = method
'''

#3-3. 문자열 분리, 결합 (split & join)
#문단 -> 문장 split
sent = multiLine.split(sep = '\n')
print(sent, len(sent))

#문장 -> 단어 split
words = multiLine.split() # sep = '' 공백을 기준으로 토큰 생성
print(words, len(words))

lines = ' '.join(words)


#4] escape 문자

'''
특수기능 문자인 \n, \t, \b, \r, '', ""
의 기능을 알아보자
'''

print('escape 문자')
print('\\n문자') # escape 기능 차단1 = \
print(r'\n문자') # escape 기능 차단2 = r

#경로 표현
print('D:\Dropbox\Bigdata visualization course\ITWILL\3_Python-I\workspace\chap01_Basic\lecture')
print('D:\\Dropbox\\Bigdata visualization course\\ITWILL\\3_Python-I\\workspace\\chap01_Basic\\lecture')
print(r'D:\Dropbox\Bigdata visualization course\ITWILL\3_Python-I\workspace\chap01_Basic\lecture')













