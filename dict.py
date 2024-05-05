import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import enchant

import re

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_word(word, pos):
    if pos is None:
        return word
    else:
        lemma = nltk.WordNetLemmatizer().lemmatize(word, pos=pos)
        return lemma


def extract_unique_words(text):
    tokens = word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    unique_words = set()

    for word, tag in tagged_words:
        pos = get_wordnet_pos(tag)
        lemma = lemmatize_word(word.lower(), pos)
        unique_words.add(lemma)

    return unique_words


def filter_english_words(words):
    d = enchant.Dict("en_US")
    english_words = set()
    for word in words:
        # Проверяем, является ли слово английским и находится ли оно в словаре
        if re.match(r'^[a-zA-Z\-]+$', word) and d.check(word):
            english_words.add(word)
    return english_words


if __name__ == "__main__":
    with open('articles.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    unique_words = extract_unique_words(text)
    filtered_wors =  filter_english_words(unique_words)

    with open('words.txt', 'w') as file:
        for word in filtered_wors:
            file.write(word + '\n')

    print("Уникальные слова:")
    print(len(filtered_wors))
    print(filtered_wors)
