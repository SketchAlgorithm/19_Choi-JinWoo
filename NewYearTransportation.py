n, t = map(int, input().split())
a = list(map(int, input().split()))
start = 0
while start<t-1:
    start+=a[start]
if start is t-1:
    print("YES")
else:
    print("NO")





