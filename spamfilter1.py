# import needed tools
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import random


#defines dictonary function
import prepare_data


def dictionary(words):
    # creates list for dictionary words
    spamdict = dict([(word, True) for word in words])
    # returns list of words
    return spamdict

# This function is going to teach naive bayes to differentiate spam and non-spma
def get_classifier():
    training_data1 = "spamdata/nonspam-train"
    nonspam_list = []
    combined_list = []

    # for loop that goes through training files for non-spam
    for directories, subdirs, files in os.walk(training_data1):
        for filename in files:
            with open(os.path.join(directories,filename), encoding = "latin-1") as f:
                #reads throuh the files and puts strings in data object
                data = f.read()
                # word_tokenize makes strings to separated words and puts list to object words
                words = word_tokenize(data)
                # words are added to nonspam list and dictionary
                nonspam_list.extend((dictionary(words), 'nonspam'))

    training_data2 = "spamdata/spam-train"
    spam_list = []
    # for loop that goes through training files for spam
    for directories, subdirs, files in os.walk(training_data2):
        for filename in files:
            with open(os.path.join(directories,filename), encoding = "latin-1") as f:
                #reads throuh the files and puts strings in data object
                data = f.read()
                # word_tokenize makes strings to separated words and puts list to object words
                words = word_tokenize(data)
                # words are added to spam list and dictionary
                nonspam_list.extend((dictionary(words), 'spam'))
    #print(nonspam_list[0])
    #print(spam_list[0])

    #compined spam and nonspam lists for training
    combine_list = {[nonspam_list]+[spam_list]}
    #suffle the list before training
    random.shuffle(combined_list)
    #gets testdata files
    test_set = 'spamdata/testing_set'

    #calls naive bayes classifier and trains it
    classifier = NaiveBayesClassifier.train(combined_list)

    #counts classifiers accurasy using testing set
    Accuracy = nltk.classify.util.accuracy(classifier, test_set)
    print("Accuracy is: ", Accuracy * 100)
    #returns 
    return classifier

# function for clients emails for real time checks
def realtimeclassification(classifier, email):
    test_set = "spamdata/Testing_set"
    words = prepare_data.prepare_data(email)
    feature = dictionary(words)
    Accuracy = nltk.classify.util.accuracy(classifier, test_set)
    print("Accuracy is: ", Accuracy * 100)
   # return ("Message is: ", classifier.classify(feature))
    return 'true'
# Train the classifier
# get the client email
# Run realtimeclassification.. return spam

classifierTest = get_classifier()
    

