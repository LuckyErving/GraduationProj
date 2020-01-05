





#iciba 翻译函数  
def trans(self, word):  
    url = 'http://www.iciba.com/index.php?a=getWordMean&c;=search&word;=' + word  
    try:  
        req = requests.get(url)  
        req.raise_for_status()  
        info = req.json()  
        data = info['baesInfo']['symbols'][0]  
        assert info['baesInfo']['symbols'][0]  
        # 去除没有音标的单词  
        assert data['ph_am'] and data['ph_en']  
        # 去除没有词性的单词  
        assert data['parts'][0]['part']  
    except:  
        return ('none','none')  
    ph_en = ' 英 [' + data['ph_en'] + ']'  
    ph_am = ' 美 [' + data['ph_am'] + ']'  
    ex = ''  
    for part in data['parts']:  
        ex += part['part'] + ';'.join(part['means']) + ';'  
    return ph_en+ph_am, ex    
#调用翻译函数，保存中文到数据库  
for i in NewWord.select():  
    i.explanation = str(t.trans(i.name)[1])  
    i.save()


import csv  
#提取所有数据库内容生成迭代对象 yield ~ 好好看看如何使用  
def extract()  
    pass  
    for word in NewWord.select():  
        for i in [word.name, word.explanation, word.frequency]:  
            datas.append(i)     
    yield datas  
#保存函数   
def save(data):  
    with open('words.csv', 'a+', errors='ignore', newline='')as f:  
        csv_writer = csv.writer(f)  
        csv_writer.writerow(data)  
#主程序  
datas = extract() #yeild 迭代对象  
while True:  
    try:  
        data = next(datas)  
    except:  
        break  
    save(data)

