

def recursive_activity_selector(a, r:list, k, n):
    m = k + 1    
    while m <= n and a[m]["start"] < a[k]["finish"]:  # encontrar em Sk a primeira atividade que termina
        m += 1
    if m <= n:
        r.append(a[m])
        recursive_activity_selector(a,r, m, n)    
    return r


if __name__ == "__main__":
    a = []                    
    d = {"start": 0,"finish": 0}
    a.append(d)
    d = {"start": 1,"finish": 4}
    a.append(d)
    d = {"start": 3,"finish": 5}
    a.append(d)
    d = {"start": 0,"finish": 6}
    a.append(d)
    d = {"start": 5,"finish": 7}
    a.append(d)
    d = {"start": 3,"finish": 9}
    a.append(d)
    d = {"start": 5,"finish": 9}
    a.append(d)
    d = {"start": 6,"finish": 10}
    a.append(d)
    d = {"start": 8,"finish": 11}
    a.append(d)
    d = {"start": 8,"finish": 12}
    a.append(d)
    d = {"start": 2,"finish": 14}
    a.append(d)
    d = {"start": 12,"finish": 16}
    a.append(d)
    
    r = []
    r = recursive_activity_selector(a, r, 0, 11)
    for a in r:
        for k, v in a.items():                        
            print(k, v)
        print("-"*10)

    