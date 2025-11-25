import sys

n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

inv = 0

class MergeSort:
    def __init__(self, lista):
        self.inv = 0
        self.sort(lista)

    def sort(self, lista) -> None:
        if len(lista) <= 1:
            return
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        self.sort(left)
        self.sort(right)
        l = r = 0
        idx = 0
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                lista[idx] = left[l]
                l += 1
            else:
                lista[idx] = right[r]
                r += 1
                self.inv += len(left) - l
            idx += 1
        
        while l < len(left):
            lista[idx] = left[l]
            l += 1
            idx += 1
        while r < len(right):
            lista[idx] = right[r]
            r += 1
            idx += 1

sorting = MergeSort(v)
sys.stdout.write(str(sorting.inv) + "\n")