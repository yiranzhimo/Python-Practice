words = input("请输入 words:")
words_new = words.split(" ")
words_result = list()
for i in words_new:
    if i not in words_result:
        words_result.append(i)
words_result.sort()
str = " ".join(words_result)
print(str)    