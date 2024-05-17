def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if n < m or m == 0:
        return []

    prime = 101


    def calculate_hash(s):
        hash_val = 0
        for char in s:
            hash_val = (hash_val * prime + ord(char)) % prime
        return hash_val

    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[:m])

    indices = []

    if pattern_hash == text_hash and text[:m] == pattern:
        indices.append(0)


    for i in range(1, n - m + 1):

        text_hash = (text_hash - ord(text[i - 1]) * (prime ** (m - 1))) % prime
        text_hash = (text_hash * prime + ord(text[i + m - 1])) % prime


        if pattern_hash == text_hash and text[i:i + m] == pattern:
            indices.append(i)

    return indices


haystack = "ababcababc"
needle = "abc"
print(rabin_karp_search(haystack, needle))
def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if n < m or m == 0:
        return []

    prime = 101


    def calculate_hash(s):
        hash_val = 0
        for char in s:
            hash_val = (hash_val * prime + ord(char)) % prime
        return hash_val

    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[:m])

    indices = []

    if pattern_hash == text_hash and text[:m] == pattern:
        indices.append(0)


    for i in range(1, n - m + 1):

        text_hash = (text_hash - ord(text[i - 1]) * (prime ** (m - 1))) % prime
        text_hash = (text_hash * prime + ord(text[i + m - 1])) % prime


        if pattern_hash == text_hash and text[i:i + m] == pattern:
            indices.append(i)

    return indices


haystack = "ababcababc"
needle = "abc"
print(rabin_karp_search(haystack, needle))
