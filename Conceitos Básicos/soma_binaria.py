def somar_binarios(a, b):
    c = []
    subiu = False
    for i in range(len(a) - 1, -1, -1):
        if subiu:
            if a[i] == 1 == b[i]:
                subiu = True
                c.append(1)
            elif a[i] == 1 and b[i] == 0 or a[i] == 0 and b[i] == 1:
                subiu = True
                c.append(0)
            else:
                subiu = False
                c.append(1)
        else:
            if a[i] == 1 == b[i]:
                subiu = True
                c.append(0)
            else:
                subiu = False
                c.append(a[i] + b[i])
    if subiu:
        c.append(1)
    else:
        c.append(0)
    c.reverse()
    return c


if __name__ == '__main__':
    a = [0, 0, 1, 0]
    b = [0, 1, 1, 0]
    print(somar_binarios(a, b))