#a =1, b=1 , c= number= 2
#for c from 0 to 14 , a = a+b,c=c+1,loop
a=1
b=1
c=2
d="th"
for i in range(0,15):
  a=a+b
  c=c+1
  print (str(c)+d+str(a))
  b=a+b
  c=c+1
  print (str(c)+d+str(b))
    if i==13:
      break
