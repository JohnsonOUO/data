data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1#count = count + 1
		if count % 1000 == 0:
			len(data)

print('總共有',len(data),'筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均是', sum_len/len(data))	
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))

good = [d for d in data if 'good' in d]
bad = ['bad' in d for d in data]		

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('平均是', sum_len/len(data))	
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))

good = [d for d in data if 'good' in d]
bad = ['bad' in d for d in data]		



print(data[0])

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] >10000:
		print(word, wc[word])

print(len(wc))	

while True:
	word = input('請問你要找的字 :')
	if word == 'q':
		break
	if word in wc:
		print(wc[word])	
	else:
		print('沒有出現喔')		
print('謝謝使用')		

	



