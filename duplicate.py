def duplicate():
	i=0
	new_list=[]
	while i<len(string_list):
		if string_list[i] not in new_list:
			new_list.append(string_list[i])
		i=i+1
	print(new_list)
string_list=["delhi","delhi","mumbai","mumbai","delhi","chennai","chennai"]
duplicate()