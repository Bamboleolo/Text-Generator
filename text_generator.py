# Write your code here
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter, defaultdict
from random import choice
punctuation_marks = ['!', '.', '?']
fname = input()

with open(fname, 'r', encoding='utf-8') as f:
    corpus = f.read()

tokens = WhitespaceTokenizer().tokenize(corpus)

bigrams = [[tokens[i], tokens[i + 1]] for i in range(len(tokens) - 1)]
trigrams =[[tokens[i], tokens[i + 1], tokens[i + 2]] for i in range(len(tokens) - 2)]

#print(trigrams)

mark_chain = defaultdict(list)
for head, mid, tail in trigrams:
    mark_chain[head + ' ' + mid].append(tail)

for head in mark_chain:
    mark_chain[head] = (Counter(mark_chain[head])).most_common()

#print(mark_chain)


for _ in range(10):
    while True:
        head = choice(list(mark_chain.keys()))
        if head[0].isupper() and head.split()[0][-1] not in punctuation_marks \
                and head.split()[1][-1] not in punctuation_marks:
            break
    print(head, end=" ")
    i = 2
    while True:
        prev_word = head.split()[-1]
        tail = mark_chain[head][0][0]
        head = prev_word + " " + mark_chain[head][0][0]
        print(tail, end=" ")
        i += 1
        if i >= 5 and head[-1] in punctuation_marks:
            break

        if i > 30:
            break
    print()
