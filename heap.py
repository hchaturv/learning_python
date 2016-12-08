LEFT = lambda x: 2*x+1
RIGHT = lambda x: 2*x+2
MAX = 100

def swap(a, b):
    a = a+b
    b = a-b # a+b-b
    a = a-b # a+b-a
    return a,b

def heapify(idx,arr,size):
    largest = idx
    if LEFT(idx) < size and arr[largest] < arr[LEFT(idx)]:
        largest = LEFT(idx)
    if RIGHT(idx) < size and arr[largest] < arr[RIGHT(idx)]:
        largest = RIGHT(idx)
    if idx != largest:
        arr[idx],arr[largest] = swap(arr[idx],arr[largest])
        heapify(largest, arr, size)
    print "\n"

def create_heap(arr,size):
    i = size/2;
    while i >= 0:
        heapify(i,arr,size)
        i -=1
    return arr

def heap_sort(arr,size):
    i = size
    while i > 0:
        arr[0],arr[i-1] = swap(arr[0],arr[i-1])
        i-=1
        heapify(0,arr,i)
    
arr = []
size = int(raw_input("Enter size of array (MAX - 100)"))
if size > 100:
    print "size greater than 100, downsizing\n"
    size = 100
print "Enter the elements of the array: "
for i in range(0,size):
    arr.append(int(raw_input("Enter the element")))

print "Creating heap : \n"
create_heap(arr,size)
print "Heap : \n"
print arr
print "Sorting the array : \n"
heap_sort(arr,size)
print "The sorted array is: \n"
print arr
