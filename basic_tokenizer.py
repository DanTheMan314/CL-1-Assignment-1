import re

contracts = {
    'mr.':'<mistercon>',
    'mrs.':'<missuscon>',
    'dr.':'<doctorcon>',
}

expands = {
    '<mistercon>':'mr.',
    '<missuscon>':'mrs.',
    '<doctorcon>':'dr.'
}

readfile = open("cleaned_text.txt","r",encoding="utf8")
text = readfile.readlines()

tokenized = []
# sentence level tokenization
for line in text:
    de_line = re.sub(r'\n','<sep>',line)
    for key in contracts.keys(): # switching from contraction to placeholder
        if key in de_line:
            de_line = de_line.replace(key,contracts[key])
    de_line = re.sub(r'[.!?] ','<sep>',de_line) # to make sentence separaters more obvious
    newlines = de_line.split('<sep>')
    for newline in newlines:
        if newline != '':
            tokenized.append(newline)

tokenlist = []
# word level tokenization
for line in tokenized:
    tokens = line.split(" ")
    newtokens = []
    for token in tokens:
        newtoken = re.sub(r'[^a-z0-9.\-<>\':,]', '',token) # for all other special cha
        for key in expands.keys(): # switching from placeholder to contraction
            if key in newtoken:
                newtoken = newtoken.replace(key,expands[key])
        if newtoken!='':
            newtokens.append(newtoken)
    tokenlist.append(newtokens)
    
file = open("tokenized.txt","w")
file.write(str(tokenlist))