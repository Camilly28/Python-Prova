t = [int(i) for i in input().split()]

for i in t:
  l = ''
  m = ''
  flag = 0
  for j in range(i):
        if i % 2 == 0:
          l += '*'
          flag += 1
          if flag == i:
            print(l)
        else:
          m += '.'
          flag += 1
          if flag == i:
            print(m)
