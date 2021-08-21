# Enter your code here. Read input from STDIN. Print output to STDOUT
nums = []

for i in range(0, 4):
    j = int(input())
    nums.append(j)

print(pow(nums[0], nums[1]) + pow(nums[2], nums[3]))
