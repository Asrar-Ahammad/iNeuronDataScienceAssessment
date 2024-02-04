def highest_frequency_word_length(s):
    words = s.split()
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    if not word_freq:
        return 0

    max_freq_word = max(word_freq, key=word_freq.get)
    return len(max_freq_word)

# Example usage:
input_string = "write write write all the number from from from 1 to 100"
output_length = highest_frequency_word_length(input_string)
print(output_length)
