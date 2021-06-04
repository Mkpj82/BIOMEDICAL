dict={}
li=[]
l = list(map(str, input ().split()))
for word in l:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
        li.append(word)
print (len(li),end=" ")   
for i in li:
    print (dict[i],end="")
