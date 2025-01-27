import re

tokenized = []
readfile = open("cleaned_text.txt","r",encoding="utf8")
text = readfile.readlines()

for line in text:
    de_line = re.sub(r'[.!?] ','<sep>',line)
    newlines = de_line.split('<sep>')
    print(len(newlines))
    for newline in newlines:
        tokenized.append(newline)
    print(len(tokenized))
    
file = open("tokenized.txt","w")
file.write(str(tokenized))