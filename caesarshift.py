import string
# Caesar's cypher
source = raw_input('Source Filename: ')
dest = raw_input('Enc Filename: ')
key = raw_input('Insert shift: ')

mapping = dict()

lowers = string.lowercase
uppers = string.uppercase

for i, ch in enumerate(lowers):
    if i + 4 < len(lowers):
        mapping[ch] = lowers[i+4]
    else:
        mapping[ch] = lowers[i+4 - len(lowers)]

for i, ch in enumerate(uppers):
    if i + 4 < len(uppers):
        mapping[ch] = uppers[i+4]
    else:
        mapping[ch] = uppers[i+4 - len(uppers)]

print mapping

file = open(source)
out = open(dest,'w')
txt = file.read()
for ch  in txt:
    try:
        out.write(mapping[ch])
    except:
        out.write(ch)
