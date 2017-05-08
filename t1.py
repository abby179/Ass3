from functools import reduce
import operator

# construct list of lists to store each sentence of the corpus
with open('corpus.en.txt', 'r') as fin:
    lst_en = []
    for line in fin:
        lst_en.append(line.split())
with open('corpus.sv.txt', 'r') as fin:
    lst_sv = []
    for line in fin:
        lst_sv.append(line.split())
# get unique words from the corpus
sv_word = list(set(reduce(operator.add, lst_sv)))
en_word = list(set(reduce(operator.add, lst_en)))

# create a dictionary with tuple (english word, swedish word) as the key and the uniform probability as the value
# initialize t(e|f)

d = {}
for ew in en_word:
    for sw in sv_word:
        d[(ew, sw)] = 1 / len(sv_word)

# start 5 iterations
for i in range(5):
    # construct a dictionary containing the swedish words as the key and total count as the value: total(f)
    t = {}
    for sw in sv_word:
        t[sw] = 0

    # create a dictionary with tuple (english word, swedish word) as the key and the count as the value: count(e|f)
    c = {}
    for ew in en_word:
        for sw in sv_word:
            c[(ew, sw)] = 0

    # loop through sentence pairs
    for en, sv in zip(lst_en, lst_sv):

        s_total = {}
        for e in en:
            s_total[e] = 0
            for s in sv:
                s_total[e] = s_total[e] + d[(e, s)]

        # collect counts
        for e in en:
            for s in sv:
                c[(e, s)] = c[(e, s)] + d[(e, s)] / s_total[e]
                t[s] = t[s] + d[(e, s)] / s_total[e]

    # update the t(e|f)
    for s in sv_word:
        for e in en_word:
            d[(e, s)] = c[(e, s)] / t[s]

    print("---iteration:%s---" % (i + 1))
    for key in d:
        print("%s|%s" % (key[0], key[1]), ":", d[key])
