import re
from constants import (EXCLUSIONS, TWO_WORDS_EXCLUSIONS, NON_DECLARATIVE_PATTERN, POINT_PATTERN,
                       WORD_AND_NUMBER_PATTERN, NUMBER_PATTERN)
def amount_of_non_declarative_sentences(text):
    end_non_dec_match = re.findall(NON_DECLARATIVE_PATTERN, text)
    sentences_with_non_dec = len(end_non_dec_match)
    return sentences_with_non_dec

def amount_of_sentences(text, sentences_with_non_dec):
    end_point_match = re.findall(POINT_PATTERN, text)
    sentences_with_poits = len(end_point_match)

    for i in EXCLUSIONS:
        sentences_with_poits -= text.count(i)

    for i in TWO_WORDS_EXCLUSIONS:
        sentences_with_poits -= text.count(i)*2

    sentences_in_the_text = sentences_with_poits + sentences_with_non_dec

    return sentences_in_the_text

def average_length_of_the_sentence(text):
    words_and_numbers = re.findall(WORD_AND_NUMBER_PATTERN, text)
    numbers = re.findall(NUMBER_PATTERN, text)
    words=[]

    for element in words_and_numbers:
        if element not in numbers:
            words.append(element)

    length_in_characters = 0

    for word in words:
        length_in_characters += len(word)

    sentences_with_non_dec = amount_of_non_declarative_sentences(text)
    sentences_in_the_text = amount_of_sentences(text, sentences_with_non_dec)

    if sentences_in_the_text != 0:
        average_sentence_length = length_in_characters / sentences_in_the_text
        return average_sentence_length
    else:
        return 0


def average_length_of_the_word(text):
    words_and_numbers = re.findall(WORD_AND_NUMBER_PATTERN, text)
    numbers = re.findall(NUMBER_PATTERN, text)
    words = []

    for element in words_and_numbers:
        if element not in numbers:
            words.append(element)

    length_in_characters = 0

    for word in words:
        length_in_characters += len(word)

    amount_of_words = len(words)

    if amount_of_words != 0:
        average_word_length = length_in_characters / amount_of_words
        return average_word_length
    else:
        return 0


