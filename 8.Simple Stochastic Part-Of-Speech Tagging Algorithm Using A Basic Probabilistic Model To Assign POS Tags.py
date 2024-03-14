import random
def train_pos_tagger(sentences):
    """
    Train a simple stochastic part-of-speech tagger based on a basic probabilistic model.
    Returns a dictionary where keys are words and values are dictionaries of POS tags with their probabilities.
    """
    word_tag_counts = {}
    for sentence in sentences:
        for word, tag in sentence:
            if word not in word_tag_counts:
                word_tag_counts[word] = {}
            if tag not in word_tag_counts[word]:
                word_tag_counts[word][tag] = 0
            word_tag_counts[word][tag] += 1
    
    word_tag_probabilities = {}
    for word, tag_counts in word_tag_counts.items():
        total_count = sum(tag_counts.values())
        probabilities = {tag: count/total_count for tag, count in tag_counts.items()}
        word_tag_probabilities[word] = probabilities
    
    return word_tag_probabilities
def stochastic_pos_tagging(sentence, word_tag_probabilities):
    """
    Assign POS tags to words in a sentence using a simple stochastic tagging algorithm.
    """
    tagged_sentence = []
    for word in sentence:
        if word in word_tag_probabilities:
            tag_probabilities = word_tag_probabilities[word]
            selected_tag = random.choices(list(tag_probabilities.keys()), list(tag_probabilities.values()))[0]
            tagged_sentence.append((word, selected_tag))
        else:
            tagged_sentence.append((word, 'NN'))     
    return tagged_sentence
num_sentences = int(input("Enter the number of sentences: "))
sentences = []
for i in range(num_sentences):
    sentence_str = input(f"Enter sentence {i+1} (word/tag pairs separated by slash or space): ")
    words_tags = [pair.split('/') if '/' in pair else pair.split() for pair in sentence_str.split()]
    sentences.append(words_tags)
word_tag_probabilities = train_pos_tagger(sentences)
sentence_input = input("Enter a sentence to tag: ")
sentence = sentence_input.split()
tagged_sentence = stochastic_pos_tagging(sentence, word_tag_probabilities)
print("Tagged sentence:")
print(tagged_sentence)
