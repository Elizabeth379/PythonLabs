import unittest

from Lab2.Task1 import functions


class AmountOfSentencesTest(unittest.TestCase):
    def test_default(self):
        text = 'Hello! Anybody here? Oh... I am seeing smth. strange; maybe an elephant.'
        expected = 4
        actual = functions.amount_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Default amount of sentences in the text test: amount of sentences not ' + str(expected))

    def test_empty(self):
        expected = 0
        actual = functions.amount_of_sentences('')
        self.assertEqual(actual, expected,
                         'Empty amount of sentences in the text test: amount of sentences not ' + str(expected))

    def test_exclusions(self):
        text = 'Hello, Mr. Smith.'
        expected = 1
        actual = functions.amount_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Exclusions amount of sentences in the text test: amount of sentences not ' + str(expected))


class AmountOfNonDeclarativeSentencesText(unittest.TestCase):
    def test_default(self):
        text = 'Hello! Anybody here? Oh... I am seeing smth. strange; maybe an elephant.'
        expected = 2
        actual = functions.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected, 'Default amount of non declarative sentences in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_empty(self):
        expected = 0
        actual = functions.amount_of_non_declarative_sentences('')
        self.assertEqual(actual, expected, 'Empty amount of non declarative sentences in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_exclusions(self):
        text = 'Hello, Mr. Smith?'
        expected = 1
        actual = functions.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected,
                         'Exclusions amount of sentences in the text test: amount of sentences not ' + str(expected))


class AverageSentencesLength(unittest.TestCase):
    def test_default(self):
        text = 'Hello! Anybody here? Oh... I am seeing smth. strange; maybe an elephant.'
        expected = 53/4
        actual = functions.average_length_of_the_sentence(text)
        self.assertEqual(actual, expected, 'Default length of sentences in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_empty(self):
        expected = 0
        actual = functions.average_length_of_the_sentence('')
        self.assertEqual(actual, expected, 'Empty length of  sentences in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_exclusions(self):
        text = 'Hello, Mr. Smith?'
        expected = 12
        actual = functions.average_length_of_the_sentence(text)
        self.assertEqual(actual, expected,
                         'Exclusions length of sentences in the text test: amount of sentences not ' + str(expected))


class AverageWordsLength(unittest.TestCase):
    def test_default(self):
        text = 'Hello! Anybody here? Oh... I am seeing smth. strange; maybe an elephant.'
        expected = 53/12
        actual = functions.average_length_of_the_word(text)
        self.assertEqual(actual, expected, 'Default length of sentences in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_empty(self):
        expected = 0
        actual = functions.average_length_of_the_word('')
        self.assertEqual(actual, expected, 'Empty length of  sentences in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_exclusions(self):
        text = 'Hello, Mr. Smith?'
        expected = 12/3
        actual = functions.average_length_of_the_word(text)
        self.assertEqual(actual, expected,
                         'Exclusions length of sentences in the text test: amount of sentences not ' + str(expected))


class NGramsOfTheText(unittest.TestCase):
    def test_default(self):
        text = 'Hello, I am a cat. Hello, I am a dog.'
        expected = [('hello i am a', 2), ('i am a cat', 1), ('am a cat hello', 1), ('a cat hello i', 1), ('cat hello '
                                                                                                          'i am', 1),
                    ('i am a dog', 1)]
        actual = functions.top_k_repeated_n_grams_in_the_text(text)
        self.assertEqual(actual, expected, 'Default n-grams in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_empty(self):
        expected = []
        actual = functions.top_k_repeated_n_grams_in_the_text('')
        self.assertEqual(actual, expected, 'Empty n-grams in the text test: amount of '
                                           'sentences not ' + str(expected))

    def test_exclusions(self):
        text = 'Hello, I think it is good.?'
        expected = [('hello i think it', 1), ('i think it is', 1), ('think it is good', 1)]
        actual = functions.top_k_repeated_n_grams_in_the_text(text)
        self.assertEqual(actual, expected,
                         'Exclusions n-grams in the text test: amount of sentences not ' + str(expected))


if __name__ == '__main__':
    unittest.main()
