def anagrams(word, words):
    # your code here
    empty = []
    full = []
    sortWord = sorted(word)
    for i in range(len(words)):
        if sorted(words[i]) == sortWord:
            full.append(words[i])

    if not full:
        return empty
    else:
        return full

print (anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))



