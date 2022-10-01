#!/usr/bin/python3
a_dict = a_dictionary
if a_dict == None:
	return None
keyz = list(a_dict.keys())
maxK = keyz[0]
for key in keyz:
	if a_dict.get(key) > a_dict.get(maxK):
		maxK = key
return maxK
