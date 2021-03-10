a = 190784
b = 260103
c = 100321
d = b - c
e = b - a
if d>e:
  print ("d is greater")
if d<=e:
  print ("e is greater")

X=True
Y=False
Z=(X and not Y) or (Y  and not X)
print (Z)

W=X!=Y
print(W==Z)
