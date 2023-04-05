from functions import amount_of_non_declarative_sentences, amount_of_sentences, average_length_of_the_sentence, \
    average_length_of_the_word


if __name__=='__main__':

    text = input("Write your text:")

    sentences_with_non_dec = amount_of_non_declarative_sentences(text)
    sentences_in_the_text = amount_of_sentences(text, sentences_with_non_dec)
    average_sentence_length = average_length_of_the_sentence(text)
    average_word_length = average_length_of_the_word(text)

    print("Amount of non-declarative sentences in the text:")
    print(sentences_with_non_dec)
    print("Amount of sentences in the text:")
    print(sentences_in_the_text)
    print("Average length of the sentence in characters:")
    print(average_sentence_length)
    print("Average length of the word in the text in characters")
    print(average_word_length)


