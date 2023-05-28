import re

from Lab2.Task1.constants import EXCLUSIONS, TWO_WORDS_EXCLUSIONS, NON_DECLARATIVE_PATTERN, POINT_PATTERN,\
    WORD_AND_NUMBER_PATTERN, NUMBER_PATTERN


def amount_of_non_declarative_sentences(text):
    end_non_dec_match = re.findall(NON_DECLARATIVE_PATTERN, text)
    sentences_with_non_dec = len(end_non_dec_match)
    return sentences_with_non_dec


def amount_of_sentences(text):
    end_point_match = re.findall(POINT_PATTERN, text)
    sentences_with_poits = len(end_point_match)

    for i in EXCLUSIONS:
        sentences_with_poits -= text.count(i)

    for i in TWO_WORDS_EXCLUSIONS:
        sentences_with_poits -= text.count(i) * 2

    sentences_with_non_dec = amount_of_non_declarative_sentences(text)

    sentences_in_the_text = sentences_with_poits + sentences_with_non_dec

    return sentences_in_the_text


def only_words(text):
    words_and_numbers = re.findall(WORD_AND_NUMBER_PATTERN, text)
    numbers = re.findall(NUMBER_PATTERN, text)
    words = []

    for element in words_and_numbers:
        if element not in numbers:
            words.append(element)
    return words


def average_length_of_the_sentence(text):
    words = only_words(text)
    length_in_characters = 0

    for word in words:
        length_in_characters += len(word)

    sentences_in_the_text = amount_of_sentences(text)

    if sentences_in_the_text != 0:
        average_sentence_length = length_in_characters / sentences_in_the_text
        return average_sentence_length
    else:
        return 0


def average_length_of_the_word(text):
    words = only_words(text)
    length_in_characters = 0

    for word in words:
        length_in_characters += len(word)

    amount_of_words = len(words)

    if amount_of_words != 0:
        average_word_length = length_in_characters / amount_of_words
        return average_word_length
    else:
        return 0


def max_value(x):
    return x[1]


def top_k_repeated_n_grams_in_the_text(text, n, k):

    dictionary = {}
    text = text.lower()
    words = only_words(text)

    for i in range(len(words) - n + 1):
        n_grams = ' '.join([str(j) for j in words[i:i + n]])
        if n_grams not in dictionary:
            dictionary[n_grams] = 1
        else:
            dictionary[n_grams] += 1

    return sorted(dictionary.items(), key=max_value, reverse=True)[:k]
