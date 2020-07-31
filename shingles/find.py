from itertools import product

# shingle descriptor: "text-fingerprinting"
from text_descriptor import shingle


def shingles_from_text(text, k):
    word_sequence = text.split(" ")
    shingles = set()

    # print(word_sequence)
    for r in range(len(word_sequence)-k+1):
        current_sequence = word_sequence[r: r+k]
        s = shingle(current_sequence)

        shingles.add(s)

    return shingles