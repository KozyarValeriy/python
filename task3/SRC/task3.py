def read_data(s):
	A = []
	with open(s, 'r') as f:
		for line in f:
			A.append(float(line.rstrip()))
	return A

def find_max_interval(A):
	current = 0
	best = [0, 0]
	for col in range(len(A[0])):
		for row in range(len(A)):
			current += A[row][col]
		#print('{0: >4.2f}'.format(current), end=' ')
		if current > best[0]:
			best[0] = current
			best[1] = col + 1
		current = 0
	return best

s = input()
#s = 'E:\\Программирование\\Для вакансий\\PerfomanceLab\\task_3'
if s[-1] != '\\':
	s = s + '\\'
names = ['Cash' + str(i) + '.txt' for i in range(1, 6)]
time_cash = []
for name in names:
	time_cash.append(read_data(s + name))
answer = find_max_interval(time_cash)
#print()
#print('Max is {0:.2f} in col {1}'.format(*answer))
print(answer[1])