n=84 #infected number
r=1.2 #rate
for i in range (1,10):
  n=n*r+n #one time of infect
  if i==5:
    print ("the total number of individuals infected after 5 generations is " + str(n)) #print result
    break
  
