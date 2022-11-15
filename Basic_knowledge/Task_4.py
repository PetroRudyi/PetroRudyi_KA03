import numpy as np


def numberCounter(list_numbers, target):
    res = np.array([[0, 0]])
    mini = min(list_numbers)
    norm_list = [x for x in list_numbers if (x <= (
                target - mini))]  # забираємо зайві числа і ті пари мін макс що не приведуть до результату Наприклад мін = 0, а є при числі 5 6, то 6 ніколи не принесе 5
    for i in range(len(norm_list)):
        for j in range(i, len(norm_list)):
            if norm_list[i] + norm_list[j] == target:
                res = np.append(res, np.array([[norm_list[i], norm_list[j]]]), axis=0)
    res = np.delete(res, 0, 0)
    res = np.unique(res, axis=0)
    return res.tolist()


numberCounter([1, 3, 6, 2, 2, 0, 4, 5], 5)
