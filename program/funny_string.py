def funnyString(s):
    list_s = []
    for i in s:
        list_s.append(ord(i))

    reverse_list = list_s[::-1]

    for i in range(len(list_s) - 1):
        if abs(list_s[i + 1] - list_s[i]) != abs(reverse_list[i + 1] - reverse_list[i]):
            return "Not Funny"

    return "Funny"
