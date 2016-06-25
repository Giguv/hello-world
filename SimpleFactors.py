def simple_factors(num):
	arr = []
	i = 2
	numorg = num
	numd = num//2 + 1
	while num != 1:
		if num % i == 0:
			arr.append(i)
			num /= i
			continue
		i +=1
		if i == numd:
			arr.append(numorg)
			print("prime number found!")
			break
	return arr
	
try:
	print(simple_factors(int(input())))
except (TypeError, ValueError):
	print("aborted: number not valid")
input()
