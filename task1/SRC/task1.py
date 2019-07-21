import math

def read_file(s):
	A = []
	with open(s, 'r') as f:
		for line in f:
			A.append(int(line.rstrip()))
	A.sort()
	return A

def solve_task(A, percent=0.9):
	assert isinstance(A, list), ('List required, received ' + str(type(A)))
	assert len(A), ('List is empty')
	N = len(A)
	if percent < 1 and N > 1:
		n = percent*(N - 1) + 1
		fract_part, int_part = math.modf(n)
		int_part = int(int_part)
		percentile = A[int_part - 1] + fract_part*(A[int_part] - A[int_part - 1])
	else:
		percentile = A[-1]
	if N%2 == 1:
		mediana = A[N//2]
	else:
		mediana = (A[N//2] + A[(N//2) - 1]) / 2
	max_seq = A[-1]
	min_seq = A[0]
	average = (sum(A) / N)
	return (percentile, mediana, max_seq, min_seq, average)

#s = 'E:\\Программирование\\Для вакансий\\PerfomanceLab\\1.txt'
s = input()
res = read_file(s)
answer = solve_task(res)

print('{0:.2f}\n{1:.2f}\n{2:.2f}\n{3:.2f}\n{4:.2f}\n'.format(*answer)) # *answer, sep='\n')

'''
if __name__ == '__main__':
	import numpy as np
	cheak = np.array(res)
	print('OK - {0: >5.2f} <> {1: >5.2f} - MY'.format(np.percentile(cheak, 90), answer[0]))	
	print('OK - {0: >5.2f} <> {1: >5.2f} - MY'.format(np.median(cheak), answer[1]))	
	print('OK - {0: >5.2f} <> {1: >5.2f} - MY'.format(np.max(cheak), answer[2]))
	print('OK - {0: >5.2f} <> {1: >5.2f} - MY'.format(np.min(cheak), answer[3]))
	print('OK - {0: >5.2f} <> {1: >5.2f} - MY'.format(np.average(cheak), answer[4]))
'''
