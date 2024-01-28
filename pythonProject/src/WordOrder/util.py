import collections

def count_word_occurrences(n, words):
    word_counts = collections.OrderedDict()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    print(len(word_counts))  # Print the number of distinct words
    print(*word_counts.values())  # Print the occurrence counts in order
