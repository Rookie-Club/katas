import random

def get_words(text):
    words = []
    sentences = text.split(", ")
    for i in sentences:
        words.append(i.split(" "))
    return words

def get_next_word(current_word, text):
        positions = get_next_words_positions(current_word, text)
        word_choice = random.choice(positions)
        return text[word_choice]

def get_next_words_positions(current_word, text):
        positions_next_word =[]
        for position, text_words  in enumerate(text):
            if text_words  == current_word:
                if current_word  == text[-1]:
                    positions_next_word.append(random.randint(0, position))
                else:
                    positions_next_word.append(position+1)
        return positions_next_word
