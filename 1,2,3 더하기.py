# 1, 2, 3 더하기
# An = A(n-1) + A(n-2) + A(n-3)임을 이용
list = []
Answer = []

Answer.append(1)
Answer.append(2)
Answer.append(4)

num = int(input())
for i in range(0, num):
    list.append(int(input()))

for i in range(3, max(list)):
    Answer.append(Answer[i-1]+Answer[i-2]+Answer[i-3])

for i in list:
    print(Answer[i-1])
