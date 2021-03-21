def test():
    return 5/0
try:
    test()
except:
    print("Exception")