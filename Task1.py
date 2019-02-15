
import string


def unique_words(filename):

    hist = histogram(filename)
    mylist = list(hist)
    mylist =  list(dict.fromkeys(mylist))

    return mylist



def count_the_article(filename):

    count = 0
    list_2 = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    hist = histogram(filename)
    for item in list_2:
        if item in hist:
            count += 1

    return count


def sorted_words(filename):

    hist = dict()
    file = open(filename)
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = len(word)
    lst = [(value, key) for key, value in hist.items()]
    lst.sort(reverse=True)

    return lst


def character_word_count(filename):

    hist = dict()
    file = open(filename)
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = len(word)
    return hist

def starts_with_vow(filename):

    tup = ("a", "e", "i", "o", "u")
    hist = dict()
    file = open(filename)
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            if word[0] in tup:
                hist[word] = hist.get(word, 0) + 1

    return len(hist)





def histogram(filename):

    hist = dict()
    file = open(filename)
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = hist.get(word, 0) + 1

    return hist

fname = 'Book1.txt'
print(unique_words(fname))
print(count_the_article(fname))
print(sorted_words(fname))
print(character_word_count(fname))
print(starts_with_vow(fname))
print("==================================================")

fname = 'Book2.txt'
print(unique_words(fname))
print(count_the_article(fname))
print(sorted_words(fname))
print(character_word_count(fname))
print(starts_with_vow(fname))
print("==================================================")


fname = 'Book3.txt'
print(unique_words(fname))
print(count_the_article(fname))
print(sorted_words(fname))
print(character_word_count(fname))
print(starts_with_vow(fname))
