data = []
import random
a = random.randint(1,1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
print(a)		
print(data[a])