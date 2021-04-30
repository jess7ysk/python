"""
날짜 : 2021/04/27
이름 : 김예슬
내용: 파이썬 표준입출력 실습 교재 p42
"""

#파이썬 표준 출력
print('hello') #javascript에서는 document.write('hello'); java는 System.out.print('hello'); c언어는같다;cpp는 cout.write('hello)
print('hello',end='!')
print('python')

print('010','1234','1111',sep='-')

#파이썬 표준 입력
num = input('숫자 입력 : ')

print('입력한 숫자:', num)
print('num type:', type(num))

#입력받은 문자열을 숫자로 변환
result = int(num)
print('result:',result)
print('result type:', type(result))

#서식문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 4, 27, '화')) #%d decimal 순서대로 mapping 된다 %s는 string=phrase

#포맷문자 출력
print('이름: {}, 나이: {}, 주소:{}'.format('김유신',23,'김해시'))