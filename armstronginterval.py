#Print armstrong number between two intervals
a=int(input())
b=int(input())
for num in range(a, b + 1):
	order = len(str(num))
	sum = 0
	temp = num
	while temp > 0:
		digit = temp % 10
		sum += digit ** order
		temp //= 10
	if num == sum:
		print(num)
