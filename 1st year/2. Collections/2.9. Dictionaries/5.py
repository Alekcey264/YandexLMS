text = input()
nums = dict()
for letter in text:
    if letter == " ":
        continue
    nums[letter] = nums.get(letter, 0) + 1
nums = sorted(list(nums.items()), key=lambda x: x[1], reverse=True)
chosen_nums = list()
for i in range(len(nums)):
    chosen_nums.append(int(nums[i][0]))
    if nums[i + 1][1] != nums[i][1]:
        break
print(*sorted(chosen_nums), sep=" ")