def most_frequent_item_count(collection):
    most = 0
    if len(collection) != 0:
        for i in collection:
            x = collection.count(i)
            if x> most:
                most = x
    return most