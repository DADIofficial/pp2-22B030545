class modifystring:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())

k = modifystring()
k.getString()
k.printString()