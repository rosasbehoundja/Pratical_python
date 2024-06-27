# a function that check if a string is a palindrom

def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]


print(is_palindrome('dog'))
