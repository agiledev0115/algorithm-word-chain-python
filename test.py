import sys

def makeDictionary(words) :
    upperWords = list()
    for word in words :
        upperWords.append(word.upper().strip('\n'))
    return tuple(upperWords)

def findNextWords(word) :
    neighbours = set()
    wordLength = len(word)
    for letter in range(0, wordLength) :
        splitWord = list(word)
        for c in range(ord('A'), ord('Z') + 1) :
            value = chr(c)
            if value != word[letter] :
                splitWord[letter] = value
                neighbours.add("".join(splitWord))
    return neighbours

def makeChain(startWord, endWord, dictionary) :
    startWord, endWord = startWord.upper(), endWord.upper()
    chain = list()
    visitedWords = set()
    backtrack = dict()

    chain.append(startWord)
    visitedWords.add(startWord)

    while len(chain) > 0 :
        firstWord = chain.pop(0)
        for neighbour in findNextWords(firstWord) :
            if neighbour == endWord :
                curChain = [neighbour]
                while len(firstWord) > 0 :
                    curChain.insert(0, firstWord)
                    if firstWord in backtrack :
                        firstWord = backtrack[firstWord]
                    else :
                        firstWord = ""
                return curChain

            if neighbour in dictionary :
                if not neighbour in visitedWords :
                    chain.append(neighbour)
                    visitedWords.add(neighbour)
                    backtrack[neighbour] = firstWord

try:
    firstWord = sys.argv[1]
    secondWord = sys.argv[2]
except IndexError:
    print("Input words!!!")
else:
    file = open("words.txt","r")
    words = file.readlines()
    file.close()
    dictionary = makeDictionary(words)

    wordschain = makeChain(firstWord, secondWord, dictionary)

    for word in wordschain:
        print(word)