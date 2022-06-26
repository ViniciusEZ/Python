#Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize
# words or add punctuation, but you should add spaces between each word.

def smash(words):
    return ' '.join(words).strip()

print(smash(['hello', 'world', 'amazing']))
