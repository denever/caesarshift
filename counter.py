import operator

txtdec = open('testo.txt')
chs = dict()
data = txtdec.read()
for ch in data:
    try:
        chs[ch] += 1
    except:
        chs[ch] = 1

sorted_chars = sorted(chs.iteritems(), key=operator.itemgetter(1))
sorted_chars.reverse()
print sorted_chars

