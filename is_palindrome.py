#pablo - dobrze!
def is_palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False

print(is_palindrome('word'))

#boss
def is_palindrome(text):
    """Checks if text is a palindrome
    Args:
        text: string to be checked
    Returns:
        True if text is palindrome, false if isn't.
    :param text:
    :return:
    """
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text)-i-1]:
            return False
        return True

print(is_palindrome('Oko'))
