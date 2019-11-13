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
    """
    All HTML tags are removed from the emails.
    Many emails often come with HTML formatting; we remove all the
    HTML tags, so that only the content remains.
    :param text:
    :return: string without html tags
    """

    clean = re.compile(r'<.*?>')
    return re.sub(clean, '', text)



def stemming_words(stemtext):
    """
    Words are reduced to their stemmed form. For example,
        “discount”, “discounts”, “discounted” and “discounting” are all
        replaced with “discount”.
    :param stemtext:
    :return:  Stemmed words with NLTK
    """
    ps = PorterStemmer()
    return ps.stem(stemtext)



def tokenize_space(tokentext):
    """

    :param tokentext:
    :return: tokenized text
    """
    # Create a reference variable for Class SpaceTokenizer
    tk = SpaceTokenizer()
    # Create a string input
    # Use tokenize method
    return tk.tokenize(tokentext)


def findURL(urltext):
    """
    All URLs are replaced with the text “httpaddr”.
    :param urltext:
    :return: “httpaddr" if it is a URL
    """
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', urltext)
    if url:
        return 'httpaddr'
    else:
        return urltext


def findNumber(num):
    """
    All numbers are replaced with the text
    “number”.
    :param num:
    :return: “number" if it is a number
    """
    numb = re.findall("[^a-zA-Z:][-+]?\d+[\.]?\d*", num)

    if numb:
        return "number"
    else:
        return num


def findemail(urltext):
    """
    All numbers are replaced with the text
    “number”.
    :param urltext:
    :return: “emailaddr" if it is a email address
    """
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

