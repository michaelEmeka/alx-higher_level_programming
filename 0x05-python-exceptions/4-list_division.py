#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    This function divides my_list_1 by my_list_2 based
    on list_length to be divided

    Args:
        my_list_1: dividend list
        my_list_2: divisor list
        list_length: list length to be divided
    """
    new_list = list(range(list_length))
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            val = 0
            continue
        except (TypeError, ValueError):
            print("wrong type")
            val = 0
            continue
        except IndexError:
            print("out of range")
            val = 0
            continue
        finally:
            new_list[i] = val

    return new_list
