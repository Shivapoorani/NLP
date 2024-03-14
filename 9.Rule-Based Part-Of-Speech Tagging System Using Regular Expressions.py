import re
def rule_based_pos_tagging(sentence):
    tagged_sentence = []
    for word in sentence:
        patterns = [
            (r'\b[Aa]n?\b', 'DT'),                     
            (r'\b(?:[A-Z].*?){2,}\b', 'NNP'),          
            (r'\b(?:[a-z].*?){2,}\b', 'NN'),           
            (r'\b(?:[Vv]erb.*?){2,}\b', 'VB'),         
            (r'\b(?:[Aa]djective.*?){2,}\b', 'JJ'),   
            (r'\b(?:[Aa]dverb.*?){2,}\b', 'RB'),      
            (r'\b(?:[Cc]onjunction.*?){2,}\b', 'CC'), 
            (r'\b(?:[Pp]ronoun.*?){2,}\b', 'PRP'),    
            (r'\b(?:[Pp]reposition.*?){2,}\b', 'IN'), 
            (r'\b(?:[Ii]nterjection.*?){2,}\b', 'UH') 
        ]
        tagged = False
        for pattern, tag in patterns:
            if re.match(pattern, word):
                tagged_sentence.append((word, tag))
                tagged = True
                break
        if not tagged:
            tagged_sentence.append((word, 'NN'))
    return tagged_sentence
sentence_input = input("Enter a sentence: ")
tokenized_sentence = sentence_input.split()
tagged_sentence = rule_based_pos_tagging(tokenized_sentence)
print("Tagged sentence:")
print(tagged_sentence)
