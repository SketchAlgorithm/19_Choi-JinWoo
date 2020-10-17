N, K = map(int, input().split(" "))
graph = [[] for i in range(N+1)]
degree = [0 for i in range(N+1)]

q = []
for _ in range(K):
    A, B =  map(int, input().split(" "))
    graph[A].append(B)
    degree[B] = degree[B] + 1

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while q:    # isEmpty(queue) == !queue
    X = q.pop(0)
    for i in graph[X]:
        degree[i]-=1
        if degree[i] == 0:
            q.append(i)
    print(X, end=' ')
