data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*data_str):
    sum_ = 0
    for i in data_str:
        if isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            for j in i:
                sum_ += calculate_structure_sum(j)
        elif isinstance(i, tuple):
            for j in i:
                sum_ += calculate_structure_sum(j)
        elif isinstance(i, set):
            for j in i:
                sum_ += calculate_structure_sum(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                sum_ += calculate_structure_sum(key, value)
        elif isinstance(i, int):
            sum_ += i
    return sum_


result = calculate_structure_sum(data_structure)
print(result)

#Сложно было пару раз запутался, сначала сделал решение без функции потом думал как собрать все
# это в 1 функцию перечитал задание увидел подсказку про isinstance и все получилось