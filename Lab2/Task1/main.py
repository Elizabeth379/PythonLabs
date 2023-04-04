import re

EXCLUSIONS = ["Dr", "Mr", "Mrs","Lt", "Rep", "etc"]


if __name__=='__main__':
    point_pattern = r'([0-9]+[a-zA-Z]+\.)|([a-zA-Z]+\.)|([a-zA-Z]+[0-9]+\.)|([0-9]+\.)'
    non_declarative_pattern = r'([0-9]+[a-zA-Z]+\?)|([a-zA-Z]+\?)|([a-zA-Z]+[0-9]+\?)|([0-9]+\?)|([0-9]+[a-zA-Z]+\!)|([a-zA-Z]+\!)|([a-zA-Z]+[0-9]+\!)|([0-9]+\!)'

    text = input("Write your text:")
    sentences_with_poits = 0

    for end_point_match in re.findall(point_pattern, text):
        sentences_with_poits = sentences_with_poits + 1
        #print(end_point_match)



    #print(re.findall(point_pattern, text))
    print(sentences_with_poits)


