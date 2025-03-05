def alternatingCharacters(s):
    count_delete = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count_delete += 1
    return count_delete
