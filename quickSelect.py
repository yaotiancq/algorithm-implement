import random
import time


def generateRandomNumbers(n):
    """Return a list of n random numbers in range [1, n+1]"""
    if n <= 0:
        return []
    random_numbers = [random.randint(1, n+1) for _ in range(n)]
    return random_numbers

def insertionSort(arr):
    """Return the sorted array by using insertion sort algorithm"""
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element
    return arr

def quickSelect(arr, k):
    """Return the kth smallest element in arr by using quick select algorithm based on median of medians"""
    if len(arr) == 1:
        return arr[0]
    # Divide into groups of five and calculate the median of each group
    medians = [insertionSort(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
    median_of_medians = quickSelect(medians, len(medians)//2)

    # Partition the array into three parts based on the median of medians
    less = [x for x in arr if x < median_of_medians]
    equal = [x for x in arr if x == median_of_medians]
    greater = [x for x in arr if x > median_of_medians]

    # conque on smaller size of problem
    if k < len(less):
        return quickSelect(less, k)
    elif k < len(less) + len(equal):
        return median_of_medians
    else:
        return quickSelect(greater, k - len(less) - len(equal))

def timeCnt(fun,generateRandomNumbers,n):
    """calculate the average time of running fun fuction"""
    res=[]
    for i in range(100):
        arr=generateRandomNumbers(n)
        start=time.time()
        fun(arr,n//2)
        end=time.time()
        res.append(end-start)
    return sum(res)/100

def run():
    """run the program"""
    for i in [i*10000 for i in range(1,15)]:
        print(timeCnt(quickSelect,generateRandomNumbers,i))


if __name__=="__main__":
    run()
