import re
from constants import (EXCLUSIONS, TWO_WORDS_EXCLUSIONS)
def amount_of_non_declarative_sentences(text):
    non_declarative_pattern = r'([0-9]+[a-zA-Z]+\?)|([a-zA-Z]+\?)|([a-zA-Z]+[0-9]+\?)|([0-9]+\?)|([0-9]+[a-zA-Z]+\!)|([a-zA-Z]+\!)|([a-zA-Z]+[0-9]+\!)|([0-9]+\!)'
    end_non_dec_match = re.findall(non_declarative_pattern, text)
    sentences_with_non_dec = len(end_non_dec_match)
    return sentences_with_non_dec

def amount_of_sentences(text, sentences_with_non_dec):
    point_pattern = r'([0-9]+[a-zA-Z]+\.)|([a-zA-Z]+\.)|([a-zA-Z]+[0-9]+\.)|([0-9]+\.)'
    end_point_match = re.findall(point_pattern, text)
    sentences_with_poits = len(end_point_match)

    for i in EXCLUSIONS:
        sentences_with_poits -= text.count(i)

    for i in TWO_WORDS_EXCLUSIONS:
        sentences_with_poits -= text.count(i)*2

    sentences_in_the_text = sentences_with_poits + sentences_with_non_dec

    return sentences_in_the_text

def average_length_of_the_sentence(text):
    word_and_number_pattern = r'(\b[a-zA-Z\d]+\b)'
    number_pattern = r'(\b\d+\b)'

    words_and_numbers = re.findall(word_and_number_pattern, text)
    numbers = re.findall(number_pattern, text)
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
    word_and_number_pattern = r'(\b[a-zA-Z\d]+\b)'
    number_pattern = r'(\b\d+\b)'

    words_and_numbers = re.findall(word_and_number_pattern, text)
    numbers = re.findall(number_pattern, text)
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


