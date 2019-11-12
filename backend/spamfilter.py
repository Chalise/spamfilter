import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import os
import random
import pickle

from backend import prepare_data


SPAM = "spamdata/training_set/spam-train"
"""Directory containing spam-training data"""

HAM = "spamdata/training_set/nonspam-train"
"""Directory containing ham-training data"""

SAVE_DATA = ".training_data"
"""Path to saved training data"""


class SpamFilter:
    def __init__(self):
        self.classifier = self.__get_classifier()

    def classify(self, classifier, message):
        """
        Classify the given message with the given classifier.
        
        :param classifier: A trained classifier.
        :param message: String message to classify.
        :returns: Classification from the classifier.
        """
        result self.classifier.classify(self.__dictionary(prepare_data.prepare_data(message)))

    def process_training_data(self):
        """
        Process training data into something understood by NaiveBayesClassifier.
        Save processed data to SAVE_DATA to save time on API startup.
        
        :returns: Training data usable for training classifiers.
        """
        print("Processing training data. This may take a while..")
        nonspam_list = __classify_dataset(HAM, 'nonspam')
        spam_list = __classify_dataset(SPAM, 'spam')
        
        print("Ham elements: ", len(nonspam_list))
        print("Spam elements: ", len(spam_list))
        
        combined_list = nonspam_list + spam_list
        print("Total elements: ", len(combined_list))
        __save_data(combined_list)
        
        return combined_list

    def __get_classifier(self):
        """
        Return a trained classifier
        """
        # Process training data only if we have no saves
        # This takes a long time so we want to prevent this usually
        if os.path.exists(SAVE_DATA):
            print(f"Loading processed training data from {SAVE_DATA}")
            training_data = self.__load_data()
        else:
            print("No saved data found. Creating from scratch..")
            training_data = process_training_data()

        # calls naive bayes classifier and trains it
        classifier = NaiveBayesClassifier.train(training_data)
            
        #gets testdata function
        #TODO: Actually do something with the test data
        #test = testdata()
        print("Classifier trained!")
        print("Most informative features: ")
        classifier.show_most_informative_features(40)

        # returns
        return classifier

    def __classify_dataset(data_dir, label):
        """
        Tokenize and classify training data in the specified directory.
        
        :param data_dir: Path to the directory containing the training data.
        :param label: String label for tokenized words (for example: 'spam' or 'nonspam').
        """
        results = []
        for directories, subdirs, files in os.walk(data_dir):
            for filename in files:
                with open(os.path.join(directories, filename), encoding="latin-1") as f:
                    data = f.read()
                    words = word_tokenize(data)
                    results.append((__dictionary(words), label))

        return results

    def __dictionary(self, words):
        # creates list for dictionary words
        results = dict([(word, True) for word in words])
        # returns list of words
        return results
    
    def __save_data(self, obj):
        with open(SAVE_DATA, 'wb') as f:
            pickle.dump(obj, f)

    def __load_data(self):
        with open(SAVE_DATA, 'rb') as f:
            return pickle.load(f)

        
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
    feature = __dictionary(words)
    classified_email=classifier.classify(feature)

    dist = classifier.prob_classify(feature)
    print(dist)
    print(list(dist.samples()))
    print("Non Spam Prob.",dist.prob("nonspam"))
    print(" Spam Prob.",dist.prob("spam"))

    print("Message is: ",classified_email)


if __name__ == '__main__':
    pass
