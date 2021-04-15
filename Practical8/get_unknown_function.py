import re,os
f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
lines=f.readlines()
result = []
for i in range(0, len(lines)):
    if lines[i].startswith(">"):  
        if 'unknown function' in lines[i]:  #  Find the unknown function
            result.append(re.findall(r'(>.+?)(?:_| )', lines[i])[0])
            bases = ''
            for n in range(0, len(lines[i:-1])):
                if not lines[i+n+1].startswith(">"):  # Skip the description line
                    bases += lines[i+n+1][:-1]
                else:
                    break
            bases += "\n"
            result.append(bases)
for i in range(0, len(result)):   
    if result[i].startswith(">"):
        result[i] += "  "
        result[i] += str(len(result[i+1]) - 1)
        result[i] += "\n"

with open('unknown_function.fa','w') as output:#creat a new .fa file
    unknown_function = open('unknown_function.fa', "w")
for line in result:
    unknown_function.write(line)   #write results in
unknown_function.close()