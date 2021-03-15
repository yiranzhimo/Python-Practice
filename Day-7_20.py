class test():
    def test(self):
        x = int(input("请输入数字:"))
        for i in range(0,20):
            if i%x == 0:
                print(i)
Test = test()
#把类实例化
Test.test()


