#lst = [int(elem) for elem in raw_input().split(" ")] 

lst = [1, 2, 3, 10, 4, 5, 6]

#lst.append(x) - adding x to list

def max2(x, y):
#	if x > y:
#		return x
#	else:
#		return y
	return x if x > y else y # x > y ? x : y

#max = reduce(max2, lst)
max = reduce(lambda x, y: x if x > y else y, lst)
print max

