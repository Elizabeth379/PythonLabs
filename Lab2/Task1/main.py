from functions import amount_of_non_declarative_sentences, amount_of_sentences


if __name__=='__main__':

    text = input("Write your text:")

    sentences_with_non_dec = amount_of_non_declarative_sentences(text)
    sentences_in_the_text = amount_of_sentences(text, sentences_with_non_dec)

    print("Amount of non-declarative sentences in the text:")
    print(sentences_with_non_dec)
    print("Amount of sentences in the text:")
    print(sentences_in_the_text)


