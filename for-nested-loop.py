# Number TABLE
for i in range(1,11):
	for j in range(1,11):
		print("{0} x {1} = {2}".format(i,j,i*j))
	print("============")

#####################
for i in range(1,11):
	for j in range(1,11):
		print("{0} x {1} = {2}".format(i,j,i*j),end='\t')
	print('')

####################
for i in range(1,11):
	for j in range(1,11):
		print("{0} x {1} = {2}".format(i,j,i*j),end='\t')