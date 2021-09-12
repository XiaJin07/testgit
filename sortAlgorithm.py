#插入排序：将数组中的所有元素依次跟前面已经排好的元素相比较，如果选择的元素比已排序的元素小，则交换，直到全部元素都比较过为止
def insertionSort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        j = i-1
        while j>=0 and value<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1] = value
arr = [3,1,21,34,11,16,234,72]
print('插入排序前数组：',arr)
insertionSort(arr)
print('插入排序后的数组：',end='')
for i in range(1,len(arr)):
    print('%d'%arr[i],end=' ')


#快速排序：快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
arr = [10, 7, 28, 9, 153, 5]
print('\n快速排序前数组：',arr)
n = len(arr)
quickSort(arr, 0, n - 1)
print("快速排序后的数组:",end='')
for i in range(n):
    print("%d" %arr[i],end=' ')

#选择排序
#首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
def selectionSort(arr):
    for i in range(len(arr)):
        min_id = i
        for j in range(i+1,len(arr)):
            if arr[min_id]>arr[j]:
                min_id = j
        arr[i],arr[min_id] = arr[min_id],arr[i]
arr=[12,4,56,19,6,10,432,32]
print('\n选择排序前数组：',arr)
selectionSort(arr)
print('选择排序后的数组：',end=' ')
for i in range(len(arr)):
    print(arr[i],end=' ')

#冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [21,43,1,5,3,63,223,14]
print('\n冒泡排序前数组：',arr)
bubbleSort(arr)
print('冒泡排序后的数组：',end=' ')
for i in range(len(arr)):
    print('%d'%arr[i],end=' ')

