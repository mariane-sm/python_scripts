def digits_reverter(input):
	output = ""
	number_str = str(input)
	if input >= 0:
		for i in range(len(number_str)-1,-1,-1):
			output = output + number_str[i]
		return int(output)
	else:
		for i in range(len(number_str)-1,0,-1):
			output = output + number_str[i]	
		output = int(output)
		return output*-1

print digits_reverter(123) #321
print digits_reverter(-314) #-413