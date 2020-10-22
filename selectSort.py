def select_sort(lst):
    ans = []
    for i in range(len(lst)):
        x = min(lst)
        ans.append(x)
        lst.remove(x)
    return ans
