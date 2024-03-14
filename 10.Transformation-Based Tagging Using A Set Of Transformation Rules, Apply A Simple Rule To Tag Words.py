rules = [
    (lambda w, i, history: history[i-1][1] if i > 0 else 'DEFAULT', 'NN', 'NNS', lambda w: w.endswith('s')),
    (lambda w, i, history: history[i-1][1] if i > 0 else 'DEFAULT', 'NN', 'NNP', lambda w: w[0].isupper()),
    (lambda w, i, history: history[i-1][1] if i > 0 else 'DEFAULT', 'JJ', 'RB', lambda w: w.endswith('ly')),
]
def transform_based_tagging(words):
    tagged = []
    history = []

    for i, word in enumerate(words):
        tagged_word = None
        for rule in rules:
            prev_tag = rule[0](word, i, history)
            if rule[3](word):
                tagged_word = (word, rule[2])
                break
            elif prev_tag == rule[1]:
                tagged_word = (word, rule[2])
                break
        if tagged_word is None:
            tagged_word = (word, 'DEFAULT')
        tagged.append(tagged_word)
        history.append(tagged_word)
    return tagged
input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
tagged_words = transform_based_tagging(words)
print(tagged_words)
