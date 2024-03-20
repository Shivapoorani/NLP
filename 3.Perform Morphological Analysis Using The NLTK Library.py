import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
text = input("Enter the Text: ")
tokens = word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

print("Original Text:", text)
print("\nPart-of-speech Tags:", pos_tags)
