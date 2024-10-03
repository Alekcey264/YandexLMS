word1, word2 = input(), input()
check_word = word2 + word2
if word1 in check_word:
    for i in range(len(check_word)):
        if check_word[i:len(word2) + i] == word1:
            print(i)
            break
    else:
        print("NO")
else:
    print("NO")