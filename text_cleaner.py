import re
import json 

abbrevs = {
    "isn\'t":"is not",
    'ain\'t':'am not',
    'don\'t':'do not',
    'i\'m':"i am",
    'won\'t':'will not',
    'can\'t':'cannot',
    'i\'ll':"i will",
    'you\'ll':"you will",
    'he\'ll':"he will",
    'they\'ll':"they will",
    'didn\'t':'did not',
    'haven\'t':'have not',
    'wasn\'t':'was not',
    'it\'s':'it is',
    'you\'ve':'you have',
    'i\'ve':'i have',
    'i\'d':'i had',
    'where\'s':'where is',
    'who\'s':'who is',
    'what\'s':'what is',
    'ma\'am':'madam'
}
def lowercase(match):
    print(match)
    return match.group(3).lower()

cleaningchars = ["‘","’",":","—","-","\"","'",";","*","*","","(",")","…","/","–","•","@","=","|","“","\u200d","+","\u200c"]
cleaned_text = []
readfile = open("18_text.txt","r",encoding="utf8")
text = readfile.readlines()

for line in text:
    line1 = re.sub(r'  +', ' ', line)
    line2 = re.sub(r'^ *', '', line1)
    line3 = re.sub(r' *$', '', line2)
    for l in re.findall(r'[A-Z]', line3):
        line3 = line3.replace(l,l.lower())
    for key in abbrevs.keys():
        if key in line3:
            line3 = line3.replace(key,abbrevs[key])
    line4 = re.sub(r'[^a-z0-9 ,.;?:\'\-!\n]', '',line3)
    cleaned_text.append(line4)

#"<.*?>"
writefile = open("cleaned_text.txt","w")
for line in cleaned_text:
    writefile.write(line)