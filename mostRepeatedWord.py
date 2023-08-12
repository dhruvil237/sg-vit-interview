def mostRepeated(s):
    lisS = s.lower().split(' ')
    hashmap = {}
    for i in lisS:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    maxrepeated = max(hashmap.values())
    res = []
    for i in hashmap:
        if hashmap[i]==maxrepeated:
            res.append(i)
    return res
str1 = input()
print(mostRepeated(str1))