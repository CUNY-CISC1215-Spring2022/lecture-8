def contains(string, substring):
    """
        This function determines whether a given substring
        is contained within a given string. For example:

        contains("Hello", "He") -> True
        contains("Hello", "Z") -> False    
    """

    for i in range(len(string)):
        if substring == string[i:i + len(substring)]:
            return True
    return False

print("Hello contains lo?", contains("Hello", "lo"))
print("Hello contains lz?", contains("Hello", "lz"))