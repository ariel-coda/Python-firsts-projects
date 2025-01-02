def simple_range(n):
    liste = []
    for i in range (n) :
        n -= 1
        liste.append(n)
        liste.sort()
    print(liste)

simple_range(5)