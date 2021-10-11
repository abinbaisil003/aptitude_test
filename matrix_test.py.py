
def Matrix(N, M) :
	#initialising parameters
	Sumof_diagonals = 0
	row_repeat = 0
	column_repeat = 0

	for i in range(N) :
		for j in range(N) :
			if (i == j):
			    Sumof_diagonals+= M[i][j]
		flag1 = 0

		for j in range(N) :
			for k in range(N) :
				if (j != k and M[i][j] == M[i][k]) :
					row_repeat += 1
					flag1 = 1
					break
			if (flag1 == 1) :
				break
		flag2 = 0

		for j in range(N) :
			for k in range(N) :
				
				if (j != k and M[j][i] == M[k][i]) :
					column_repeat += 1
					flag2 = 1
					break
				
			if (flag2 == 1) :
				break

	print(Sumof_diagonals, row_repeat, column_repeat)

M = [[ 2, 1, 3 ],
	[ 1, 3, 2 ],
	[ 1, 2, 3 ]]		
N = len(M)
Matrix(N, M)


