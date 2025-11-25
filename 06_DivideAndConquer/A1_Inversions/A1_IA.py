import sys

n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

# Array auxiliar global para evitar creaciones repetidas
aux = [0] * n

def merge_sort(arr, temp, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) >> 1  # Bit shift más rápido que división
    
    inv_count = merge_sort(arr, temp, left, mid)
    inv_count += merge_sort(arr, temp, mid + 1, right)
    inv_count += merge(arr, temp, left, mid, right)
    
    return inv_count

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    
    # Mezclar los dos subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += mid - i + 1
            j += 1
        k += 1
    
    # Copiar elementos restantes con slice (más rápido en Python)
    if i <= mid:
        temp[k:right+1] = arr[i:mid+1]
    if j <= right:
        temp[k:right+1] = arr[j:right+1]
    
    # Copiar de vuelta con slice (más rápido que bucle for)
    arr[left:right+1] = temp[left:right+1]
    
    return inv_count

inversions = merge_sort(v, aux, 0, n - 1)
print(inversions)
