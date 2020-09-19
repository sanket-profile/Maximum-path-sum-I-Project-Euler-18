def neighbours(l, a):
	if (a[0] , a[1]) == (a[0] , 0):
		neighbour = [(a[0]-1 , 0)]
	elif (a[0],a[1]) == (a[0] , len(l[a[0]]) - 1):
		neighbour = [(a[0]-1 , a[1]-1)]
	else:
		neighbour = [(a[0]-1 , a[1]-1) , (a[0]-1 , a[1])]
	return(neighbour)

def path(l , a , n):
	d = {}
	e ={}
	num = 0
	for i in range(n):
		for j in range(i+1):
			if (i,j) == (0,0):
				d[str((0 , 0))] = 1
				e[str((0 , 0))] = [[l[0][0]]]
			else:
				neighbour = neighbours(l , (i,j))
				if len(neighbour) > 1:
					d[str((i , j))] = d[str(neighbour[0])] + d[str(neighbour[1])]
					e[str((i,j))] = []
					for k in range(len(e[str(neighbour[0])])):
						e[str((i, j))].extend([[l[i][j]]])
						a = e[str(neighbour[0])][k]
						e[str((i,j))][k].extend(a)
					for k in range(len(e[str(neighbour[0])]),len(e[str(neighbour[0])])+len(e[str(neighbour[1])])):
						e[str((i, j))].extend([[l[i][j]]])
						a = e[str(neighbour[1])][k - len(e[str(neighbour[0])])]
						e[str((i,j))][k].extend(a)
				else:
					d[str((i , j))] = d[str(neighbour[0])]
					e[(str((i,j)))] = [[l[i][j]]]
					e[(str((i,j)))][0].extend(e[str(neighbour[0])][0])
	for i in range(n):
		a =e[str((n-1 , i))]
		for j in a:
			if sum(j) > num:
				num = sum(j)
				m = j
			else:
				pass
	return(num , m)