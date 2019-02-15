import operator 
file1= open("Book1.txt","r")
file2= open("Book2.txt","r")
file3=open("Book3.txt","r")
def unique_words():
   
    textWithoutStops = RemStopWords(file1, file2,file3)

    wordCount = {}
    for word in textWithoutStops.split(' '):  
        if not word in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
    
    sortedWordCount = sorted(wordCount.items(), key=operator.itemgetter(1))
    sortedWordCount = sortedWordCount[::-1]

    if len(sortedWordCount) > 10:
        sortedWordCount = sortedWordCount[:10]

    return sortedWordCount
print(unique_words())
