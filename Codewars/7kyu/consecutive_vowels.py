# You are given a random string of lower-case letters. Your job is to find out
# how many ordered and consecutive vowels there are in the given string beginning from 'a'. Keep in mind
# that the consecutive vowel to 'u' is 'a' and the cycle continues.
# Return an integer with the length of the consecutive vowels found.


def get_the_vowels(word):
    c = 0
    for i in word:
        if i in 'aeiou'[c%5]:
            c += 1
    return c


print(get_the_vowels("akfheujfkgiaaaofmmfkdfuaiiie"))
