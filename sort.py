# coding: utf-8
"""
排序算法汇总
排序算法可以分为内部排序和外部排序，内部排序是数据记录在内存中进行排序，
而外部排序是因排序的数据很大，一次不能容纳全部的排序记录，在排序过程中需要访问外存。
常见的内部排序算法有：插入排序、希尔排序、选择排序、冒泡排序、归并排序、快速排序、堆排序、基数排序等。
1、平方阶 (O(n2)) 排序 各类简单排序：直接插入、直接选择和冒泡排序。
2、线性对数阶 (O(nlog2n)) 排序 快速排序、堆排序和归并排序。
3、O(n1+§)) 排序，§ 是介于 0 和 1 之间的常数。 希尔排序。
4、线性阶 (O(n)) 排序 基数排序，此外还有桶、箱排序。
"""
arr0 = [0,1,1,2,3,4,5,6,7,8,9,10,11,12,12]

#冒泡排序
def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr1 = bubbleSort(arr0)
print("冒泡排序 arr1 =",arr1)


#插入排序
#1. 算法步骤
#1)将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
#2)从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
#3)（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr
arr2 = insertionSort(arr0)
print("插入排序 arr2 =",arr2)


#希尔排序
#希尔排序是把序列按下标的一定增量分组，对每组使用直接插入排序算法排序；
# 随着增量的逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个序列恰好被分为一组，算法便终止。

def shellSort(arr):
    import math
    gap = int(len(arr)/2)
    while gap > 0:
        for i in range(gap, len(arr)):

            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = int(gap/2)
    return arr
arr3 = shellSort(arr0)
print("希尔排序 arr3 =",arr3)


#归并排序

def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = int(len(arr)/2)
    left, right = arr[:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result
arr4 = mergeSort(arr0)
print("归并排序 arr4 =",arr4)


#快速排序
#在原列表修改
def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:  # 递归的退出条件
        return
    # import pdb;pdb.set_trace()
    mid = alist[start]  # 设定起始的基准元素
    low = start  # low为序列左边在开始位置的由左向右移动的游标
    high = end  # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[low] = mid  # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)  # start :0  low -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)  # low+1 : 原基准元素靠右一位  end: 最后

    return alist

arr5 = quick_sort(arr0, 0, len(arr0)-1)
print ("快速排序 arr5 =",arr5)

#计数排序
#计数排序(Counting Sort)是一种不比较数据大小的排序算法，是一种牺牲空间换取时间的排序算法。
#计数排序适合数据量大且数据范围小的数据排序
#1. 找到待排序列表中的最大值 k，开辟一个长度为 k+1 的计数列表，计数列表中的值都为 0。
#2. 走访待排序列表，如果走访到的元素值为 i，则计数列表中索引 i 的值加1。
#3. 走访完整个待排序列表，计数列表中索引 i 的值 j 表示 i 的个数为 j，统计出待排序列表中每个值的数量。
#4. 创建一个新列表，遍历计数列表，依次在新列表中添加 j 个 i，新列表就是排好序后的列表，整个过程没有比较待排序列表中的数据大小。

# coding=utf-8
def counting_sort(array):
    if len(array) < 2:
        return array
    max_num = max(array)
    count = [0] * (max_num + 1)
    for num in array:
        count[num] += 1
    new_array = list()
    for i in range(len(count)):
        for j in range(count[i]):
            new_array.append(i)
    return new_array

arr6 = counting_sort(arr0)
print ("计数排序 arr6 =",arr6)


#堆排序
#堆排序的算法实现
#最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
#创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
#堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算
#大根堆调整
def max_heapify(heap,heapSize,root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
    '''
    给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2  即：左子节点 + 1
    '''
    left = 2*root + 1
    right = left + 1
    larger = root
    # 小根堆只需要把下面and后面的条件改成：heap[larger] < heap[left] 和 heap[larger] < heap[right]
    # 当然，为了能见名知义，可以把larger换成smaller
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作，交换此时的最大值到root节点
        heap[larger], heap[root] = heap[root], heap[larger]
        # 递归的对子树做调整
        max_heapify(heap, heapSize, larger)

#建立大根堆
def build_max_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    heapSize = len(heap)
    for i in range((heapSize -2)//2,-1,-1):  # 自底向上建堆
        max_heapify(heap, heapSize, i)
#堆排序
def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    build_max_heap(heap)
    # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)
    return heap

arr7 = heap_sort(arr0)
print("堆排序 arr7 =",arr7)