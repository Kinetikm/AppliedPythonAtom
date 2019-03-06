#!/usr/bin/env python
# coding: utf-8

def is_bracket_correct(input_string):
	bracket = ['(',')','[',']','{','}']
	count = []
	for i in input_string:
		if i in bracket:
			if ( i == '(' ) or ( i == '{' ) or ( i == '[' ):
				count.append(i)
			else:
				try :
					x = count.pop()
				except:
					return False
				if not (( x == '(' and i == ')') or ( x == '{' and i == '}') or ( x == '[' and i == ']')):
					return False
	return True if len(count) == 0 else False
