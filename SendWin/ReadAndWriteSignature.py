
class WriteSignature:
    def __init__(self,text):
        write = open("SendWin\\Signatur.txt","w")
        write.write(text)
        write.close()

class ReadSignature:
    def __init__(self):
        self.signature = []
        read = open("SendWin\\Signatur.txt","r")
        for line in read:
            self.signature.append(line)
        self.string = ''.join(self.signature)

    def returnSomething(self):
        return self.string