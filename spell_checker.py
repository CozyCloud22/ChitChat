from autocorrect import Speller

def spellchecker(input_message):
    spell = Speller()

    words = input_message.split()

    corrected_words = [spell(word) for word in words]

    corrected_message = ' '.join(corrected_words)
    return corrected_message

input_message = input("Enter a message: ")
corrected_message = spellchecker(input_message)
print("Corrected message:", corrected_message)
