def solve(num_heads,num_legs):
    for i in range(num_heads+1):
        j = num_heads - i
        if 2*i + 4*j == num_legs:
            return i,j
num_heads = 35
num_legs = 94
print(solve(num_heads,num_legs))