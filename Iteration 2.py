from textblob import TextBlob

#time to add text scraping capabilities?

#this may need a path to the files

#BIG: NEED TO ADD WORDS TO DICTIONARY (missing "bad", for example), ADD NEGATIVE ADVERBS

with open('C:/Users/neel2/Desktop/Tekmonks Sentiment Analysis/negative-words.txt') as negWords:
    negLines = negWords.read().splitlines()
with open('C:/Users/neel2/Desktop/Tekmonks Sentiment Analysis/positive-words.txt') as posWords:
    posLines = posWords.read().splitlines()
with open('C:/Users/neel2/Desktop/Tekmonks Sentiment Analysis/adverbs.txt') as allAdverbs:
    adverbs = allAdverbs.read().splitlines()

sentencePercentage = 0
sentencePositive = 0
sentenceNegative = 0
text = TextBlob("This product is very intolerable and good. This product is bad.")
#make it all lowercase, so it can be compared to txt files
text = text.lower()

print(text)

sentences = text.sentences
for sentence in sentences:
    wordList = sentence.words
    positive = 0
    negative = 0
    percentage = 0
    modifier = 0

    for word in wordList:
        if word in adverbs:
            modifier += 1
        elif word in negLines:
            negative = negative + 1 + modifier
            modifier = 0
        elif word in posLines:
            positive = positive + 1 + modifier
            modifier = 0

    if negative == 0:
        percentage = 1
    else:
        percentage = positive / (positive + negative)
    
    print(percentage)

    if percentage >= 0.5:
        sentencePositive += 1
    else:
        sentenceNegative += 1
    
if sentenceNegative == 0:
    sentencePercentage = 1
else:
    sentencePercentage = sentencePositive / (sentencePositive + sentenceNegative)


print(sentencePercentage)

if sentencePercentage >= 0.5:
    print('positive')
else:
    print('negative')