import pandas as pd
import re
from collections import Counter

def find_and_replace(filename):
    with open(filename,'r') as file:
        content=file.read()

    words=re.split(r'[ ,.\n]+',content)

    df=pd.DataFrame(words,columns=['Word'])
    word_count=df['Word'].value_counts()

    max_count=word_count.max()
    max_words=word_count[word_count==max_count].index.tolist()

    print(f"The following word(s) have the maximum occurrence ({max_count} times) : {', '.join(max_words)} ")

    for word in max_words:
        content=re.sub(r'\b' + re.escape(word) + r'\b', "Aligarh",content)

    with open(filename,'w') as file:
        file.write(content)

    print(f"All occurrences of {', '.join(max_words)} have been replaced with 'Aligarh'")

filename='WEEK10/week10_prob5.txt'
find_and_replace(filename)