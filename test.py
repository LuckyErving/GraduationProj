
s=''
for i in range(100):
    s=s+str(i)+' '
print(s)
print(s[20])


# Try to find the similar words with shingling in a easy way
words=[]
wordsFile=open('CET4+6.txt','r')
str=wordsFile.read()
words=str.split('\n')
print(words[3])