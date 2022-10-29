#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("myFile.txt", "This School is so cool!\n")
print(nb_characters_added)
