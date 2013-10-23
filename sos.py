

def sos(arrayB,arrayC):
	zeroest = arrayB[len(arrayB)-1]+arrayC[(len(arrayC)-1)]
	for s in range(len(arrayB)):
		for t in range(len(arrayC)):
			newSum = sumArrays(arrayB[s:],arrayC[t:])
			if isCloserToZero(newSum,zeroest):
				zeroest = newSum
				finalS = s
				finalT = t
	return [zeroest,finalS,finalT]

def ssos(arrayB,arrayC):	
	zeroest = arrayB[len(arrayB)-1]+arrayC[(len(arrayC)-1)]
	combineArray = fuseArrays(arrayB,arrayC)
	for i in range(len(combineArray)-2):
		if (combineArray[i][1]!=combineArray[i+1][1]):
			if (combineArray[i][1]=='b'):
				if isCloserToZero(combineArray[i][0]-combineArray[i+1][0],zeroest):
					zeroest = combineArray[i][0]-combineArray[i+1][0]
			if (combineArray[i][1]=='c'):
				if isCloserToZero(combineArray[i+1][0]-combineArray[i][0],zeroest):
					zeroest = combineArray[i+1][0]-combineArray[i][0]
	return zeroest

def fuseArrays(arrayB,arrayC):
	for i in range(len(arrayB)):
		arrayB[i] = [sum(arrayB[i:]),'b']
	for j in range(len(arrayC)):
		arrayC[j] = [-sum(arrayC[j:]),'c']
	arrayOut = arrayB+arrayC
	arrayOut.sort(reverse=True)
	return arrayOut

def sumArrays(arrayA,arrayB):
	return sum(arrayA)+sum(arrayB)

# True if first arg is closer to zero, False if is second arg is closer to zero or they are equal
def isCloserToZero(t, f):
	t = abs(t)
	f = abs(f)
	if (t>=f): return False
	return True
