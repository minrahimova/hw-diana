x = []

y = []

for i in range(8):

 x1, y1 = list(map(int, input().split()))

 x.append(x1)

 y.append(y1)

Is_right = False

for i in range(7):

 for k in range (i + 1, 8):

   if x[i] == x[k] or y[i] == y[k] or abs(x[i] - x[k]) == abs(y[i]-y[k]):

     Is_right = True

if Is_right:

 print("YES")

else:

 print('NO')