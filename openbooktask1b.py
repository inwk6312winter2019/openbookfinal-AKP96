
logfile = open("Book1.txt","r")
def count_the_article():
    counts = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    words = logfile.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(count_the_article())

