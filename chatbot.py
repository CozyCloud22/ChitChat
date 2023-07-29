import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from collections import OrderedDict

# Have to download file and have it as a local copy and change the path from Darrian's to your own. Ask Darrian if needed.
cred = credentials.Certificate(
    'C:\\Users\\dcnat\\OneDrive\\Desktop\\Coding-Projects\\ChitChat\\chitchat-317ed-firebase-adminsdk-iig8w-dd515155ca.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chitchat-317ed-default-rtdb.firebaseio.com/'
})

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = tf.keras.models.load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    """
    Cleans up sentence.
    :param sentence: Untokenized words.
    :return: Tokenized words.
    """
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    """
    Converts sentence into bag of words.
    :param sentence:
    :return:
    """
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    """
    Creates bag and probabilities to decide which is the correct class.
    :param sentence:
    :return:
    """
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    """
    Function
    :param intents_list:
    :param intents_json:
    :return:
    """
    #try:
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tags'] == tag:
            #checks if the message written is close enough to any of the prepared questions
            if (float(intents_list[0]['probability']) < 0.75):
                result = "The question is unclear, could you please specify"
                return result
            result = random.choice(i['responses'])
            break
    return result
    #except:
     #   print("Sorry, the question is unclear, could you please specify?")
        
print("Chatbot Running")
while True:
    try:
        message = input("")
        ints = predict_class(message)
        res = get_response(ints, intents)

        if (message != "exit"):
            print(res)

    except:
        print("Sorry I don't know. Please check spelling.~")

    tempOutput = get_response(ints, intents)
    # direct upload to google reak time database
    if (message != "exit"):
        ref = db.reference('/User_Input')
        ref.push().set(OrderedDict([
            ('User_Input', message),
            ('Model_Output', tempOutput)
        ]))

    if (message == "exit"):
        break