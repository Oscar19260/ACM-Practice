# https://codeforces.com/contest/158/problem/B

def ntaxis(n, s):
  taxis = 0
  agroup = 0
  i, j = 0, n-1

  if sum(s) <= 4:
    taxis += 1
    return taxis

  while i != j+1:
    if agroup == 0:
      agroup += s[j]
    if agroup == 4:
      taxis += 1
      j -= 1
      agroup = 0
    elif i == j:
      taxis += 1
      break
    else:
      agroup += s[i]
      if agroup == 4:
        taxis += 1
        j -= 1
        i += 1
        agroup = 0
      elif agroup > 4:
        taxis += 1
        j -= 1
        agroup = 0
      else:
        i += 1
  return taxis

n = int(input())
s = list(map(int, input().split()))
s.sort()
print(ntaxis(n, s))