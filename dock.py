'''
Docker Assignment 
Cloud Computing Class
Author: Athulya Ganesh 
'''

import socket 
import re 
import os

cwd = os.getcwd() 
countif=0
countlim=0

d=dict() 

def test(d):
  ret = str(max(d, key = d.get)+": "+str(d[max(d, key = d.get)])+" times\n")
  del d[max(d, key = d.get)]
  return ret 


with open(cwd+"/data/IF.txt", "r") as f:
    data = f.read() 
    data = data.strip()
    data = data.lower()
    words = data.split()
    countif+= len(words)
    
    for word in words:
        word = filter(None, re.split(r'\W|\d', word))
        word = "".join(word)
        if word in d:
            d[word]+=1
        else:
            d[word]=1
        
f.close()

with open(cwd+"/data/Limerick.txt", "r") as f:
    data = f.read() 
    words = data.split() 
    countlim+= len(words)
f.close() 


res = open('output/result.txt','w')
res.writelines("\nFilenames: "+ str(os.listdir(cwd+'/data'))+"\n\n")
res.writelines("Number of words in IF.txt = "+str(countif)+"\n")
res.writelines("Number of words in Limerick.txt = "+str(countlim)+"\n\n")
res.writelines("Grand Total Words in IF.txt and Limerick.txt = "+str(countif+countlim)+"\n\n")
res.writelines("Most occuring words in IF.txt: \n"+test(d)+test(d)+test(d))
    
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

res.writelines("\nIP Address of my computer: "+IPAddr+"\n\n")
res.close()  

with open("output/result.txt", "r") as f:
    content = f.read() 
print(content)

f.close()