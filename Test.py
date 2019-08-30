n = int(input())
res =list(map(int,input().split()))
lst=[]
for i in res:
    lst.append(res.count(i))

print(max(lst))


