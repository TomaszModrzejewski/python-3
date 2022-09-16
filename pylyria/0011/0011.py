# -*- coding: utf-8 -*-
#!/usr/bin/env python

def is_sensitive(word):
	sensitive_words = [line.strip() for line in open('sensitive.txt', encoding='utf-8')]
	word = word.strip()
	return word.lower() in sensitive_words

if __name__ == "__main__":
    while 1:
    	if is_sensitive(input()):
    		print('Freedom')
    	else:
    		print('Human Rights')
