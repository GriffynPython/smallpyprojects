#Find zero width chars in a text string to get a hidden code.
import re
import unicodedata

# Define the zero-width characters
zero_width_chars = {
    '\u200B': 'ZERO WIDTH SPACE',
    '\u200C': 'ZERO WIDTH NON-JOINER',
    '\u200D': 'ZERO WIDTH JOINER',
    '\uFEFF': 'ZERO WIDTH NO-BREAK SPACE'
}

# Function to find zero-width characters in text
def find_zero_width_chars(text):
    found_chars = [] #Initialize a empty  list
    for char in text:
        if char in zero_width_chars:
            found_chars.append((char, zero_width_chars[char]))
    return found_chars

# Given tweet
tweet = "Ｃhｏose  a  jοｂ  yоu lονｅ,  and  you  ｗіｌl  ｎeｖｅｒ  have tο ｗｏrk  a  day  in  yοur lіfｅ．"

# Detect zero-width characters
hidden_info = find_zero_width_chars(tweet)

# Print results
if hidden_info:
    print("Zero-width characters found:")
    for char, name in hidden_info:
        print(f"Character: '{char}' | Unicode Name: {name}")
else:
    print("No zero-width characters found.")
