from textblob import TextBlob

#this may need a path to the files
#BIG: NEED TO ADD WORDS TO DICTIONARY (missing "bad", for example)
with open('C:/Users/neel2/Desktop/Tekmonks Sentiment Analysis/negative-words.txt') as negWords:
    negLines = negWords.read().splitlines()
with open('C:/Users/neel2/Desktop/Tekmonks Sentiment Analysis/positive-words.txt') as posWords:
    posLines = posWords.read().splitlines()

text = TextBlob("I love python, but sometimes I dislike it, especially when it gives me bad errors.")
#make an overarching loop running through sentences from around here
#then make the percentage based on # of sentences that are pos or neg
wordList = text.words
positive = 0
negative = 0

for i in wordList:
    if i in negLines:
        negative += 1
    elif i in posLines:
        positive += 1

if negative == 0:
    percentage = 1
else:
    percentage = positive / negative

print(percentage)

if percentage >= 0.5:
    print('positive')
else:
    print('negative')