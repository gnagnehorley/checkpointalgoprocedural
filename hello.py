# Définition de la fonction dot_product
def dot_product(v1, v2):
    ps = 0
    for i in range(len(v1)):
        ps += v1[i] * v2[i]
    return ps

# Algorithme pour déterminer si deux vecteurs sont orthogonaux
def are_orthogonal(vectors):
    for v1, v2 in vectors:
        ps = dot_product(v1, v2)
        if ps == 0:
            print("Les vecteurs", v1, "et", v2, "sont orthogonaux.")
        else:
            print("Les vecteurs", v1, "et", v2, "ne sont pas orthogonaux.")

# Exemple d'utilisation
vectors = [([1, 0], [0, 1]), ([1, 2], [2, -1]), ([-3, 1], [1, 3])]
are_orthogonal(vectors)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Exemple d'utilisation
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Tableau trié par insertion:", arr)