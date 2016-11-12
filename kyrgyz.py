import nltk

with open('kyrgyzdar_test_mini.txt', 'r') as f:
    sentence = f.read()

tokens = nltk.word_tokenize(sentence)
print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged[0:6])
