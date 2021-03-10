a = 190784
b = 260103
c = 100321
d = b - c
e = b - a
X = d>e
Y = d<=e
Z = (X and not Y) or (Y and not X)
if X = true:
  print "d is greater"
