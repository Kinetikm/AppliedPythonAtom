#!/usr/bin/env python
# coding: utf-8

def advanced_calculator(input_string):
	if input_string.isalpha() or len (input_string) == 0:
		return None
	bad = ['**','//','%','<<','>>','&','|','<','>','<=','>=','==','not','and','or']
	for i in bad:
		if (input_string.find(i) != -1):
			return None
	try :
		x = eval(input_string)
	except:
		return None
	return x if (type(x) is int or type(x) is float) else None