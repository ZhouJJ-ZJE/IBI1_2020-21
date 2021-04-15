import re, os
from DNA_to_protein import translate#use the function from another program

f = open()
lines = f.readlines() 

result = []
for i in range(0, len(lines)):
    if lines[i].startswith(">"):  
        if 'unknown function' in lines[i]:  #  Find the unknown function
            result.append(re.findall(r'(>.+?)(?:_| )', lines[i])[0])
            bases = ''
            for n in range(0, len(lines[i:-1])):
                if not lines[i+n+1].startswith(">"):  # Skip the description line
                    bases += lines[i+n+1][:-1]
                    pro = translate(bases)#translate, get the protein sequence
                else:
                    break
            pro += "\n"

        result.append(pro)

for i in range(0, len(result)):   
    if result[i].startswith(">"):
        result[i] += "  "
        result[i] += str(len(result[i+1]) - 1)
        result[i] += "\n"

with open('unknown_protein.fa','w') as output:
    unknown_function = open('unknown_protein.fa', "w")
for line in result:     
    unknown_function.write(line)
unknown_function.close()

