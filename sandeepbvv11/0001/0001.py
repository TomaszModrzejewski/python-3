import uuid
import random
st= 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*'
for _ in range(200):
    x=str(uuid.uuid4().fields[-1])[:10]+st
    y = ''.join(random.choice(x) for _ in range(10))
    print (y+"\n")
    



