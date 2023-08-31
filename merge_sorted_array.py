import random

def merge_sorted_arr(arr1,arr2):
    j=0
    print(len(arr1),len(arr2))
    while(j<len(arr2)):
        for i in range(len(arr1)):
            if arr2[j]<=arr1[i]:
                arr1.insert(i,arr2[j])
                break
            if i==len(arr1)-1:
                arr1.append(arr2[j])
        j+=1
    return arr1

def genrate_random_arr():
    return sorted([i for i in range(random.randrange(2,10))])
print(merge_sorted_arr([0,3,4,31],[4,6,30]))
print(merge_sorted_arr([1,2,3,4],[5,6]))
print(merge_sorted_arr([5,6],[1,2,3,4]))
print(merge_sorted_arr(genrate_random_arr(),genrate_random_arr()))
print(merge_sorted_arr(genrate_random_arr(),genrate_random_arr()))
print(merge_sorted_arr(genrate_random_arr(),genrate_random_arr()))
print(merge_sorted_arr(genrate_random_arr(),genrate_random_arr()))
print(merge_sorted_arr(genrate_random_arr(),genrate_random_arr()))
print(merge_sorted_arr(genrate_random_arr(),genrate_random_arr()))
print(merge_sorted_arr(genrate_random_arr(),genrate_random_arr()))