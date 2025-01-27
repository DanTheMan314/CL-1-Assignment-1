import re

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

cleaningchars = ["‘","’",":","—","-","\"","'",";","*","*","","(",")","…","/","–","•","@","=","|","“","\u200d","+","\u200c"]
cleaned_text = []
readfile = open("18_text.txt","r",encoding="utf8")
text = readfile.readlines()

for line in text:
    # leading, trailing and in between whitespace
    cleaned_line = re.sub(r'  +', ' ', line)
    cleaned_line = re.sub(r'^ *', '', cleaned_line)
    cleaned_line = re.sub(r' *$', '', cleaned_line)
    # converting uppercase characters to lowercase
    for l in re.findall(r'[A-Z]', cleaned_line):
        cleaned_line = cleaned_line.replace(l,l.lower())
    # replacing basic contractions
    for key in abbrevs.keys():
        if key in cleaned_line:
            cleaned_line = cleaned_line.replace(key,abbrevs[key])

    # HTML Tags
    cleaned_line = re.sub(r'<.*?>', '', cleaned_line)
    # URLs
    cleaned_line = re.sub(r'[a-z]+(\.[a-z]+)+','<URL>',cleaned_line)
    # emails
    cleaned_line = re.sub(r'[a-z]+(\.[a-z]+)*@[a-z]+(\.[a-z]+)+', '<MAIL>', cleaned_line)
    # hashtags
    cleaned_line = re.sub(r'#[a-z]+','<HASHTAG>',cleaned_line)
    # mentions
    cleaned_line = re.sub(r'@[a-z]+', '<MENTION>', cleaned_line)

    # quotation marks
    cleaned_line = re.sub(r"\'\'",'"',cleaned_line)
    """ for l in re.findall(r'\'.*\'', cleaned_line):
        set = cleaned_line.split(l,1)
        cleaned_line = set[0]+'\"'+set[1] """
    # ellipsis
    cleaned_line = re.sub(r'\. +\. +\. +\.?', '...', cleaned_line)

    # removing unnecessary special characters
    cleaned_line = re.sub(r'[^a-z0-9 @$,.!?:;\'\"\-]', '',cleaned_line)

    cleaned_text.append(cleaned_line)



#""
writefile = open("cleaned_text.txt","w")
for line in cleaned_text:
    writefile.write(line)