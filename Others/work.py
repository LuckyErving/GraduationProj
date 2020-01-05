import re
from collections import Counter #计数器 

# def _open_file(filename):#打开文件，返回所有单词 list  
with open('article.txt','r',encoding='utf-8')as f:  
    raw_words = f.read()          # Read all the words to string
    low_words = raw_words.lower()  
    words = re.findall('[a-z]+',low_words) #正则 re 找到所有单词  


exclude_list=['is','the','of']
NUMBERS=10
# def _filter_words(raw_words,count=NUMBERS):#载入未处理的所有单词列表 和 默认 count 值  
new_words = []  

#找出非 exclude 和 长度大于 1 的单词 -> new_words  
for word in range(len(words)):
    if words[word] not in exclude_list and len(words[word]) > 1:
        new_words.append(words[word])  
            

print('Begin......')
# print(words)
print()
print(new_words)   # Why NULL???
print()
# c = Counter(words) #list new_words without "exclude_list"
c = Counter(new_words)
print(c.most_common(500)) #拿到出现次数最多的 5000 单词，返回从大到小的排序 list[(and,1),....]