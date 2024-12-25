def get_minrun(n):
        r = 0
        while n >= 64: #16
            r |= n & 1
            n >>= 1
        return n + r

def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n):
            j = i - 1
            while (j > -1) and abs(arr[j]) < abs(arr[j + 1]):
                elem = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = elem
                j -= 1

def find_first_greater(arr, start, T):
        left, right = start, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if abs(arr[mid]) < abs(T):
                right = mid - 1
            else:
                left = mid + 1
        return left

def find_runs(arr):
    n = len(arr)
    minrun = get_minrun(n)
    runs = []
    i = 0
    while i < n:
        run = [arr[i]]

        if i + 1 < n: 
            flag = abs(arr[i]) >= abs(arr[i+1])
        else: flag = False

        while i + 1 < n and (abs(arr[i]) >= abs(arr[i+1])) == flag:
            run.append(arr[i+1])
            i += 1

        if not flag:
            run.reverse()

        i += 1
        if len(run) < minrun:
            stop = i + minrun - len(run)
            run.extend(arr[i:stop])
            i = stop

        insertion_sort(run)
        runs.append(run)

    return runs

def merging_arr(arr1, arr2):
    i = j = 0
    count1, count2 = 0, 0
    gallop_count = 0
    res = []

    while i < len(arr1) and j < len(arr2):
        if abs(arr1[i]) >= abs(arr2[j]):
            res.append(arr1[i])
            i += 1
            count1 += 1
            count2 = 0
            
        else:
            res.append(arr2[j])
            j += 1
            count2 += 1
            count1 = 0

        if count1 == 7: #3
            gallop_count += 1
            stop = find_first_greater(arr1, i, arr2[j])
            while i < stop:
                res.append(arr1[i])
                i += 1

        if count2 == 7: #3
            gallop_count += 1
            stop = find_first_greater(arr2, j, arr1[i])
            while j < stop:
                res.append(arr2[j])
                j += 1
            
    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res, gallop_count

def merge_runs(runs):
    def cheking_invar(stack):
        return len(stack[-2]) > len(stack[-1]) and (len(stack) <= 2 or len(stack[-3]) > len(stack[-1]) + len(stack[-2]))
    def merge_in_stack(stack):
        if len(stack) == 2 or len(stack[-1]) <= len(stack[-3]):
            stack[-2], gallop_count = merging_arr(stack[-2], stack[-1])
            stack.pop()
            return gallop_count, stack[-1]
        else:
            stack[-3], gallop_count = merging_arr(stack[-2], stack[-3])
            stack.pop(-2)
            return gallop_count, stack[-2]

    stack = []
    merges = []
    for run in runs:
        stack.append(run)
        while len(stack) >= 2 and not cheking_invar(stack):
            merges.append(merge_in_stack(stack))

    while len(stack) > 1:
        merges.append(merge_in_stack(stack))

    return stack[0], merges

def timsort(arr):
    runs = find_runs(arr)
    res, gallop_and_merge = merge_runs(runs)
    
    for i in range(len(runs)):
        print(f'Part {i}: {" ".join(map(str,runs[i]))}')

    for i in range(len(gallop_and_merge)):
        print(f'Gallops {i}: {gallop_and_merge[i][0]}')  
        print(f'Merge {i}: {" ".join(map(str,gallop_and_merge[i][1]))}')

    return res

n = int(input())
arr = list(map(int,input().split()))
res = timsort(arr)
print(f'Answer:', " ".join(map(str,res)))
