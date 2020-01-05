from peewee import *

db = SqliteDatabase('voca.db')  
class NewWord(Model):  
# 单词名  
    name = CharField()  
# 解释  
    explanation = TextField(default='')  
# 词频  
    frequency = IntegerField(default=0)  
# 音标  
    phonogram = CharField(default='')  

class Meta:  
    database = db

    def insert_data(self, words_times):  
    # 向数据库内插入数据  
        for word,fre in words_times:              
            word_ins = NewWord.create(name = word , frequency = fre) #直接调用 create  
            book.is_analyzed = True  
            book.save()
            print('ok')

