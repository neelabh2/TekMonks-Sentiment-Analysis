from textblob import TextBlob
#see if you can import a dictionary instead of manually making adj
#adj = {'love': 1, 'dislike': -1, 'good': 1, 'bad': -1}

#this may need a path to the files
#BIG: NEED TO ADD WORDS TO DICTIONARY (missing "bad", for example)
with open('C:/Users/neel2/Desktop/negative-words.txt') as negWords:
    negLines = negWords.read().splitlines()
with open('C:/Users/neel2/Desktop/positive-words.txt') as posWords:
    posLines = posWords.read().splitlines()

text = TextBlob("I love python, but sometimes I dislike it, especially when it gives me bad errors.")
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