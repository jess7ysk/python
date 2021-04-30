"""
날짜 : 2021/04/27
이름 : 김예슬
내용: 파이썬 조건문 if 실습 교재 p68
"""

# if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.') #여기서 indentation이 if문 scope라고 불린다 so make sure to keep the indentation for 가독성

if num1 > num2:
    print('num1은 num2보다 크다.')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다.')

#if else
num3, num4 = 3, 4

if num3 > num4:
    #조건이 참일 경우에
    #pass: 블럭을 채워 넣는다
    print('num3가 num4보다 크다.')
else:
    #조건이 거짓일 경우에
    print('num3가 num4보다 작다.')

#if - el if - else
"""
if 조건1:
    pass
elif 조건2:
    pass
elif 조건3:
    pass
else:
    pass
"""

if num1> num2:
    print('num1은 num2보다 크다.')
elif num2 > num3: 
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

#삼항 조건문
num1 = 3
num2 = 5

result = num1 * 2 if num1 >=5 else num1 + 2
result2 = num2 * 2 if num2 >=5 else num2 + 2
print('result:', result)
print('result2:', result2)

#확인문제
score = int(input('점수 입력:'))
print('점수 확인:', score)

if score >= 90 and score <= 100:
    print('A입니다.')
elif score >= 80 and score < 90:
    print('B입니다.')
elif score >= 70 and score < 80:
    print('C입니다.')
elif score >= 60 and score < 70:
    print('D입니다.')
if score < 60:
    print('F입니다.')