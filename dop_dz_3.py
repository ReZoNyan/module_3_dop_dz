def checker(element):
    sum = 0
    if isinstance(element, dict):
        for key, value in element.items():
            sum += checker(key)
            sum += checker(value)
    if isinstance(element, list) or isinstance(element, set) or isinstance(element, tuple):
        for i in element:
            sum += checker(i)
    if isinstance(element, int) or isinstance(element, float):
        sum += element
    if isinstance(element, str):
        sum += len(element)
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

res = checker(data_structure)
print(res)