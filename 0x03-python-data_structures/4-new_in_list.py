#/usr/bin/python3
def new_in_list(my_list, idx, element):
    clone_list = my_list.copy()
    length = len(my_list)
    if idx < 0:
        return clone_list
    if idx >= length:
        return clone_list
    for i in range(length):
        if i == idx:
            clone_list[i] = element
            return clone_list
