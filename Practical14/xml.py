from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

# parse xml file
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

dic={}
for term in terms:    
    dic[term.getElementsByTagName("id")[0].firstChild.data]=[]
#find 'is a' and 'id'
for term in terms:
    IS_A = term.getElementsByTagName("is_a")
    ID = term.getElementsByTagName("id")
    for is_a in IS_A:
        dic[is_a.firstChild.data].append(ID[0].firstChild.data)

        
#design a function to count the number of child node
def countlen(m):
    for i in range(len(m)): 
        if m[i] not in listm: #listm shoud be empty at the beginning, and avoid add the same element twice
            listm.append(m[i])
            countlen(dic[m[i]])  #add every element in the list, thus, the len of the list is the number of child nodes
    return len(listm) 

def count(n):
    for term in terms:
        defstr=term.getElementsByTagName('defstr')   #find defstr, in which line exist the molecule we want          
        if n in defstr[0].firstChild.data:
            ID=term.getElementsByTagName('id')
            l=dic[ID[0].firstChild.data] #put data of the dic into a list because the function above is designed for list len count
            c=countlen(l)#use the function above to count len
    return c


#run the function     
listm=[] #clear the list, making sure it's empty 
DNA=count('DNA')
listm=[]
RNA=count('RNA')
listm=[]
protein=count('protein')
listm=[]
glycoprotein=count('glycoprotein')

#print the output
print("the number of childNodes for each DNA-related gene ontology term: " + str(DNA))
print("the number of childNodes for each RNA-related gene ontology term: " + str(RNA))
print("the number of childNodes for each protein-related gene ontology term: " + str(protein))
print("the number of childNodes for each glycoprotein-related gene ontology term: " + str(glycoprotein))

#draw a pie chart
molecules = {"DNA": DNA, "RNA": RNA,
             "Protein": protein, "Glycoprotein": glycoprotein}
labels = molecules.keys()
sizes = molecules.values()
explode =(0, 0, 0, 0)
fig1, ax1 = plt.subplots()    
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
ax1.set(title ='The number of childNodes')
plt.show()
