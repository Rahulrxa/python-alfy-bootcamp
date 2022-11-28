# Time Complexity

# time complexity of below function is O(n*n), because both loop 1 and loop 2 is executed n times
def func(n):
    for i in range(n):
        for j in range(n):
            if j < I:
                break


# time complexity of below function is O(n)*O(n) which is O(n*n), because loop in this function executes n times and the inner function is O(n)
def func(L):
    for v in L:
        # helper func time complexity is O(n)
        helper_func(v)

# time complexity of below function is O((log n) + m), because loop 1 is executed log n times and loop 2  is executed m times
def func(n):
    j = n
    while j > 0:
        j = j // 2
    while j < n:
        j = j + 3
        n = n - 5
    return j


# time complexity of below function is O(log n), because loop is executed log n times
def func(n):
		total = 0
		while n > 5:
				n = n // 2
				# Remember the time complexity of the sum and range methods
				total += sum(range(n))
		return total

# time complexity of below function is O(n), because loop is executed n times
def func(n):
	for i in range(2,n):
			if n % i == 0:
					return True
			if i > n/i:
					return False

# time complexity of below function is O(n*n-1) which I think is considered as O(n*n) ignoring the constants, because loop 1 is executed n times and loop 2 is executed at most n-1 times
def func(n):
		for i in range(n):
				for j in range(i):
						if j * j > I:
								break

# time complexity of below function is O(n log n), because loop 1 is executed n/2 times removing the constant, and second loop is executed log n times
def func(n):
		k=0
		for i in range(n//2, n):
				j=1
		    while (j <= n):
		        k += 1
						j *= 2
		return k

# time complexity of below 2 functions is O(n), because loop the only loop in the functions is executed less than n times
def helper_func(x):
	for i in range(x):
		print(i)
	return x
def func(n):
	if n == 2:
		return 0
	else:
		return helper_func(n - 1) + helper_func(n - 2)

# time complexity of below 2 functions is O(n*n), because both loops are executed n times
def helper_func(n):
		for i in range(n ** 2):
			print(i)
def func(n):
	for i in range(n ** 2):
		print(helper_func(100))
	return 0