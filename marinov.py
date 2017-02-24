import random

def get_words(text):
    return text.split(' ')

def get_next_word(current_word, text):
        positions = get_next_words_positions(current_word, text)
        word_choice = random.choice(positions)
        return text[word_choice]

def get_next_words_positions(current_word, text):
        positions_next_word = [position + 1  for position, text_words  in enumerate(text) if text_words  == current_word]
        return positions_next_word
