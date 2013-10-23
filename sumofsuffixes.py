import timeit
import random

def divideEnum(arr):
	if(arr.len() == 1): return arr[0]
	arr1 = divideEnum(arr[:arr.len()/2])
	arr2 = divideEnum(arr[arr.len()-(arr.len()/2):])
	#in progress
	
	
def sumOfSuffixes(a, b):
	arrASum = getSumArr(a)
	arrBSum = getSumArr(b)
	arrBSum = [-x for x in arrBSum]
	arr = arrASum + arrBSum
	arr.sort()
	print([arrASum, arrBSum, arr])
		
def getSumArr(a):
	arr = []
	curSum = 0
	for i in a:
		arr.append(sum(a[a.index(i):]))	
	return arr

	
arr1 = [2,-2,3,-1,-4]
arr2 = [6,9,-7,8]
sumOfSuffixes(arr1, arr2)
