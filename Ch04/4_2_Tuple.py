"""
날짜 : 2021/04/27
이름 : 김예슬
내용: 파이썬 자료구조 tuple 실습 교재 p92
"""

#Tuple(고정 list) 생성
tuple1 = (1, 2, 3, 4, 5) #list는 [ ]를 쓰고 Tuple은 ( )를 쓴다
print('tuple1 type:',type(tuple1))
print('tuple1[0]:', tuple1[0])
print('tuple1[1]:', tuple1[1])
print('tuple1[2]:', tuple1[2])


tuple2 = ('서울', '대전', '대구', '부산', '광주')
print('tuple2 type:', type(tuple2))
print('tuple2[0] : %s ' % tuple2[0])
print('tuple2[4] : {}'.format(tuple2[4]))


#tuple 수정, 추가, 삭제 x
tuple3 = 1, 2, 3, 4, 5
print('tuple3 type:', type(tuple3))

#tuple3[1] = 7 에러발생 튜플 수정불가
#tuple3[4[ = [] # 에러발생 튜플 삭제불가
