is_instance = __import__('2-is_same_class').is_same_class
print("6 is an instance of int: {}".format(is_instance(6, int)))
print("7.5 is an instance of float: {}".format(is_instance(7.5, float)))
print("5.6 is an instance of int: {}".format(is_instance(5.6, int)))
print("[4, 6, 7] is an instance of tuple: {}".format(is_instance([4, 6, 7], tuple)))
print("[6, 2] is an instance of list: {}".format(is_instance([6, 2], list)))
print("(2, 3, 1) is an instance of tuple: {}".format(is_instance((2, 3, 1), tuple)))
