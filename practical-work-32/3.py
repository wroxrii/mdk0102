def get_max_index(numbers):
    max_index = 0
    max_value = max(numbers)

    for index, value in enumerate(numbers):
        if index > max_index and value == max_value:
            max_index = index
            max_value = value

    return max_index


print(get_max_index([91, 98, 175, 112, 119, 126, 133, 140, 175, 147, 154, 161, 168]))
print(get_max_index([91, 98, 112, 168, 119, 126, 133, 168, 140, 147, 154, 161]))
