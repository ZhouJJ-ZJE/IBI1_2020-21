n = 84  # infected number at the beginning
r = 1.2  # set an r rate
for i in range(1, 10):
    n = n * r + n
# after one round of infect, the infected number should be previous number+previous number*rate
    if i == 5:
        # print result
        print("the total number of individuals infected after 5 generations is " + str(n))
        break
