

import random

import nltk

nltk.download('punkt')

phrase_table = {}



def code_switch_sequence( X, Y, phrase_table,language, max_phrase_len=5, max_substitution_ratio=0.3, num_samples=1,probability=0.4):
    """
    Generates code switch sequences for a parallel sentence pair (X, Y) using a bilingual phrase table.

    Args:
        X (str): Source sentence in the major source language.
        Y (str): Target sentence in the major target language.
        phrase_table (dict): Bilingual phrase table with source phrases as keys and target phrases as values.
        max_phrase_len (int, optional): Maximum length of phrases to be substituted. Defaults to 5.
        max_substitution_ratio (float, optional): Maximum ratio of words to be substituted in a sentence. Defaults to 0.3. ###??
        num_samples (int, optional): Number of code switch sequences to generate. Defaults to 1.

    Returns:
        list: List of generated code switch sequences.
    """

    
    code_switch_sequences = []
    source_language = language.split('-')[0]
    target_language = language.split('-')[1]

    for _ in range(num_samples):
        X_tokens = nltk.word_tokenize(X) ## should be replaced by tokenization
        Y_tokens = nltk.word_tokenize(Y) ## should be replaced by tokenization


        max_substitution_words = int(max_substitution_ratio * len(X_tokens))  # Calculate the maximum number of words to be substituted
        num_substitution_words = 0  # Initialize the counter for substituted words

        # Substitute phrases in source sentence with target phrases
        for i in range(len(X_tokens)):
            if X_tokens[i] in phrase_table.keys() and len(phrase_table[X_tokens[i]].split()) <= max_phrase_len:
                if random.random() < probability and num_substitution_words < max_substitution_words:
                    X_tokens[i] = phrase_table[X_tokens[i]].split()[0]
                    num_substitution_words += 1

        max_substitution_words = int(max_substitution_ratio * len(X_tokens))  # Calculate the maximum number of words to be substituted
        num_substitution_words = 0  # Initialize the counter for substituted words

        # Substitute phrases in target sentence with source phrases
        for i in range(len(Y_tokens)):
            if Y_tokens[i] in phrase_table.values() and len(Y_tokens[i].split()) <= max_phrase_len:
                if random.random() < probability and num_substitution_words < max_substitution_words:
                    target_phrase = Y_tokens[i]
                    source_phrase = [k for k, v in phrase_table.items() if v == target_phrase][0]
                    Y_tokens[i] = source_phrase.split()[0]
                    num_substitution_words += 1
        if source_language == 'chinese':
            code_switch_sequence = [''.join(X_tokens), ' '.join(Y_tokens)]
        elif target_language == 'chinese': 
        	code_switch_sequence = [' '.join(X_tokens), ''.join(Y_tokens)]
        else:
        	code_switch_sequence = [' '.join(X_tokens), ' '.join(Y_tokens)]

        code_switch_sequences.append(code_switch_sequence)

    return code_switch_sequences

# Example usage
X = "I like to eat apples"
Y = "Je préfère manger des pommes"
phrase_table = {"like": "préfère", "eat": "manger", "apples": "pommes"}
max_phrase_len = 5
max_substitution_ratio = 0.3
num_samples = 3
probability=0.4
language = 'english-french'

code_switch_sequences = code_switch_sequence(X, Y, phrase_table,language, max_phrase_len, max_substitution_ratio, num_samples,probability)
print("Generated code switch sequences:")
for i, sequence in enumerate(code_switch_sequences):
    print(f"Sequence {i + 1}: {sequence}")


