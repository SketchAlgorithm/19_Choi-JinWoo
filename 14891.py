List = []   #톱니바퀴 정보를 저장
flag = [2, 2, 2, 2] #톱니 바퀴의 3시방향의 index를 저장
check = [0, 0, 0]  #옆 톱니바퀴와 서로 같으면 0, 다르면 1


for i in range(4):
    str = input()
    List.append(list(map(int, (list(str)))))

rotation = int(input())

for i in range(0, rotation):
    num, direction = map(int, input().split())
    num -= 1    #인덱스는 0부터 시작하므로 -1
    for j in range(0, 3):
        if List[j][flag[j]] != List[j+1][(flag[j+1]+4)%8]:
            check[j] = 1
        else:
            check[j] = 0

    flag[num] = (flag[num] - direction) % 8

    j = num + 1
    while True: #   num 기준 오른쪽
        if j>3:
            break
        if abs(j-num)%2 is 0:
            if check[j-1] is 1:
                flag[j] = (flag[j] - direction) % 8
            else:
                break
        else:
            if check[j-1] is 1:
                flag[j] = (flag[j] + direction) % 8
            else:
                break
        j += 1

    j = num - 1
    while True: #   num 기준 왼쪽
        if j<0:
            break
        if abs(j-num) % 2 is 0:
            if check[j] is 1:
                flag[j] = (flag[j] - direction) % 8
            else:
                break
        else:
            if check[j] is 1:
                flag[j] = (flag[j] + direction) % 8
            else:
                break
        j -= 1
    # print()
    # print(flag)
    # print("",check)
# print()
# print()

result = 0
for i in range(0, 4):
    if List[i][(flag[i]-2)%8] is 1:
        result+=2**i
print(result)


