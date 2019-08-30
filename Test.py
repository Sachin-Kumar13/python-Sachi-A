n = int(input())
res =list(map(int,input().split()))


for i in res:
    d=max(res.count(i))
    print(d)

