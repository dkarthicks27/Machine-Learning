"""

    categorization or classification is done using two steps first the documents are indexed then they are classified
so indexing is very important, so here we can actually index the documents into a format which can be used to
perform mathematical operation on it.

    A vector representation would be the most ideal case over here. Next step followed by it is to build a
classification model like naive bayes or SVM.

"""

import re
import sys
import time
from datetime import datetime
from glob import glob

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


def preprocess(s):
    """
    :param s: string (document)
    :return k: string (processed text)
    """
    k = re.sub('[0-9]*', '', s.lower())
    return k


def tfidf(filePath, n_gram=(1, 3)):
    """
        INPUT PARAMETERS:
            filepath : (list) this is a list of filePaths, for eg: ['/Enron/121.txt','/Enron/134.txt', ... ]
            n_gram : (tuple) this is the ngram range, it must be a tuple input; default (1, 3)
            stop_words : (string) this is the language, default is 'english'
            decode_error: (string) default is 'ignore', options are 'strict'
            pickleloc: (string) where the pickle file needs to be saved for further use. (mandatory)

        OUTPUT:
            Pickle file: it will be saved to the location provided during input parameter
        """
    print("Tfidf Initiated: \n")
    start = time.time()
    print(datetime.now())
    Vectorizer = TfidfVectorizer(input='filename', use_idf=True,
                                 stop_words='english',
                                 decode_error='ignore', max_df=0.50, sublinear_tf=True, ngram_range=n_gram,
                                 preprocessor=preprocess)
    vectors = Vectorizer.fit_transform(filePath)

    end = time.time()
    print("\ntime take is {} s".format(end - start))
    return vectors


def classifier(vector, labelTraining):
    """
    :param vector: Tfidf vector of the documents
    :param labelTraining: Label for the training dataset
    :return: None
    """
    iteration = 1
    train, test = train_test_split(vector, train_size=0.05)
    while iteration == 1:
        algorithm = int(input("\n1 for NaiveBayes\n2 for SVM\n3 for Logistic regression: "))
        if algorithm == 1:
            clf = MultinomialNB()
            clf.fit(train, labelTraining)
            predicted = clf.predict(test)
            print("\nThe Output below shows the distribution of label probability corresponding to each documents")
            print("rows- document\ncolumns- label order")
            print(clf.predict_proba(train))
            print("\nThe accuracy of algorithm is :", end='')
            print(clf.score(train, labelTraining))
            print("Class of Each tested Dataset: \n")
            print(predicted)
        elif algorithm == 2:
            svm = SVC(probability=True)
            svm.fit(train, labelTraining)
            predicted = svm.predict(test)
            print("\nThe Output below shows the distribution of label probability corresponding to each documents")
            print("rows- document\ncolumns- label order")
            print(svm.predict_proba(train))
            print("\nThe accuracy of algorithm is :", end='')
            print(svm.score(train, labelTraining))
            print("Class of Each tested Dataset: \n")
            print(predicted)
        elif algorithm == 3:
            logistic = LogisticRegression()
            logistic.fit(train, labelTraining)
            predicted = logistic.predict(test)
            print("\nThe Output below shows the distribution of label probability corresponding to each documents")
            print("rows- document\ncolumns- label order")
            print(logistic.predict_proba(train))
            print("\nThe accuracy of algorithm is :", end='')
            print(logistic.score(train, labelTraining))
            print("Class of Each tested dataset: \n")
            print(predicted)
        else:
            print("no option like this")
            # sys.exit(0)
        iteration = int(input("Enter\n1 to continue once more\n2 to End: "))

    sys.exit(0)


if __name__ == '__main__':
    path = glob('/Users/karthickdurai/Equator/OneDoc/*.txt')  # Enter the file Path of the folder containing the text documents inside glob
    trainData, testData = train_test_split(path, train_size=0.05)
    label = [1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]

    # this is just a random sample its better to manually annotate your training dataset
    # in case of Classification

    classifier(vector=tfidf(filePath=path), labelTraining=label)
