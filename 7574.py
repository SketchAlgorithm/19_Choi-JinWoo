import sys
def getParents(parentList, point):
    if parentList[point] == point:
        return point
    else:
        return getParents(parentList, parentList[point])

def unionParent(parentList, point1, point2):
    parent1 = getParents(parentList, point1)
    parent2 = getParents(parentList, point2)

    if parent1 < parent2:
        parentList[parent2] = parent1
    else:
        parentList[parent1] = parent2

N, r = map(int, sys.stdin.readline().split(" "))
# graph = [[-1]*N for _ in range(N)]

point = []
graph = {}
parents = [i for i in range(N)]
for i in range(N):
    (x, y) = map(int, sys.stdin.readline().split(" "))
    point.append((x, y))
    # graph[(x, y)] = []

d = int(sys.stdin.readline())

for i in range(0, N):
    p1 = point[i]
    for j in range(i+1, N):
        p2 = point[j]
        if (p1[0]<=p2[0] and p2[0] <= p1[0]+r) or (p2[0]<=p1[0] and p1[0] <= p2[0]+r):
            if abs(p1[1]-p2[1]) <= r+d:
                unionParent(parents, i, j)
                # graph[p1].append(p2)
                # graph[p2].append(p1)

        elif (p1[1]<=p2[1] and p2[1] <= p1[1]+r) or (p2[1]<=p1[1] and p1[1] <= p2[1]+r):
            if abs(p1[0]-p2[0]) <= r+d:
                unionParent(parents, i, j)
                # graph[p1].append(p2)
                # graph[p2].append(p1)

max = -1
for i in range(1, N):
    if parents[i] == 0:
        max = max> point[i][0] +point[i][1]+2*r and max or point[i][0] +point[i][1]+2*r

print(max)
# print(parents)
# print(graph)