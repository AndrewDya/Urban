def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words


result = single_root_words("cat", "category", "cater", "dog", "catnip", "at")
print(result)  # Вывод: ['category', 'cater', 'catnip', 'at']