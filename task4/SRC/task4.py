def read_data(s):
	A = []
	with open(s, 'r') as f:
		for line in f:
			time_in, time_out = line.rstrip().split()
			A.append((get_mins(time_in), get_mins(time_out)))
	return A

def get_mins(s):
	s = [int(x) for x in s.split(':')]
	s = s[0]*60 + s[1]
	return s

def find_interval(A):
	max_count = 0
	res = []
	for i in range(len(A) - 1):
		tmp = []
		for j in range(i + 1, len(A)):
			if A[j][1] > A[i][0] and A[j][0] < A[i][1]:
				max_border = min(A[j][1], A[i][1])
				min_border = max(A[j][0], A[i][0])
				for iter_tmp in range(len(tmp)):
					if (tmp[iter_tmp][0] < max_border and
						min_border < tmp[iter_tmp][1]):
						tmp[iter_tmp][0] = min(tmp[iter_tmp][0], min_border) 
						tmp[iter_tmp][1] = max(tmp[iter_tmp][1], max_border)
						tmp[iter_tmp][2] += 1
						break
				else:
					tmp.append([min_border, max_border, 2])
		connect_list = 	find_max_elements(tmp)
		if connect_list:	
			res += find_max_elements(tmp)
	res = find_max_elements(res)
	for i in range(len(res) - 1, 0, -1):
		for j in range(i - 1, -1, -1):
			if res[i][0] <= res[j][1] and res[i][1] >= res[j][1]:
				res[j][1] = res[i][1]
				res.pop(i)			
	return res

def find_max_elements(A):
	res = []
	if len(A) == 0:
		return None
	max_count = max([x[2] for x in A])	
	for el in A:
		if el[2] == max_count:
			res.append(el)
	return res

s = input()
#s = 'task_4.txt'
data = read_data(s)
#print(data)
answer = find_interval(data)
for el in answer:
	print('{0:2d}:{1:0>2d} {2:2d}:{3:0>2d}'.format(el[0]//60, el[0]%60, el[1]//60, el[1]%60))
#print(answer)