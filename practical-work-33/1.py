import copy

data = {'a': [1, 2, 3], 'b': [4, 5, 6]}


def add_to_list_in_dict(dictionary, key, value):
    result = copy.deepcopy(dictionary)
    try:
        result[key].append(value)
    except KeyError:
        result[key] = value
    return result


print(add_to_list_in_dict(data, 'b', 7))
print(add_to_list_in_dict(data, 'c', 7))
