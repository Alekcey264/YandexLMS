trees = list()
text = input()
while text:
    trees.append(text.split(" : "))
    text = input()
num = int(input())
for item in trees:
    for i in range(len(item)):
        if int(item[i]) < num:
            print('0', end="\t")
        else:
            print(int(item[i]), end="\t")
    print()