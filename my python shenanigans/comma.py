spa = ["a", "b", "c"]

def commalist(spam):
    try:
        q = len(spam) - 1
        r = ""
        for word in spam[0: -2]:
            word = str(word)
            r += word + ", "
        m = spam[-2] + " and " + spam[-1]
        r += m
        return r
    except:
        return "Empty list"



print(commalist(spa))
    

    
