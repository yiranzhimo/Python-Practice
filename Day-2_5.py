class myclass():
    def getString(self):
        self.s = input("请输入：")
    def printString(self):
        print(self.s.upper())
test = myclass()
test.getString()
test.printString()
