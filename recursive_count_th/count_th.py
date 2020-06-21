'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # wordLen = len(word)
    # th = "th"
    # thLen = len(th)

    # if wordLen < thLen:
    #     return 0

    # if word[0 : thLen] == th:
    #     return count_th(word[thLen - 1:], th) + 1
    
    # return count_th(word[thLen - 1:], th)
    
    wordLen = len(word)
    th = "th"
    thLen = len(th)

    if wordLen < thLen:
        return 0
    if word[0:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
  
