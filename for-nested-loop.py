# Number TABLE
for i in range(1,11):
	for j in range(1,11):
		print("{0} x {1} = {2}".format(i,j,i*j))
	print("============")#Will print table from top to bottom

#####################
for i in range(1,11):
	for j in range(1,11):
		print("{0} x {1} = {2}".format(i,j,i*j),end='\t')
	print('') #prints table from left to right

####################
for i in range(1,11):
	for j in range(1,11):
		print("{0} x {1} = {2}".format(i,j,i*j),end='\t')
		#prints each line side-by-side