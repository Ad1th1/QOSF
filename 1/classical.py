def less_than_k(k, list_n):
    max_int = max(list_n)
    num_bits = max_int.bit_length()
    result = []

    for integer in list_n:
        if integer < k:
            result.append(integer)

    return result

A = less_than_k(7, [4, 9, 11, 14, 1, 13, 6, 15])
print(A)
