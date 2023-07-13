# For some reason it doesnt like the run button on the right use the "Run" "Start Debugging" or "Start Without Debugging"
from autocorrect import Speller
# uh for this pip install autocorrect
from gingerit.gingerit import GingerIt
# and for this pip install gingerit
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
