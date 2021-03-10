#a =1, b=1 , c= number= 2
#for c from 0 to 14 , a = a+b,c=c+1,loop
a=1
b=1
c=2
print ("1st 1\n2nd 2")  #print the first and second number
for i in range(0,15):
  a=a+b #generate the next number
  c=c+1
  print (str(c)+"th "+str(a)) #print number
  b=a+b
  c=c+1
  print (str(c)+"th "+str(b)) #again
  if i==13:
      break
