text="""
The quick brown fox jumps over the lazy dog.
A journey of a thousand miles begins with a single step.
To be or not to be, that is the question.
All that glitters is not gold.
A picture is worth a thousand words.
Where there is a will, there is a way.
Actions speak louder than words.
The early bird catches the worm.
Don't count your chickens before they hatch.
Every cloud has a silver lining.
"""

import re
from collections import Counter
import pprint

list_text=text.split()

count=Counter(list_text)
pprint.pprint(count) # it will consider dog and dog. differently use RE to avoid spe char.

reg_exp=re.findall('\w+',text) #it will return list
count_reg_exp=Counter(reg_exp)
pprint.pprint(count_reg_exp)

'''
\w+ effectively extracts words from the text while ignoring punctuation and other non-word characters.'''