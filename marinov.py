def get_words(text):
    return text.split(' ')

def get_next_possible(word):
    if word == "je":
        return ["suis", "mange"]
