n, B = list(map(int, input().strip().split()))
T = 0

sequence = []

for x in range(n):
  if (x+1) % 2 == 0:
    sequence.append(int(2**(x+1) + 1))
  elif (x+1) % 2 == 1:
    sequence.append(int(3**(x+1) + 1))

total = 0
bottom_range = 0
top_range = 10000
mid_range = 5000
for x in range(n):
  total += (sequence[x]**(n - (x + 1))) * T
if total >= B:
  T = 5000
  while 1:
    total = 0
    for x in range(n):
      total += (sequence[x]**(n - (x + 1))) * T
    if T > 10000:
      T = -1
      break
    elif total > B:
      break
    else:
      T += 1
else:
  T = 0
  while 1:
    total = 0
    for x in range(n):
      total += (sequence[x]**(n - (x + 1))) * T
    if total > B:
      break
    else:
      T += 1


print(T)