def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        sub = s[i:i + k]
        seen = set()
        result = ""
        for char in sub:
            if char not in seen:
                result += char
                seen.add(char)
        print(result)

