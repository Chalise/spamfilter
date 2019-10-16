

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import random

def dictionary(words):
    spamdict = dict([(word, True) for word in words])
    return spamdict

def get_classifier():

    training_data1 = "nonspam-train"

    nonspam_list = []
    combined_list = []

#def dictionary():
    #with open('dictionary.txt') as f:
       #my_dictionary = dict(x.rstrip().split(None, 1) for x in f)
    #return my_dictionary

    

    for directories, subdirs, files in os.walk(training_data1):
    for filename in files:
        with open(os.path.join(directories,filename), encoding = "latin-1") as f:
            data = f.read()
            words = word_tokenize(data)
            nonspam_list.extend((dictionary(words), 'nonspam'))
            #nonspam_list.extend("nonspam": words)
    print(directories,subdirs, lens(files))

    training_data2 = "spam-train"
    spam_list = []

    for directories, subdirs, files in os.walk(training_data2):
        for filename in files:
            with open(os.path.join(directories,filename), encoding = "latin-1") as f:
                data = f.read()
                words = word_tokenize(data)
                nonspam_list.extend((dictionary(words), 'spam'))
            #spam_list.extend("spam":words)
        print(directories,subdirs, lens(files))    

    print(nonspam_list[0])
    print(spam_list[0])

#combined_list = nonspam_list + spam_list
    combine_list = {[nonspam_list]+[spam_list]}
    print(len(combined_list))
    random.shuffle(combined_list)
    test_set = 'testing_set'

    classifier = NaiveBayesClassifier.train(combined_list)

    Accuracy = nltk.classify.util.accuracy(classifier, test_set)
    print("Accuracy is: ", Accuracy * 100)

    return classifier

def realtimeclassification():
    classifier = NaiveBayesClassifier.

    Accuracy = nltk.classify.util.accuracy(classifier, test_)
    print("Accuracy is: ", Accuracy * 100)



    feature = dictionary(words)
    return("Message is: " , classifier.classify(feature))



#testing code
msg1 = 'posting hi m work phonetics project modern irish m hard source anyone recommend book article english specifically interest palatal slender consonant work helpful too thank laurel sutton sutton garnet berkeley edu '
msg2 = 'great parttime summer job display box credit application need place small owneroperate store area here introduce yourself store owner manager our effective script tell little display box save customer hundred dollar draw card business every app send spot counter place box nothing need need name address company send commission check compensaation every box place become representative earn commission each application store course much profitable plan pay month small effort call code hours receive detail removed our mailing list type b hotmail com area remove subject area e mail send '
msg3 = 'guess oqth http www lovemenow com material server adult orient sexually explicit relate material adult nature site provide access image nude adult possibly engage sexual act access available those accept term follow agreement accept agreement certify follow image nude adult adult engage sexual act sexual material offensive objectionable least age legal right possess adult material community understand standard law community site computer transport material solely responsible action nor ever employ law enforcement agency attempt bypass security access feature site service violation above agreement understand violation local federal law solely responsible action log release discharge provider owner creator site liability arise bookmark page server site whereby warn page bypass shall constitute implicit acceptance forego term herein set forth http www lovemenow com http www lovemenow com cgibin index pl free day trial membership '

words = word_tokenize(msg1)
feature = dictionary(words)
print("Message 1 is: " , classifier.classify(feature))

words = word_tokenize(msg2)
feature = dictionary(words)
print("Message 2 is: " , classifier.classify(feature))

words = word_tokenize(msg3)
feature = dictionary(words)
print("Message 3 is: " , classifier.classify(feature))