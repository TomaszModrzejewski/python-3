import uuid

def gen(num, len):
	L = []
	for _ in range(num):
		ran = str(uuid.uuid4()).replace('-', '')[:len]
		if ran not in L:
			L.append(ran)
	return L

if __name__ == '__main__':
	for item in gen(200, 16):
		print(item)
		