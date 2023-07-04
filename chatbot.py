#imports
import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = tf.keras.models.load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    """
    Cleans up sentence. Lemmatizer reduces/simplifies the word into a base form in order to better identify the meanings of words.
    :param sentence: Untokenized words.
    :return: Tokenized words.
    """
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    """
    Converts the cleaned up sentence into a comparison between it and the trained model.
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
    :param intents_list:
    :param intents_json:
    :return:
    """

    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tags'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print("Chatbot Running. 'exit' to stop.")

#while loop to keep the bot running until user wants to exit
while True:
    try:
        message = input("")
        ints = predict_class(message)
        res = get_response(ints,intents)
        if(message != "exit"):
            print(res)
    except:
        print("Sorry I don't know~")
    if(message == "exit"):
        break

