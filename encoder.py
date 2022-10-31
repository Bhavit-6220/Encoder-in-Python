# Taking input
data = input("Hello, pls enter the message\n")

#combined characters
combined_chars = {
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U',
    'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
    'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
    'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
    'Y': 'B', 'Z': 'A',
 
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
    'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
    'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
    's': 'h', 't': 'g', 'u': 'F', 'v': 'e', 'w': 'd', 'x': 'c',
    # I've these copied. You can find then in description

}

#encoded message
encoded_message = ""

for i in range(0, len(data)):
    if data[i] in combined_chars.keys():
        encoded_message += combined_chars[data[i]]
    else:
        encoded_message += data[i]

print(f"Your message is {encoded_message}")