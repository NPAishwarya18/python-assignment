def generate_shift_table(pattern):
    table = {}
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - 1 - i
    return table

def horspool_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    shift_table = generate_shift_table(pattern)
    i = pattern_length - 1  # Index in the text

    while i < text_length:
        k = 0  # Index in the pattern
        while k < pattern_length and pattern[pattern_length - 1 - k] == text[i - k]:
            k += 1
        if k == pattern_length:
            return i - pattern_length + 1  # Match found
        else:
            shift = shift_table.get(text[i], pattern_length)
            i += shift

    return -1  # Match not found

# Taking user input
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

result = horspool_search(text, pattern)
if result != -1:
    print(f"Pattern found at index {result}")
else:
    print("Pattern not found")
