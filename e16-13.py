def get_inverteds(a): 
	# Time-complexity: O(N^2)
	for i in range(0,len(a)):
		for j in range(i+1,len(a)):
			if (i < j) and (a[i] > a[j]):
				print("indexes: %d %d and values: %d %d" %(i,j,a[i], a[j]))

def get_inverteds2(a, c): 
	for i in range(0,len(a)):
		for j in range(i+1,len(a)):
			if (i < j) and (a[i] > a[j]):
				c = c + 1

def get_inverteds_efficient(a):
	# Time-complexity: O(N*logN)
	counter = 0
	merge_sort2(a, counter)
	return counter

def merge_sort2(lista, c):
	if len(lista) <= 3:
		get_inverteds2(lista, c)
		lista(3)
		return lista
	else:
		# [10 20] [1 4]
		mid = len(lista) / 2
		first = lista[:mid]
		second = lista[mid:]
		return merge2(merge_sort2(first , c), merge_sort2(second, c))

def merge2(lista_x,lista_y):

  if lista_x == []:
       return lista_y
  elif lista_y == []:
       return lista_x
  else:
      if lista_x[0] < lista_y[0]:
          return [lista_x[0]] + merge(lista_x[1:],lista_y)
      else:
          return [lista_y[0]] + merge(lista_x,lista_y[1:])


def merge_sort(lista):
	#Basic case, a list of size 1 is already sorted
	if len(lista) <= 1:
		return lista
	else:
		mid = len(lista) / 2
		return merge(merge_sort(lista[:mid]), merge_sort(lista[mid:]))

def merge(lista_x,lista_y):
  if lista_x == []:
       return lista_y
  elif lista_y == []:
       return lista_x
  else:
      if lista_x[0] < lista_y[0]:
          return [lista_x[0]] + merge(lista_x[1:],lista_y)
      else:
          return [lista_y[0]] + merge(lista_x,lista_y[1:])
 
a = [10, 20, 1, 4]
#print merge_sort(a)
#get_inverteds(a)
print get_inverteds_efficient(a)

