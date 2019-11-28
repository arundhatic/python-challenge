"""
Import a text file filled with a paragraph of your choosing.

Assess the passage for each of the following:

Approximate word count

Approximate sentence count

Approximate letter count (per word)

Average sentence length (in words)

As an example, this passage:

“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”

...would yield these results:
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0

"""

import os
import csv
import re

paragraphPath = os.path.join("Resources", "paragraph.txt")

def pyParagraphAnalysis(filepath):
    wordCount = []
    with open(filepath, 'r') as f:
        file_contents = f.read()
        words = len(file_contents.split())
        sentence_count = file_contents.count('.')
        letter_count_per_word = {w:len(w) for w in file_contents.split()}
        
        for l in re.split(r"\.|\?|\!",file_contents):
             num_words_per_sentence=len(l.split(" "))
             wordCount.append(num_words_per_sentence)
        average_word_sentence = sum(wordCount)/len(wordCount)
        #print( average_word_sentence)
    #print('Total words: ', words)
    #print('Total sentences: ', file_contents.count('.'))
    #print(letter_count_per_word)
    total_letter_count_per_word = sum(letter_count_per_word.values())
    average_count = round(total_letter_count_per_word/words, 2)
    #print(average_count)
        
    output=''
    output+='Paragraph Analysis\n'
    output+='-----------------\n'
    output+=f'Approximate Word Count: {words}' + '\n'
    output+=f'Approximate Sentence Count: {sentence_count}' + '\n'
    output+=f'Average Letter Count (per word): {average_count}' + '\n'
    output+=f'Average Sentence Length (in words): {average_word_sentence}' + '\n'
    
    print(output)
        
def main():
        pyParagraphAnalysis(paragraphPath )


if __name__ == "__main__":
    main()  