#******************************METODO DE BURBUJA*********************************
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso:
mi_lista = [64, 34, 25, 12.5, 12, 22, 11, 90]
bubble_sort(mi_lista)
print("Lista ordenada usando Bubble Sort:", mi_lista)

#***************************POR SELECCION*************************************
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Ejemplo de uso:
mi_lista = [64, 25, 12, 22, 11]
selection_sort(mi_lista)
print("Lista ordenada usando Selection Sort:", mi_lista)

#****************************POR INSERCION************************************
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso:
mi_lista = [12, 11, 13, 5, 6]
insertion_sort(mi_lista)
print("Lista ordenada usando Insertion Sort:", mi_lista)

#************************ORDENAMIENTO RAPIDO*****************************
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Ejemplo de uso:
mi_lista = [10, 7, 8, 9, 1, 5]
mi_lista_ordenada = quick_sort(mi_lista)
print("Lista ordenada usando Quick Sort:", mi_lista_ordenada)