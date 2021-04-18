import re, os
import re
def translate(sequence):
    dict()
    protein = {
    'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
    'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',
    'TTA':'L', 'TCA':'S', 'TAA':'O', 'TGA':'X',
    'TTG':'L', 'TCG':'S', 'TAG':'U', 'TGG':'W',
    'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',
    'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',
    'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
    'CTG':'L', 'CCG':'P', 'CAG':'Z', 'CGG':'R',
    'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',
    'ATC':'I', 'ACC':'T', 'AAC':'B', 'AGC':'S',
    'ATA':'J', 'ACA':'T', 'AAA':'K', 'AGA':'R',
    'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
    'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',
    'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',
    'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',
    'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G',
    }
    pro = ''
    for i in range(0, len(sequence), 3):
        pro = pro + protein[sequence[i:i + 3]]
    return pro

f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
lines = f.readlines()

result = []
pro=''
for i in range(0, len(lines)):
    if lines[i].startswith(">"):
        if 'unknown function' in lines[i]:  #  Find the unknown function
            result.append(re.findall(r'(>.+?)(?:_| )', lines[i])[0])
            bases = ''
            for n in range(0, len(lines[i:-1])):
                if not lines[i+n+1].startswith(">"):  #go to the next line
                    bases += lines[i+n+1][:-1]
                    seq = translate(bases)#translate, get the protein sequence
                else:
                    break
            seq += "\n"
            result.append(seq)

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
