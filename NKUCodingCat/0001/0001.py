#coding=utf-8
import os,time,random,hashlib
def md5(str):
	m = hashlib.md5()   
	m.update(str)
	return m.hexdigest()
def salt():
	return "%s"*5 % tuple(random.randint(10000000,99999999) for _ in range(5))
res = [md5(salt()+str(time.time())) for _ in range(200)]
path = f"{os.path.split(os.path.realpath(__file__))[0]}/"
with open(f"{path}code.txt", "w") as f:
	for i in res:
		f.write(i+"\n")