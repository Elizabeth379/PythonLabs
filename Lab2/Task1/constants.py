EXCLUSIONS = ["Dr.", "Mr.", "Mrs.","Lt.", "Rep.", "etc.", "smth.", "smb.", "Jan.", "Feb.", "Mar.", "Apr.", "Jun.",
              'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.', 'Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.',
              'vs.', 'sr.', 'jr.', 'n.', 'v.', 'adj.', 'adv.', 'prep.', 'appx.', 'ex.']

TWO_WORDS_EXCLUSIONS = ['e.g.', 'p.s.', 'i.e.']

NON_DECLARATIVE_PATTERN = r'([0-9]+[a-zA-Z]+\?)|([a-zA-Z]+\?)|([a-zA-Z]+[0-9]+\?)|([0-9]+\?)|([0-9]+[a-zA-Z]+\!)|([a-zA-Z]+\!)|([a-zA-Z]+[0-9]+\!)|([0-9]+\!)'
POINT_PATTERN = r'([0-9]+[a-zA-Z]+\.)|([a-zA-Z]+\.)|([a-zA-Z]+[0-9]+\.)|([0-9]+\.)'
WORD_AND_NUMBER_PATTERN = r'(\b[a-zA-Z\d]+\b)'
NUMBER_PATTERN = r'(\b\d+\b)'


