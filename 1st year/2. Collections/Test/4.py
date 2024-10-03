first_string = input().split()
second_string = input().split("_|_")
third_string = input().split("_0_")
for word in first_string:
    print(word, ":", sep="")
    second_words_list = []
    for word2 in second_string:
        if len(list(word2.lower())) != len(list(set(word2.lower()))) and len(word2) <= len(word):
            second_words_list.append(word2.capitalize())
    print(*second_words_list, sep="* ")
    third_words_list = []
    for word3 in third_string:
        if word.lower() < word3.lower() and word3.islower():
            third_words_list.append(word3.upper())
    print(*third_words_list, sep="*" + word[-2].upper() + "*")