import uuid

for i in range(1, 201):
	f = open('code.md', 'ar+')
	s = f"{str(i)}. {str(uuid.uuid4())}"
	f.write(s+"\n")
