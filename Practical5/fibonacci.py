# a = 1, b = 1 , c = round number = 2
# for c from 0 to 14 , a = a+b,c=c+1, loop
a = 1
b = 1
c = 2
print("1st 1\n2nd 1")  # print the first and second number which we have set.
for i in range(0, 15):
    a = a+b  # now a becomes the next nunmber
    c = c+1
    print(str(c)+"th "+str(a))  # print number
    b = a+b
    c = c+1
    print(str(c)+"th "+str(b))  # again, but this time b is the next number
    # now, the first number a and second number b become separately the third and forth number， and this program will repeat like this.
    if i == 10:
        break
