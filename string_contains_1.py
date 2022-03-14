def contains(string, substring):
    """
        This function determines whether a given substring
        is contained within a given string. For example:

        contains("Hello", "He") -> True
        contains("Hello", "Z") -> False    
    """

    # Loop through the string, one character at a time.
    # On each loop, we compare the string with the substring,
    # starting from index i.

    # The substring must be able to overlap the string,
    # which is why we subtract the length of the substring
    # and add one: this ensures that the last comparison we
    # will do looks like this:
    #
    # contains("Hello", "lo") -> True
    #
    #           "Hello"
    #              "lo"
    #
    # If we did not, our algorithm would attempt to read past
    # the end of the string:
    #
    #           "Hello"
    #                "lo"
    for i in range(len(string) - len(substring) + 1):
        # If the first character of the substring and the ith
        # character of the string do not match, there is no
        # point in continuing.
        if string[i] == substring[0]:
            # Iterate through every character of the substring,
            # and compare to a corresponding character in the string
            # starting from position j
            for j in range(len(substring)):
                if string[i+j] == substring[j]:
                    # If we reach this point, we are at the end of the
                    # substring and all characters to this point have
                    # matched with the string. The substring must be
                    # contained in the string.
                    if j == len(substring) - 1:
                        return True
                else:
                    # If any characters don't match, stop looking and
                    # continue searching through the string.
                    break
                

    # If we reach this point, we never found a match.
    # The substring must not be contained within the string.
    return False

print("Hello contains lo?", contains("Hello", "lo"))
print("Hello contains lz?", contains("Hello", "lz"))