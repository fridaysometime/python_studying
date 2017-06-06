import re

para=open('english_para.txt','r')
start=para.read()

reg=re.compile('\b?([A-Za-z]+)\b?')
words=reg.findall(start)
print(words)

wordDict=dict()
for word in words:
    if word.lower() in wordDict:
        wordDict[word.lower()]+=1
    else:
        wordDict[word]=1

for key,value in wordDict.items():
    print('%s:%s'%(key,value))
