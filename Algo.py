def recursive(Alphabet,n):
    if(n==0):
        return ['']
    else:
        res=[]
        for letter in Alphabet:
            res.extend([letter+element for element in recursive(Alphabet,n-1)])
        return res
# python3 crowbar.py -b https -u login -w crowbar.txt --username-field=login --password-field=password http://localhost/crowbar/traitement.php

# print(recursive(['a','b','c','d'],10))
def writeCrowbarFile(alphabet,n,filename):
    file = open(filename, "w")
    possibilities=recursive(alphabet,n)
    for poss in possibilities:
        file.write(poss+"\n")
    file.close()

writeCrowbarFile(['a','b','c'],3,'crowbar.txt')

def iterative(Alphabet,n):
    liste=Alphabet
    i=1
    while i<n:
        res=[]
        for elementliste in liste:
            for letter in Alphabet:
                res.append(elementliste+letter)
        liste=res
        i+=1
    return liste
# print(iterative(['a','b'],2))