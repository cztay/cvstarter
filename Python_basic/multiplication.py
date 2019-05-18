while True:
	print("-" * 20)
	answer = input("Number[less than 10]:")
	number = int(answer)
	if number < 10:
		print("The table of", number)
		print("-" * 20)
		i = 1
		for i in range(1,11):
			result = i * number
			print (i, " * ", number, " =" , result)
			
		break
	else:
		print("Input number is greater than or equal to 10!")
		break

print("-" * 20)
print("Done counting...")
print("-" * 20)



