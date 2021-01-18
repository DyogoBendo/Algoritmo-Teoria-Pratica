def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j-1]:
                anterior = a[j]
                a[j] = a[j-1]
                a[j-1] = anterior


if __name__ == '__main__':
    entrada = list(map(int, input().split(', ')))
    bubblesort(entrada)
    print(entrada)
