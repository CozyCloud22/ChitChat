# from autocorrect import Speller

# def spellchecker(input_message):
#     spell = Speller()

#     words = input_message.split()

#     corrected_words = [spell(word) for word in words]

#     corrected_message = ' '.join(corrected_words)
#     return corrected_message

# input_message = input("Enter a message: ")
# corrected_message = spellchecker(input_message)
# print("Corrected message:", corrected_message)

# from gingerit.gingerit import GingerIt

# def sentence_correction(input_message):
#     parser = GingerIt()

#     corrected = parser.parse(input_message)

#     corrected_sentence = corrected['result']

#     return corrected_sentence

# input_message = input("Enter a message: ")
# corrected_message = sentence_correction(input_message)
# print("Corrected message:", corrected_message)

from autocorrect import Speller
from gingerit.gingerit import GingerIt

def spellchecker(input_message):
    spell = Speller()

    words = input_message.split()

    corrected_words = [spell(word) for word in words]

    corrected_message = ' '.join(corrected_words)
    return corrected_message

def sentence_correction(input_message):
    parser = GingerIt()

    corrected = parser.parse(input_message)

    corrected_sentence = corrected['result']

    return corrected_sentence

input_message = input("Enter a message: ")

corrected_message = spellchecker(input_message)

corrected_message = sentence_correction(corrected_message)

print("Corrected message:", corrected_message)
