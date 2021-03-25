nums = list(input("请输入数字："))
nums_new = list(set(nums))
nums_new.sort(reverse = True)
print(nums_new[1])