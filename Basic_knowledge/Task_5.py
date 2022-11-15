import numpy as np


def sortNameSurnameList(list_of_names):
    my_list = list_of_names.split(";")
    arr = []
    for i in my_list:
        arr.append(i.split(":"))
    arr_n = np.array(arr)
    dt = [('col1', arr_n.dtype), ('col2', arr_n.dtype)]
    assert arr_n.flags['C_CONTIGUOUS']
    b = arr_n.ravel().view(dt)
    b.sort(order=['col1', 'col2'])

    return list(zip(arr_n.T[1], arr_n.T[0]))


sortNameSurnameList("Fred:Corwill;Wilfred:ryfff;Alfred:Corwill")
