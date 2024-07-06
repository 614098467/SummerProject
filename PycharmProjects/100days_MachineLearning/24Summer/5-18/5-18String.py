

class MyString(object):

    def __init__(self,string):
        self.string = string

    def StringLength(self):
        return len(self.string)

    def AddString(self,s):
        self.string = self.string+"\t"+s

    def IsEuqal(self,s):
        return self.string == s

    def Index(self,s):
        for i in range(len(self.string)):
            if self.string[i] == s:
                return i
        return -1

    def __str__(self):
        return self.string


string = MyString("stt")
string.AddString("hello")
print(string.StringLength())
print(string.Index('t'))
print(string)
