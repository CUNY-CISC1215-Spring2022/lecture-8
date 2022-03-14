def is_palindrome(word):
    """Determine whether a given word is a palindrome."""

    # Base case: All strings with 1 or fewer characters
    # is a palindrome
    if len(word) <= 1:
        return True

    # Base case: If the first and last character of the
    # string do not match, it cannot be a palindrome.
    if word[0] != word[-1]:
        return False
    
    # Recursive case: Remove the first and last character
    # of the word and test on the remaining substring.
    return is_palindrome(word[1:-1])

if __name__ == "__main__":
    # How many palindromes are contained in the words.txt list?
    infile = open("words.txt")

    num_palindromes = 0
    for word in infile:
        word = word.strip()
        if is_palindrome(word):
            num_palindromes += 1

    print(str(num_palindromes) + " palindromes")