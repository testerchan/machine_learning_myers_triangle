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

save_str = ''

for i in range(100000):
	a = random.randint(1, 99999)
	b = random.randint(1, 99999)
	c = random.randint(1, 99999)

	rnd = random.randrange(3)
	if rnd == 0:
		ans = judge_triangle(a, b, c)
		save_str += str(a) + ',' + str(b) + ',' + str(c) + ',' + str(ans) + str('\n')
	elif rnd == 1:
		ans = judge_triangle(a, a, a)
		save_str += str(a) + ',' + str(a) + ',' + str(a) + ',' + str(ans) + str('\n')
	elif rnd == 2:
		rnd2 = random.randrange(3)
		if rnd2 == 0:
			ans = judge_triangle(a, a, c)
			save_str += str(a) + ',' + str(a) + ',' + str(c) + ',' + str(ans) + str('\n')
		elif rnd2 == 1:
			ans = judge_triangle(a, b, b)
			save_str += str(a) + ',' + str(b) + ',' + str(b) + ',' + str(ans) + str('\n')
		elif rnd2 == 2:
			ans = judge_triangle(c, b, c)
			save_str += str(c) + ',' + str(b) + ',' + str(c) + ',' + str(ans) + str('\n')


	

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