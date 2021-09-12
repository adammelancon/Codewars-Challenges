#https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
'''# Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.'''

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def high(x):
    words = x.split()
    print(words)
    score = []
    final_scores = []

    for word in words:
        letter_score = []
        for letter in word:
            letter_score.append(getscore(str(letter)))
        print(letter_score)
        score.append(letter_score)
    for word in score:
        x = sum(word)
        final_scores.append(x)


    print(f"Final Scores: {final_scores}")
    print(f"       Words: {words}")
    print(f"Largest Word Index: {final_scores.index(max(final_scores))}")
    print(f"      Longest Word: {words[final_scores.index(max(final_scores))]}")
    winner_index = final_scores.index(max(final_scores))
    winning_word = words[final_scores.index(max(final_scores))]
    return winning_word

def getscore(alpha_lookup):
    # print(alpha.index(alpha_lookup) + 1)
    return alpha.index(alpha_lookup) + 1 




high('man i need a taxi up to ubud')#, 'taxi')
# high('what time are we climbing up the volcano')#, 'volcano')
# high('take me to semynak')#, 'semynak')
# high('aa b')#, 'aa')
# high('b aa')#, 'b')
# high('bb d')#, 'bb')
# high('d bb')#, 'd')
# high("aaa b")#, "aaa")