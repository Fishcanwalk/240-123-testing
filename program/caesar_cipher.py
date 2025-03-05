def caesarCipher(s, k):
    output = ""

    k = k % 26

    for i in s:
        if i.isalpha():
            if i.isupper():
                i = ord(i)
                i += k
                if i > ord("Z"):
                    i -= 26
                i = chr(i)
            else:
                i = ord(i)
                i += k
                if i > ord("z"):
                    i -= 26
                i = chr(i)
        output += i

    return output
