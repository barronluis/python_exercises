def palindrome(word: str = 'ana'):
    reversed_word = "".join(reversed(word))
    if word == reversed_word:
        return print("Is palindrome")
    else:
        return print("Is not palindrome")


if __name__ == '__main__':
    palindrome('anitalavalatina')
