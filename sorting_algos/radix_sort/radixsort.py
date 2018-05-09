def radix_sort(lst):
    """Implement radix sort algorithm."""
    if len(lst) < 2:
        return lst

    def fill_buckets(lst, iteration):
        """Divide."""
        buckets = [[] for x in range(10)]
        for number in lst:
            digit = (number // (10 ** iteration)) % 10
            # import pdb; pdb.set_trace()
            buckets[digit].append(number)
        return buckets

    def empty_buckets(buckets):
        lst = []
        for bucket in buckets:
            for number in bucket:
                lst.append(number)
        return lst

    largest = max(lst)
    iteration = 0

    while 10 ** iteration <= largest:
        lst = empty_buckets(fill_buckets(lst, iteration))
        iteration += 1

    return lst
