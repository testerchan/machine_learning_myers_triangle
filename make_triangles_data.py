import random

def judge_triangle(a, b, c):
	if a + b <= c or b + c <= a or c + a <= b :
		return 0
	if a == b and a == c:
		return 1
	if a == b or b == c or c == a:
		return 2
	else:
		return 3

def save_file(file_name, s):
	with open(file_name, 'w') as f:
		f.write(s)

def shuffle(a, b, c):
	l = [a, b, c]
	random.shuffle(l)
	return l[0], l[1], l[2]

save_str = ''

for i in range(10000):
	a = random.randint(1, 100000)
	b = random.randint(1, 100000)
	c = random.randint(1, 100000)

	rnd = random.randrange(3)
	if rnd == 0:
		rnd2 = random.randrange(3)
		#a = b + cの場合
		if rnd2 == 0:
			b = random.randrange(a)
			c = a - b
			a,b,c = shuffle(a, b, c)
			ans = judge_triangle(a, b, c)
		else:
			ans = judge_triangle(a, b, c)
	elif rnd == 1:
		b = a
		c = a
		ans = judge_triangle(a, b, c)
	elif rnd == 2:
		a,b,c = shuffle(a, a, c)
		ans = judge_triangle(a, b, c)
	save_str += str(a) + ',' + str(b) + ',' + str(c) + ',' + str(ans) + str('\n')
		
			


	

save_file('teacher_data.csv', save_str)

'''
print(judge_triangle(1,2,3))
print(judge_triangle(1,1,1))
print(judge_triangle(2,2,3))
print(judge_triangle(1,3,3))
print(judge_triangle(2,2,3))
print(judge_triangle(3,4,5))
print(judge_triangle(1000,4,5))
print(judge_triangle(5,1000,5))
'''