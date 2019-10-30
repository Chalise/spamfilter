# import needed tools
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import random
import prepare_data

def dictionary(words):
    # creates list for dictionary words
    spamdict = dict([(word, True) for word in words])
    # returns list of words
    return spamdict


# This function is going to teach naive bayes to differentiate spam and non-spma
def get_classifier():
    training_data1 = "spamdata/training_set/nonspam-train"
    nonspam_list = []
    combined_list = []

    # for loop that goes through training files for non-spam
    for directories, subdirs, files in os.walk(training_data1):
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                # reads throuh the files and puts strings in data object
                data = f.read()
                # word_tokenize makes strings to separated words and puts list to object words
                words = word_tokenize(data)
                # words are added to nonspam list and dictionary
                nonspam_list.append((dictionary(words), 'nonspam'))

    training_data2 = "spamdata/training_set/spam-train"
    spam_list = []
    # for loop that goes through training files for spam
    for directories, subdirs, files in os.walk(training_data2):
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                # reads throuh the files and puts strings in data object
                data = f.read()
                # word_tokenize makes strings to separated words and puts list to object words
                words = word_tokenize(data)
                # words are added to spam list and dictionary
                spam_list.append((dictionary(words), 'spam'))


    print("Non spam list before extention",len(nonspam_list))
    print(" spam list ", len(nonspam_list))
    # compined spam and nonspam lists for training
    combine_list = nonspam_list.extend(spam_list)

    print("Non spam list after extention", len(nonspam_list))
    # suffle the list before training
    random.shuffle(nonspam_list)

    # calls naive bayes classifier and trains it
    classifier = NaiveBayesClassifier.train(nonspam_list)

    #gets testdata function
    test = testdata()


    # returns
    return classifier



# function that makes testset ready for use
def testdata():
    test_set = 'spamdata/testing_set'
    testlist=[]
    for directories, subdirs, files in os.walk(test_set):
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                # reads throuh the files and puts strings in data object
                t = f.read()
                # word_tokenize makes strings to separated words and puts list to object words
                tst = word_tokenize(t)
                # words are added to test list
                testlist.append(tst)
    return testlist

# function for clients emails for real time checks
def realtimeclassification(classifier, email):
    words = prepare_data.prepare_data(email)
    feature = dictionary(words)
    print("Message is: ", classifier.classify(feature))



trained_classifier= get_classifier()
realtimeclassification(trained_classifier,"Hi i am testing email, am i email ?")