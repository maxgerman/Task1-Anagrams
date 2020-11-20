def reverse(input_string):
    temp = []
    for i, word in enumerate(str.split(input_string)):
        rev_word = [""] * len(word)
        letters=[]
        symbols=[]
        for ind, char in enumerate(word):
            if not char.isalpha():
                rev_word[ind]=char # adding non-letters to result at their original places
            else:
                letters.append(char) # adding letters to a separate list
        # adding reversed letters to the result at their new places
        letind = 0
        letters.reverse()
        for pos, char in enumerate(rev_word):
            if (char == ""):  #add a letter if the place is "free" from symbol/number
                rev_word[pos] = letters[letind]
                letind+=1
        temp.append ("".join(rev_word)) #append resulting words one by one; convert rev_word from list to string

    output = " ".join(temp) #convert list to string
    return output

if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("",""),
    ]

    for text, reversed_text in cases:
        assert reverse(text) == reversed_text

    while (True):
        inp = input("Enter string:")
        print (reverse(inp))
