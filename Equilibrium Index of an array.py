# Python program to find equilibrium 
# Index of an array 

# function to find the equilibrium index 
def equilibrium(arr): 
	leftsum = 0
	rightsum = 0
	n = len(arr) 
	for i in range(n): 
		leftsum = 0
		rightsum = 0
	
		# get left sum 
		for j in range(i): 
			leftsum += arr[j] 
		
		# get right sum 
		for j in range(i + 1, n): 
			rightsum += arr[j] 
		
		# if leftsum and rightsum are same, 
		# then we are done 
		if leftsum == rightsum: 
			return i 
	
	# return -1 if no equilibrium index is found 
	return -1
			
 
arr = [-4, 2, 5, 6, -4, 3, 0] 
print (equilibrium(arr))  
