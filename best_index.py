import math
import random
def bestindex(a):
	major_sum=0
	index=-1
	biggest=-math.inf
	for i in range(len(a)):
		# print("current i",i)
		major_sum=0
		sum=0
		ruler=2
		j=i+1
		limit=0
		major_sum+=a[i]
		# print("current element",a[i])
		# print("major sum is",major_sum)
		while(j<len(a)):
			if limit<ruler:
				# print("current element",a[j])
				sum+=a[j]
				j+=1
				limit+=1
			if limit==ruler:
				# print("done ruler")
				ruler+=1
				limit=0
				major_sum+=sum
				# print("major sum is",major_sum)
				sum=0
		# print("major sum for ",i,"element",major_sum)
		if major_sum>biggest:
			
			biggest=major_sum
			index=i
		# print("biggest",biggest)
	return index,biggest

def genreate_random_arr(size):
    return [random.randrange(-10**7,10**7) for i in range(size)]
print(bestindex(genreate_random_arr(10000)))
#print(bestindex([1,3,1,2,5]))
# print(bestindex([2,1,3,9,2,4 ,-10, -9 ,1, 3]))
#print(bestindex([-3,2,3,-4,3,1]))