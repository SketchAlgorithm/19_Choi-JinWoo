#다익스트라 Dijkstra
import sys
input = sys.stdin.readline

graph = []
V, E = map(int, input().split(" "))
visited = [False for i in range(V)] #노드 방문 여부
dist = [1e6 for i in range(V)]      #최단 거리 메모라이징
start = int(input())-1

for i in range(0, V):       #그래프 구현할 2차원 행렬 리스트 생성
    graph.append([1e6 for j in range(V)])
    graph[i][i] = 0
for i in range(0, E):
    u, v, w = map(int, input().split(" "))
    graph[u-1][v-1] = w




def SmallIndex(start):
    min = 1e6
    index = 0
    for i in range(len(dist)):
        if start is i: continue
        if visited[i]:continue
        if graph[start][i]<min:
            min = graph[start][i]
            index = i
    return index


def Dijkstra(start):
    visited[start] = True
    for i in range(0, len(graph)):
        dist[i] = graph[start][i]
    for x in range(len(graph)-2):    #첫 노드는 25행에서 방문하였고, 마지막 노드 굳이 방문하지 않아도 됨
        start = SmallIndex(start)
        visited[start] = True
        for i in range(len(graph)):
            if dist[i]>graph[start][i]+dist[start]:
                dist[i] = graph[start][i]+dist[start]





Dijkstra(start)
# for i in range(0, len(graph)):#그래프 출력
#     print(graph[i])
for answer in dist:
    if answer == 1e6:
        print("INF")
    else: print(answer)
