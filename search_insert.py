def search_insert_position(lst, target):
    for i in range (0, len(lst)):
        if lst[i] == target:
            return i
        if lst[i] > target:
            return (i - 1)
