from random import shuffle


def shuffle_word(match_obj) -> str:
    word = match_obj.group(0)
    if len(word) <= 3:
        return word

    middle_chars = list(word[1:-1])
    shuffle(middle_chars)
    return word[0] + ''.join(middle_chars) + word[-1]