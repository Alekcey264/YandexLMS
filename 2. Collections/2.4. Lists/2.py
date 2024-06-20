nums = list()
num = input()
while num != "0":
    nums.append(int(num))
    num = input()
new_nums = list()
for item in nums:
    if item % len(nums) == 0:
        new_nums.append(item)
print(new_nums)