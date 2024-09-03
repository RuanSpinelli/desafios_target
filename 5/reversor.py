def reversor_string(string):
    cadeia_char = []

    for c in range(len(string) - 1, -1 , -1):
        print(f"{string[c]}",end="")
        cadeia_char.append(string[c])

    string_invertida =  ''.join(cadeia_char)

    return string_invertida
