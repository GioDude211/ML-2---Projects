import matplotlib as mlp
import numpy as ny


def remove_word(filename, word):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    new_text = text.replace(word, ' ')

    with open(filename, 'w',  encoding='utf-8') as file:
        file.write(new_text)

#Example usage
filename = "D:\GioDude\Documents\ACC\Spring 2024\Machine Learning II\Datasets\DnD Scripts\cr_dnd_transcripts_1.txt"
word_to_remove = "→"  # Replace with the word you want to remove
remove_word(filename, word_to_remove)