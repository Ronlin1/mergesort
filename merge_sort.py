def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        right = array[mid:]
        left = array[:mid]

        mergesort(left)
        mergesort(right)

        i  = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

array =[23,43,902,4,67,8,12,69,34]
mergesort(array)
print(array)
