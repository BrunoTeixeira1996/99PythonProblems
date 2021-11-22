from itertools import groupby
from typing import List, Tuple, Any, Sequence

#01
def my_last(listx: list) -> str:
	return listx[-1]

#02
def my_but_last(listx: list) -> str:
	return listx[-2]

#03
def element_at(listx: list, element: int) -> str:
	return listx[element-1]

#04
def list_length(listx: list) -> int:
	return len(listx)

#05
def reverse_list(listx: list) -> list:
	return listx[::-1]

#06
def is_palindrome(listx: list) -> bool:
	return True if listx == listx[::-1] else False

#07
def flatten_list(listx: list) -> list:
    for index,value in enumerate(listx):
        while index < len(listx) and isinstance(listx[index],list):
            listx[index:index+1] = listx[index]
    return listx

#08
def del_consecutive(listx: list) -> list:
	aux = []
	for index,value in enumerate(listx):
		if index == 0 or value != listx[index-1]:
			aux.append(value)

	return aux

#09
def pack_consecutive(listx: list) -> list:
	temp = []
	aux = []

	for index,value in enumerate(listx):
		if index == 0 and value == listx[index+1]:
			temp.append(value)
		elif index == 0 and value != listx[index+1]:
			aux.append([value])
		elif (index + 1) < len(listx) and value == listx[index+1]:
			temp.append(value)
		elif (index + 1) < len(listx) and value != listx[index+1]:
			temp.append(value)
			aux.append(temp)
			temp = []
		elif index+1 == len(listx):
			temp.append(value)
			aux.append(temp)
			
	return aux

#09 with groupby
def pack_consecutive_group_by(listx: list) -> list:
	aux = []
	for char,value in groupby(listx):
		aux.append(list(value))

	return aux


#10
def run_lenght_encoding_data(listx: list) -> list[tuple]:
	aux = []
	temp = []
	
	for char,value in groupby(listx):
		temp.append([len(list(value)), char])

	for x in temp:
		aux.append(tuple(x))
	
	return aux

#11
def modified_run_lenght_encoding_data(listx: list) -> list[tuple]:
	aux = []
	first_temp = []
	second_temp = []
	
	# appends values has [[4,'a'], [1,'b'] ...]]
	for char,value in groupby(listx):
		first_temp.append([len(list(value)), char])

	# removes values that only has 1 element
	# [[4,'a'], 'b', ...]
	for values in first_temp:
		if values[0] != 1:
			second_temp.append(values)
		else:
			second_temp.append(values[1])

	# transforms lists in sets
	# [(4,'a'), 'b', ...]
	for x in second_temp:
		if isinstance(x, list):
			aux.append(tuple(x))
		else:
			aux.append(x)
	
	return aux

#12
def decode_run_length_enconded_list(listx: list) -> list:
	aux = []
	temp = 0
	for i in listx:
		temp = i[0]
		while temp > 0:
			aux.append(i[1])
			temp -= 1

	return aux


#14
def dup_elem_of_list(listx: list) -> list:
	aux = []
	for i in listx:
		aux.append(i)
		aux.append(i)

	return aux

#15
def replicate_elem_of_list_n_times(listx: list, n_times: int) -> list:
	return [element for element in listx for _ in range(n_times)]

#16
def drop_elem_of_list(listx: list, n_elem: int) -> list:
	temp = 0
	aux = []
	for i in listx:
		if temp == (n_elem - 1):
			temp = 0
		else:
			aux.append(i)
			temp += 1

	return aux

#17
def split_list(listx: list, n_part: int) -> list:
    return [listx[:n_part], listx[n_part:]]

#18
def slice_list(listx: list, i_elem: int, k_elem:int) -> list:
	return [listx[i_elem-1:k_elem]]


#19 TODO


#20
def remove_kelem_from_list(listx: list, k_elem: int) -> list:
	#[value for item,value in enumerate(listx) if item + 1 != k_elem]
	
	#listx[:k_elem - 1] + listx[k_elem:] 

	del listx[k_elem - 1]
	return listx
	

if __name__ == '__main__':
	# list1 = ['a','b','c','d']
	# print(my_last(list1))

	# list2 = ['a','b','c','d']
	# print(my_but_last(list2))

	# list3 = ['a','b','c','d','e']
	# print(element_at(list3,3))

	# list4 = ['a','b','c','d','e']
	# print(list_length(list4))

	# list5 = ['a','b','c','d','e']
	# print(reverse_list(list5))

	# list6 = ['x','a','m','a','x']
	# print(is_palindrome(list6))

	#list7 = ['a', ['b', ['c', 'd'], 'e'], 'f']
	#print(flatten_list(list7))

	#list8 = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
	#print(del_consecutive(list8))

	# list9 = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
	# print(pack_consecutive(list9))

	# list9 = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
	# print(pack_consecutive_group_by(list9))

	# list10 = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
	# print(run_lenght_encoding_data(list10))


	# list11 = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
	# print(modified_run_lenght_encoding_data(list11))

	# list12 = [[4,'a'],[1,'b'],[2,'c'],[2,'a'],[1,'d'],[4,'e']]
	# print(decode_run_length_enconded_list(list12))

	# list14 = ['a','b','c','d','e']
	# print(dup_elem_of_list(list14,2))

	# list15 = ['a','b','c','d','e']
	# print(replicate_elem_of_list_n_times(list15,3))

	# list16 = ['a','b','c','d','e','f','g','h','i','k']
	# print(drop_elem_of_list(list16,3))

	# list17 = ['a','b','c','d','e','f','g','h','i','k']
	# print(split_list(list17,2))

	# list18 = ['a','b','c','d','e','f','g','h','i','k']
	# print(slice_list(list18,3,7))

	list20 = ['a','b','c','d']
	print(remove_kelem_from_list(list20,2))
