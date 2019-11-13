import os
import re

# import these modules
from itertools import count

import numpy as np
from nltk import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import SpaceTokenizer

from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def remove_html_tags(text):
    # Remove html tags from a string
    clean = re.compile(r'<.*?>')
    return re.sub(clean, '', text)


def stemming_words(stemtext):
    ps = PorterStemmer()
    return ps.stem(stemtext)
    # Stemming words with NLTK


def tokenize_space(tokentext):
    # Create a reference variable for Class SpaceTokenizer
    tk = SpaceTokenizer()
    # Create a string input
    # Use tokenize method
    return tk.tokenize(tokentext)


def findURL(urltext):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', urltext)
    if url:
        return 'httpaddr'
    else:
        return urltext


def findNumber(num):
    numb = re.findall("[^a-zA-Z:][-+]?\d+[\.]?\d*", num)

    if numb:
        return "number"
    else:
        return num


def findemail(urltext):
    email = re.findall('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', urltext)
    if email:
        return 'emailaddr'
    else:
        return urltext


# Load and concatenate all the emails in one string
def prepare_data(emailtext):
    content = []
    i = 0
    for line in emailtext.splitlines():
        line = strip_tags(line)  # Stripping HTML
        for word in line.split():
            # Lower-casing
            word = word.lower()
            # Word Stemming
            word = stemming_words(word)
            # Normalizing URL
            word = findURL(word)
            # Normalizing Email Addresses
            word = findemail(word)
            word = findNumber(word)
            # Removal of non-words
            word = re.compile('\w+').findall(word)
            
            for i in word:
                content.append(i)

    return content

