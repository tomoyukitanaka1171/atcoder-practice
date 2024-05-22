# https://atcoder.jp/contests/abc352/tasks/abc352_b

S = list(input())
T = list(input())

memo = 0
ans = []
for i in range(len(T)):
  if S[memo] == T[i]:
    ans.append(i+1)
    memo +=1

print(*ans)
