# -*-coding:utf-8-*-
import string
class senseWord():
    def __init__(self):
        self.list=[]
        self.word=[]
        inputfile=file('filtered_word.txt','r')
        self.list.extend(
            lines.decode('utf-8').encode('gbk') for lines in inputfile.readlines()
        )

        inputfile.close()
        self.list=map(string.strip,self.list);
       
    def checkWord(self,word):
        flag=False
        for words in self.list:
            if words in word:
                self.word.append(words)
                flag= True
        return flag

    def getWord(self):

        return self.word

if __name__=='__main__':
    myCheck=senseWord()
    while ipstr := str(raw_input()):
        if (myCheck.checkWord(ipstr)):
            senseList=myCheck.getWord()
            for items in senseList:
                length=len(items.decode('gbk'))
                torep='*';
                for _ in range(1,length):
                    torep+='*'
                ipstr=ipstr.replace(items,torep)
        senseList=myCheck.getWord()



