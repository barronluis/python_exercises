def palindrome(word: str = 'ana'):
    reversed_word = "".join(reversed(word))
    if word == reversed_word:
        return print("Is palindrome")
    else:
        return print("Is not palindrome")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    palindrome('anitalavalatina')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
