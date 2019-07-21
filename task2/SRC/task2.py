def position_point(point_1, point_2, point_p):
	return ((point_2[0] - point_1[0])*(point_p[1] - point_1[1]) -
	 	    (point_p[0] - point_1[0])*(point_2[1] - point_1[1]))

def rect(*points):
	def equation(*check_point):
		if check_point in points:
			return 0
		D = [position_point(points[0], points[1], check_point),
			 position_point(points[1], points[2], check_point),
			 position_point(points[2], points[3], check_point),
			 position_point(points[3], points[0], check_point)]
		if any(d == 0 for d in D) and (all(d >= 0 for d in D) or
									   all(d <= 0 for d in D)):
			return 1
		if all(d > 0 for d in D) or all(d < 0 for d in D):
			return 2
		else:
			return 3
	return equation

def read_point(s):
	A = []
	with open(s, 'r') as f:
		for line in f:
			A.append(tuple(float(x) for x in (line.rstrip().split())))
	return A

s_1 = input()
s_2 = input()
#s_1 = '2_fig.txt'
#s_2 = '2_point.txt'
rect_point = read_point(s_1)
check_points = read_point(s_2)

validate = rect(*rect_point)

for point in check_points:
	print(validate(*point))