"""
날짜 : 2021/04/28
이름 : 김예슬
내용: 파이썬 조건문 While 실습 교재 p64
"""

# while

num1 = 1 # not that num1 one is fixed as 1, but that num1 STARTS with 1 in this case

while num1 < 5:
    print('num1 :', num1)
    num1 += 1

# 1부터 10까지 합
k, sum = 1, 0 # 열 번호를 클릭하면 나오는 빨간색 버튼: break point (수동계산 -> debug + F8)

while k <= 10:
    sum += k
    k += 1

print('1부터 10까지 합 :', sum)

# 1부터 10까지 짝수 합
i, tot = 1, 0

while i <= 10:

    # if i가 짝수이면
    if i % 2 == 0:
        tot += i
        #여기에서 칸 들여쓰기 안 하면 인식 못함^^

    i += 1

print('1부터 10까지 짝수합: ', tot)

# break

num = 1

while True:

    if num % 5 == 0 and num % 7 == 0:
        #반복문 종료
        break

    num += 1

print('5와 7의 최소공배수:', num)

# continue

s, total = 1, 0

while s <= 10:

    s += 1

    if s % 2 == 1:
        continue

    total += s

print('1부터 10까지 짝수합 :', total)

