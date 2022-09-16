#coding=utf-8
import os,sys,re

def each(path):
	All = []
	for root, dirs, files in os.walk(path):
		All.extend(f"{root}/{name}" for name in files)
	return All
def deal(input):
	if os.path.splitext(input)[1] not in [".py", ".pyw"]:
		return 0,0,0
	total,comment,empty = 0,0,0
	f = open(input,"r")
	in_comment = False
	for line in f:
		total+=1
		if re.findall("\"\"\"$",line):
			in_comment = not in_comment
		if not re.findall("\S",line):
			empty+=1
		if line[0] == "#" or in_comment:
			comment += 1
	return total,comment,empty
		
		
if len(sys.argv)<=1:
	print "The Script will calculate the LOC of the file in "+os.path.split(os.path.realpath(__file__))[0]+"/"
	path = os.path.split(os.path.realpath(__file__))[0]+"/"
else:
	print "calculating the file in "+sys.argv[1]
	if os.path.isdir(sys.argv[1]):
		path = sys.argv[1]
	else:
		print "Path Error! use this script as "+os.path.split(os.path.realpath(__file__))[1]+" [path]"
t,c,e = 0,0,0
for i in each(path):
	t_a,c_a,e_a = deal(i)
	t+=t_a
	c+=c_a
	e+=e_a
print("Total lines: %s. Empty lines: %s. Comment Lines: %s." % (t, e, c))