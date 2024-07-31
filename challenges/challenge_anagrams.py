def combine(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_array(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_part = sort_array(array[:middle])
    right_part = sort_array(array[middle:])
    return combine(left_part, right_part)


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    if len(first_string) != len(second_string):
        return ("".join(sort_array(list(first_string))),
                "".join(sort_array(list(second_string))), False)
    if not first_string or not second_string:
        sort_first = "".join(sort_array(list(first_string)))
        sort_second = "".join(sort_array(list(second_string)))
        return (sort_first,
                sort_second, False)
    sort_first = ''.join(sort_array(list(first_string)))
    sort_second = ''.join(sort_array(list(second_string)))
    if sort_first == sort_second:
        return (sort_first, sort_second, True)
    else:
        return (sort_first, sort_second, False)
