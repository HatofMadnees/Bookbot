# stats.py
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


# stats.py

# ... (previous functions remain the same)

def sort_on(item):
    """Helper function for the .sort() method"""
    return item["num"]


def sorted_chars_list(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        # Only include alphabetical characters
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            sorted_list.append(new_dict)

    # Sort descending (greatest to least)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
