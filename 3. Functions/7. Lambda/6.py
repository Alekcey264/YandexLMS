def smart_search(*arr, func):
    if type(arr[0]) is int:
        return tuple(filter(func, arr))
    else:
        return tuple(filter(lambda x: x[0].isupper(), arr))
    
print(smart_search(1, 2, 3, 5, 12, func=lambda x: x % 2))
print(smart_search('The', 'quick', 'brown', 'Fox', 'jumps', 
                   'over', 'the', 'Lazy', 'Dog', func=lambda x: x))