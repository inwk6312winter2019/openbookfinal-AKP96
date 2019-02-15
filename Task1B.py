
import string


def histogram(filename):

    hist = dict()
    file = open(filename)
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = hist.get(word, 0) + 1

    return hist


def common(file1,file2,file3):

    hist1 = histogram(file1)
    hist2 = histogram(file2)
    hist3 = histogram(file3)
    hist_common = dict()

    for word in hist1:
        if word in hist2 and word in hist3:
            hist_common[word] =  hist_common.get(word, 0) + 1

    lst = [(value,key)for key,value in hist_common.items()]
    lst.sort(reverse=True)
    only_20 = lst[:20]
    common_20 = dict(only_20)

    return common_20


print(common("Book1.txt","Book2.txt","Book3.txt"))
