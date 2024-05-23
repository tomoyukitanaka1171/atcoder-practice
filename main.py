# https://atcoder.jp/contests/abc352/tasks/abc352_c

N = int(input())
array = []
for n in range(N):
  a = list(map(int, input().split()))
  array.append(a)

ans = 0
m = 0
for n in range(N):
  m = max(m, array[n][1] - array[n][0])

for n in range(N):
  m += array[n][0]
  
print(m)
