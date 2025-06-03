def process_array(arr):
    positive_sum = sum(x for x in arr if x > 0)
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    product_between = 1
    for x in arr[min_index + 1:max_index]:
        product_between *= x

    return positive_sum, product_between