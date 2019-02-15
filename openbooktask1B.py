from string import punctuation
N = 20
words = {}
words_gen = (word.strip(punctuation).lower()
for line in open("Book1.txt") 
  for word in line.split())
   for word in words_gen:
    words[word] = words.get(word, 0) + 1
    top_words = sorted(words.iteritems(), 
    cmp=lambda x, y: cmp(x[1], y[1]) or cmp(y[0], x[0]), 
    reverse=True)[:N]
for word, frequency in top_words:
  print "%s: %d" % (word, frequency)
