def alternate(s):
    unique_chars = list(set(s))
    max_length = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            output = ""
            for c in s:
                if c == char1 or c == char2:
                    output += c
            is_alternating = True
            for k in range(1, len(output)):
                if output[k] == output[k - 1]:
                    is_alternating = False
                    break
            if is_alternating:
                if len(output) > max_length:
                    max_length = len(output)

    return max_length
