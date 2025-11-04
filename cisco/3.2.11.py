word_without_vowels = ""

# Prompt the user to enter a 
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("user to enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop. A, E, I, O, U 
    if letter == "A": 
        continue
    elif letter =="E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    word_without_vowels = word_without_vowels + letter
print(word_without_vowels)


