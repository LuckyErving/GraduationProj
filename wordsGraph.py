# Find the most-similar words
# Just Do IT

import json
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
fileWords=open('CET4+6.txt','r')
testWords=open('testWords.txt','r')

str=fileWords.read()
str1=testWords.read()
# 换行符会占一个位想

# 用string数组存每个单词，导入时以换行符为分界线
words=[]
testW=[]

words=str.split('\n')
testW=str1.split('\n')

print(testW)
# print(words)

# list创建二维数组
words_shingling_3=[['' for i in range(20)] for j in range(8028)]
testW_shingling_2=[['' for i in range(20)] for j in range(20)]

# 存sim值
testW_simVal=[[-1 for i in range(20)] for j in range(20)]
# words_simValues=[[-1 for i in range(8028)] for j in range(8028)]
wordsSim=[-1 for i in range(4014*8029)]

# Shingling 分词
def Shingling(wordlist, words_shingling, k):
    print('Shingling begins......')
    numWords=len(wordlist)
    for i in range(numWords-1):
        s=wordlist[i]
        
        if len(s)<= k:
            words_shingling[i][0]=s
        else:
            numSets=len(s)-(k-1)
            for j in range(numSets):
                ss=s[j:j+k]
                words_shingling[i][j]=ss

# Jaccard similarity 计算相似度：Sim(C1, C2) = |C1∩C2|/|C1∪C2|
def JacSim(wordlist, words_shingling, words_simValues, k):
    print('Begin JacSim calculating......')
    for i in range(len(wordlist)-1):
        N=U=0
        j=i+1
        while j<len(wordlist)-1:
            if len(wordlist[i])<k & len(wordlist[j])<k:
                U=2
                
            elif len(wordlist[i]) < k:
                U=len(wordlist[j])-1
                
            elif len(wordlist[j]) < k:
                U=len(wordlist[i])-1
                
            else:
                U=len(wordlist[i])+len(wordlist[j])-(k+1)
                
            for m in range(len(wordlist[i])-(k-1)-1):
                for n in range(len(wordlist[j])-(k-1)-1):
                    if words_shingling[i][m] == words_shingling[j][n]:
                        N+=1
            # words_simValues[i][j]=N/U  改为存到一维数组中
            l=1
            wordsSim[l]=N/U
            l+=1
            N=U=0
            j+=1


# Shingling(testW,testW_shingling_2,2)
Shingling(words,words_shingling_3,3)

# print(testW_shingling_2)

# JacSim(testW,testW_shingling_2,testW_simVal,2)
# JacSim(words,words_shingling_3,words_simValues,3)
JacSim(words,words_shingling_3,wordsSim,3)


# print(testW_simVal)

print()
print('testing......')


# 存储可否改善？？ 按以下方法，浪费了一半空间，实际需要8028*8027/2 的空间（约32 000 000），实为上三角矩阵，最好进行压缩存储
# words_simValues=[[0 for i in range(len(words))] for j in range(len(words))] 
# print(words_simValues)
# JacSim(words_shingling_3, words_simValues)


with open('CET4+6(SimValue).txt','w') as fw:
    # fw.write(json.dumps(words_simValues))
    fw.write(json.dumps(wordsSim))

'''
with open('xxx.txt','r') as fr:
    content=json.loads(fr.read())

'''


fw.close()
# fr.close()
fileWords.close()
testWords.close()



