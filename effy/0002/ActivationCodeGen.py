#!/usr/bin/env
import random

codeSeedA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def digit(raw):
	l = len(raw)
	return raw[random.randrange(l)] 

def codeGen(n):
	codes_pool = []
	for _ in range(n):
		code = "".join(digit(codeSeedA) for _ in range(10))
		codes_pool.append(code)
	return codes_pool
