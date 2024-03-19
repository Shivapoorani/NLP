import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "this is a cat"

tokens = word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

print("Original Text:", text)
print("\nPart-of-speech Tags:", pos_tags)
