# https://atcoder.jp/contests/abc352/tasks/abc352_a

N, X, Y, Z = map(int, input().split())

if Y < X:
  if Z < X and Z > Y:
    print("Yes")
  else:
    print("No")
else:
  if Z < Y and Z > X:
    print("Yes")
  else:
    print("No")
