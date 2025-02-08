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

def clean(line):
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
    cleaned_line = re.sub(r'--', '...', cleaned_line)

    # removing colon from everywhere except references/timestamps
    cleaned_line = re.sub(r':[ \n]', ' ', cleaned_line) # for non numbers/timestamps

    # removing comma from everywhere except numbers
    cleaned_line = re.sub(r',[ \n]', ' ', cleaned_line)

    # removing unnecessary special characters
    cleaned_line = re.sub(r'[^a-z0-9 .,?!]', '',cleaned_line)
    
    return cleaned_line


file = open("brown_corpus.txt","r",encoding = "utf8")
text = file.readlines()

vocabulary = []
worddict = {}

for line in text:
    cleaned_text = clean(line)
    words = cleaned_text.split(" ")
    # Creating initial character list to get vocabulary
    for word in words:
        if word not in worddict:
            worddict[word] = 1
        else:
            worddict[word] += 1
        for i in range(len(word)):
            if word[i] not in vocabulary:
                vocabulary.append(word[i])


# creating a representation for each word and how it's split up
wordstates = {}
for word in worddict.keys():
    wordstates[word] = [char for char in word]

# Setting the required vocabulary length after merging
vocablen = 300


while len(vocabulary) < vocablen:


    # finding the frequency of each pair
    pairdict = {}
    for word in worddict.keys():
        elements = wordstates[word]
        for i in range(len(elements)-1):
            if (elements[i],elements[i+1]) in pairdict:
                pairdict[(elements[i],elements[i+1])] += worddict[word]
            else:
                pairdict[(elements[i],elements[i+1])] = worddict[word]

    pairlist = list(pairdict.items())
    # Sorting the pairs by frequency
    pairlist = sorted(pairlist,key = lambda x: x[1])

    # Picking the most frequent pair
    newpair = pairlist[-1][0]

    # Merging the pair in every word
    for word in wordstates.keys():
        elements = wordstates[word]
        for i in range(len(elements)-1):
            if(elements[i],elements[i+1]) == newpair:
                elements[i] = elements[i]+elements[i+1]
                for j in range(i+1,len(elements)-1):
                    elements[j] = elements[j+1]
                elements.pop()
                break

    vocabulary.append(newpair[0]+newpair[1])

print(vocabulary)
