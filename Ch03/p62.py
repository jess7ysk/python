"""
날짜 : 2021/04/28
이름 : 김예슬
내용: 파이썬 실습 교재 p62
"""

score = int(input('점수 입력: '))
grade = '' # 등급

if score >= 85 and score <=100 :
    grade = '우수'
elif score >= 70 :
    grade = '보통'
else :
    grade = '저조'

print('당신의 점수는 %d이고, 등급은 %s'%(score, grade))