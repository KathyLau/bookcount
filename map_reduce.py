f = open("book.txt","r")
story = f.read()

book = [word.strip('(",.)!?-') for word in story.split()]

def freq(word1):
    return len(filter(lambda word2: word2 == word1, book))

def freqGroup(group):
    return str(reduce(lambda a,b: a + b, [freq(word) for word in group]))

print freq("Chapter")
