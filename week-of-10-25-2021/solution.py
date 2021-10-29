# Python:

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

# Notes: Assume the data is input by console.

def divisibleBy5(bin_string):

	num = 0

	for i, x in enumerate(bin_string[::-1]):
		if x == "1":
			num += 2 ** i

	return num % 5 == 0

if __name__ == "__main__":

	input_string = "0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111"
	nums = input_string.split(",")

	divisible = []

	for num in nums:
		if divisibleBy5(num):
			divisible.append(num)

	print(",".join(divisible))
