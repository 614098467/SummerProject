

class SequenceTable(object):
    def __init__(self):
        self.SequenceTable = []
    def GetSize(self):
        return len(self.SequenceTable)
    '''增'''
    def Add(self,num):
        self.SequenceTable.append(num)
    '''插入'''
    def Insert(self,index,num):
        if index < len(self.SequenceTable):self.SequenceTable.insert(index,num)
        else:print("Index out of range")
    '''删'''
    def DeleteByValue(self,value):
        return self.SequenceTable.remove(value)
    def DeleteByIndex(self,index):
        if index < len(self.SequenceTable):self.SequenceTable.pop(index)
        else:print("Index out of range")
    '''改'''
    def Change(self,index,value):
        if index < len(self.SequenceTable):self.SequenceTable[index] = value
        else:print("Index out of range")
    '''查'''
    def Get(self,index):
        if index < len(self.SequenceTable):return self.SequenceTable[index]
        else:return -1
    def In(self,value):
        return value in self.SequenceTable
    def GetAll(self):
        return self.SequenceTable



seqta = SequenceTable()
seqta.Add(1)
seqta.Add(2)
seqta.Add(3)
seqta.Insert(1,2)
# seqta.DeleteByIndex(1)
seqta.Change(0,5)
print(seqta.GetAll())


