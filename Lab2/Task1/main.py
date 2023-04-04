import re

def amount_of_non_declarative_sentences(text):
    non_declarative_pattern = r'([0-9]+[a-zA-Z]+\?)|([a-zA-Z]+\?)|([a-zA-Z]+[0-9]+\?)|([0-9]+\?)|([0-9]+[a-zA-Z]+\!)|([a-zA-Z]+\!)|([a-zA-Z]+[0-9]+\!)|([0-9]+\!)'
    end_non_dec_match = re.findall(non_declarative_pattern, text)
    sentences_with_non_dec = len(end_non_dec_match)
    return sentences_with_non_dec

def amount_of_sentences(text, sentences_with_non_dec):
    point_pattern = r'([0-9]+[a-zA-Z]+\.)|([a-zA-Z]+\.)|([a-zA-Z]+[0-9]+\.)|([0-9]+\.)'
    end_point_match = re.findall(point_pattern, text)
    sentences_with_poits = len(end_point_match)
    sentences_in_the_text = sentences_with_poits + sentences_with_non_dec
    return sentences_in_the_text


if __name__=='__main__':

    text = input("Write your text:")

    sentences_with_non_dec = amount_of_non_declarative_sentences(text)
    sentences_in_the_text = amount_of_sentences(text, sentences_with_non_dec)

    print("Amount of non-declarative sentences in the text:")
    print(sentences_with_non_dec)
    print("Amount of sentences in the text:")
    print(sentences_in_the_text)


