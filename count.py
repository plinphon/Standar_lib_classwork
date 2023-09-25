from collections import Counter

def most_frequent_item_count(ints):
    return 0 if not ints else Counter(ints).most_common(1)[0][1]