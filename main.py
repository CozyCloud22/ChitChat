import csv
import nltk
import re
import json
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def tokenize(data):
    """
    Tokenizes a CSV file list.
    :param data: List of strings.
    :return: List of tokenized strings.
    """
    data = to_lower(data)
    data = sentence_token(data)[0]
    data = word_token(data)
    data = clean_special(data)
    #data = remove_stopword(data)  # REMOVES IMPORTANT CONTEXT LIKE 'WHEN' OR 'WHERE', THIS COULD CAUSE ISSUES.
    #data = lemmatizer(data)  # These two functions can be used or not, we don't know if they should or not. Lemmatizer doesn't seem to change much of the sentence at all.
    return data


def lemmatizer(data):
    """
    Lemmatizes words, which means it groups different inflected forms of the same word so the NLP can more easily process it.
    :param data:
    :return:
    """
    wnet = WordNetLemmatizer()
    clean_list = []

    for word in data:
        clean_list.append(wnet.lemmatize(word))

    return clean_list


def remove_stopword(data):
    """
    Removes "Stopwords" from data list.
    :param data: List of tokens.
    :return: List of tokens without "Stopwords".
    """
    clean_list = []

    for word in data:
        if word not in stopwords.words('english'):
            clean_list.append(word)

    return clean_list


def clean_special(data):
    """
    Removes all special characters from the list of data.
    :param data: List of strings.
    :return: List of strings.
    """
    clean_list = []

    for sentence in data:
        for word in sentence:
            clean = ""
            for i in word:
                remove = re.sub(r'[^\w\s]', "", i)  # NGL I ripped this straight from a YT video.
                if remove != "":
                    clean += remove
            if clean != "":
                clean_list.append(clean)
    return clean_list


def word_token(data):
    """
    Tokenizes any words within the list of data.
    :param data: list of strings.
    :return: Tokenized words of those strings in form of a list.
    """
    return [word_tokenize(i) for i in data]


def sentence_token(data):
    """
    Tokenizes any sentences within the list of data.
    :param data: List of strings.
    :return: Tokenized sentences of those strings in form of a list.
    """
    return [sent_tokenize(i) for i in data]


def to_lower(data):
    """
    Lowercases all strings in a list.
    :param data: List of strings.
    :return: Lowercase list of strings.
    """
    return [i.lower() for i in data]


def csv_to_string(file_name):
    """
    Reads CSV file into a single string contained in a list.
    :param file_name: Name of CSV file.
    :return: List containing one sting of entire CSV file.
    """
    file_list = list(pd.read_csv(file_name))
    whole_text = ""

    for i in file_list:
        whole_text += i

    return [whole_text[3:]]


def open_file():
    ask = input("Enter CSV Filename: ")
    while True:
        try:
            fp = open(ask + ".csv")
            return fp
        except:
            print("\nError: File not found.")
            ask = input("Enter CSV Filename: ")


def main():
    csv_file = open_file()

    if csv_file:
        text_list = csv_to_string(csv_file)
        text_list = tokenize(text_list)
        print(text_list)

        csv_file.close()
    else:
        print("Failed to open CSV file.")


if __name__ == '__main__':
    main()
